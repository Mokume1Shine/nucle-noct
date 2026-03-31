type UserProfile = {
  id: string;
  displayName: string;
  role: "viewer" | "editor" | "admin";
  isActive: boolean;
  score: number;
  accent?: string;
};

const users: UserProfile[] = [
  { id: "u_001", displayName: "Aster", role: "viewer", isActive: true, score: 12, accent: "#00A6C8" },
  { id: "u_002", displayName: "Mira", role: "admin", isActive: true, score: 28, accent: "#FE9F2F" },
  { id: "u_004", displayName: "Lyra", role: "editor", isActive: false, score: 10 },
];

function formatUser(user: UserProfile): string {
  const badge = user.isActive ? "ONLINE" : "OFFLINE";
  const tone = user.accent ?? "#355C68";
  return `${user.displayName} [${user.role}] - ${badge} (${user.score}) ${tone}`;
}

function buildSummary(items: UserProfile[]): string[] {
  return items
    .filter((user) => user.isActive || user.role === "admin")
    .sort((left, right) => right.score - left.score)
    .map((user) => formatUser(user));
}

console.log(buildSummary(users));
