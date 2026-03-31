type UserProfile = {
  id: string;
  name: string;
  role: "viewer" | "editor";
  active: boolean;
  score: number;
};

const users: UserProfile[] = [
  { id: "u_001", name: "Aster", role: "viewer", active: true, score: 12 },
  { id: "u_002", name: "Mira", role: "editor", active: false, score: 8 },
  { id: "u_003", name: "Noct", role: "viewer", active: true, score: 17 },
];

function formatUser(user: UserProfile): string {
  const badge = user.active ? "ACTIVE" : "IDLE";
  return `${user.name} [${user.role}] - ${badge} (${user.score})`;
}

function buildSummary(items: UserProfile[]): string[] {
  return items
    .filter((user) => user.active)
    .map((user) => formatUser(user));
}

console.log(buildSummary(users));
