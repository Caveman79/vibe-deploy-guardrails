"""Read only course reader. Only registered Markdown files can be served."""
from pathlib import Path
from html import escape
import re
from urllib.parse import quote
from guardrails.ui import page
ROOT = Path(__file__).resolve().parents[1]
FILES = {p.relative_to(ROOT).as_posix(): p for folder in ('lessons','labs','docs','assessments','case-studies','interview-drills') for p in (ROOT/folder).rglob('*.md')}
FILES.update({name: ROOT/name for name in ('START_HERE.md','CURRICULUM.md','CAPSTONE.md','INTERVIEW_TRANSLATION.md')})

def inline(text, source):
    def link(m):
        label, target = m.groups()
        resolved = (source.parent / target.split('#')[0]).resolve()
        key = resolved.relative_to(ROOT).as_posix() if resolved.is_relative_to(ROOT) else ''
        if key in FILES:
            return '<a href="/lesson?name='+quote(key)+'">'+escape(label)+'</a>'
        if target.startswith('https://'):
            return '<a href="'+escape(target,quote=True)+'">'+escape(label)+'</a>'
        return escape(label)+' <small>(repository file: '+escape(target)+')</small>'
    parts=[]; start=0
    for m in re.finditer(r'\[([^]]+)\]\(([^)]+)\)',text):
        parts.append(escape(text[start:m.start()])); parts.append(link(m)); start=m.end()
    parts.append(escape(text[start:])); result=''.join(parts)
    result=re.sub(r'`([^`]+)`',r'<code>\1</code>',result)
    return re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',result)

def lesson(name):
    if name not in FILES or not FILES[name].is_file():
        raise ValueError('unknown lesson')
    source=FILES[name]; out=[]; code=None; language=''; table=False; listing=False
    # Preserve fenced code but join Markdown soft line breaks into paragraphs.
    lines=[]; paragraph=[]; fenced=False
    for raw in source.read_text().splitlines():
        boundary = fenced or not raw.strip() or raw.startswith(('#','|','```')) or re.match(r'^[-*] |^[0-9]+[.] ',raw)
        if boundary:
            if paragraph: lines.append(' '.join(paragraph)); paragraph=[]
            lines.append(raw)
        else: paragraph.append(raw.strip())
        if raw.startswith('```'): fenced=not fenced
    if paragraph: lines.append(' '.join(paragraph))
    for line in lines:
        if not line.startswith('|') and table:
            out.append('</tbody></table></div>'); table=False
        if not re.match(r'^[-*] |^[0-9]+[.] ',line) and listing:
            out.append('</ul>'); listing=False
        if line.startswith('```'):
            if code is None: code=[]; language=line[3:]
            else:
                label={'bash':'Run in your terminal, from the course folder','sql':'SQL — save in a .sql file, then run it with the query command','python':'Python code — read the instructions before running','json':'Example data'}.get(language,'Example / reference')
                out.append('<div class="card"><small>'+label+'</small><pre>'+escape('\n'.join(code))+'</pre></div>'); code=None
        elif code is not None: code.append(line)
        elif line.startswith('|'):
            cells=[x.strip() for x in line.strip('|').split('|')]
            if all(re.fullmatch(r'[: -]+',x) for x in cells): continue
            if not table:
                out.append('<div class=table-wrap><table><tbody>'); table=True
                tag='th'
            else: tag='td'
            out.append('<tr>'+''.join('<'+tag+'>'+inline(x,source)+'</'+tag+'>' for x in cells)+'</tr>')
        elif re.match(r'^[-*] |^[0-9]+[.] ',line):
            if not listing: out.append('<ul>'); listing=True
            out.append('<li>'+inline(re.sub(r'^[-*] |^[0-9]+[.] ','',line),source)+'</li>')
        elif line.startswith('#'):
            level=min(len(line)-len(line.lstrip('#')),6); out.append(f'<h{level}>'+inline(line[level:].strip(),source)+f'</h{level}>')
        elif line.strip(): out.append('<p>'+inline(line,source)+'</p>')
    if table: out.append('</tbody></table></div>')
    if listing: out.append('</ul>')
    if code is not None: out.append('<pre>'+escape('\n'.join(code))+'</pre>')
    return page(source.stem,'<nav><a href="/">Course home</a><a href="/course">All lessons</a></nav>'+''.join(out))

def index():
    return lesson('CURRICULUM.md')
