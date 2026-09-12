# Training base tag: mutable. Record the built image ID and promote that same image.
# See docs/deployment.md for digest pinning before real deployment.
FROM python:3.14-alpine
# Apply the upstream fix for the inherited libuuid package before dropping privileges.
RUN apk add --no-cache "libuuid>=2.42.3-r1"
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY guardrails/ ./guardrails/
USER 10001:10001
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz',timeout=2).close()"]
CMD ["python", "-m", "guardrails.app", "--host", "0.0.0.0"]
