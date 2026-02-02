const API_URL = "http://localhost:8000";

export async function login(email: string, password: string) {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) throw new Error("Login failed");
  return res.json();
}

export async function getPortfolio(token: string) {
  const res = await fetch(`${API_URL}/portfolio`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) throw new Error("Unauthorized");
  return res.json();
}

export async function addAsset(token: string, asset: {
  name: string;
  symbol: string;
  quantity: number;
}) {
  const res = await fetch(`${API_URL}/portfolio`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(asset),
  });

  if (!res.ok) throw new Error("Error adding asset");
}

export async function deleteAsset(token: string, id: number) {
  await fetch(`${API_URL}/portfolio/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
