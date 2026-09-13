SELECT o.operator_id, o.name, q.expires_on FROM operators o LEFT JOIN qualifications q ON o.operator_id=q.operator_id AND q.qualification='mission_operator' ORDER BY o.operator_id;
