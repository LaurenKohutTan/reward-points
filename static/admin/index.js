function modify_points(points, user, delta) {
  points[user] = (points[user] ?? 0) + delta;
  if (points[user] == 0) delete points[user];
}

function keys(obj) {
  return Object.keys(obj).length;
}

async function save(students, points) {
  const response = await fetch("/api/save", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(points),
  });
  const result = await response.json();
  for (let key in result) delete points[key];

  const studentsResponse = await fetch("/api/students");
  const studentsData = await studentsResponse.json();
  students.length = 0;
  students.push(...studentsData);
}

async function deactivate(student) {
  const msg = `Are you sure you want to deactivate ${student.name.full}'s account?`;
  if (!confirm(msg)) return;

  const response = await fetch(`/api/delete`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify([student.id]),
  });
}
