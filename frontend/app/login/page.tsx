"use client";

import { useState } from "react";
import { login } from "../../services/api";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    try {
      const data = await login(email, password);
      localStorage.setItem("token", data.access_token);
      router.push("/dashboard");
    } catch {
      alert("Login incorrect");
    }
  }

  return (
    <main>
      <div className="card">
        <h1>Connexion</h1>

        <form onSubmit={handleLogin}>
          <input
            placeholder="Email"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Mot de passe"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />

          <button type="submit">Se connecter</button>
        </form>

        <div className="link">
          <Link href="/register">Créer un compte</Link>
        </div>
      </div>
    </main>
  );
}
