function modify_points(points, user, delta) {
  points[user] = (points[user] ?? 0) + delta;
  if (points[user] == 0) delete points[user];
}

function keys(obj) {
  return Object.keys(obj).length;
}

function save(points) {
  fetch("/api/save", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(points),
  })
    .then((x) => x.json())
    .then((x) => alert(`Saved: ${JSON.stringify(x)}`));
}
