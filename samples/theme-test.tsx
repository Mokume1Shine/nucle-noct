import { useState } from "react";

type ThemeCardProps = {
  title: string;
  accent: string;
  active?: boolean;
};

export function ThemeCard({ title, accent, active = true }: ThemeCardProps) {
  const [count, setCount] = useState(0);

  return (
    <section className={`theme-card ${active ? "is-active" : "is-idle"}`}>
      <h2>{title}</h2>
      <p style={{ color: accent }}>NucleNoct preview</p>
      <button onClick={() => setCount((value) => value + 1)}>count: {count}</button>
    </section>
  );
}
