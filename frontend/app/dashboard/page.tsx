"use client";

import { useEffect, useState } from "react";
import { getPortfolio, addAsset, deleteAsset } from "../../services/api";
import { useRouter } from "next/navigation";

export default function DashboardPage() {
  const [portfolio, setPortfolio] = useState<any>(null);
  const [name, setName] = useState("");
  const [symbol, setSymbol] = useState("");
  const [quantity, setQuantity] = useState("");
  const router = useRouter();

  const token =
    typeof window !== "undefined" ? localStorage.getItem("token") : null;

  useEffect(() => {
    if (!token) {
      router.push("/login");
      return;
    }
    loadPortfolio();
  }, []);

  async function loadPortfolio() {
    try {
      const data = await getPortfolio(token!);
      setPortfolio(data);
    } catch {
      router.push("/login");
    }
  }

  async function handleAdd() {
    await addAsset(token!, {
      name,
      symbol,
      quantity: Number(quantity),
    });
    setName("");
    setSymbol("");
    setQuantity("");
    loadPortfolio();
  }

  async function handleDelete(id: number) {
    await deleteAsset(token!, id);
    loadPortfolio();
  }

  if (!portfolio) return <p>Chargement...</p>;

  return (
    <div className="dashboard">
      <h1>Mon portefeuille</h1>
      <h2>Valeur totale : {portfolio.total_value} €</h2>

      {portfolio.assets.map((a: any) => (
        <div className="asset" key={a.id}>
          <span>
            {a.name} ({a.symbol}) — {a.quantity} → {a.value} €
          </span>
          <button onClick={() => handleDelete(a.id)}>Supprimer</button>
        </div>
      ))}

      <div className="add-asset">
        <h3>Ajouter un actif</h3>
        <input placeholder="Nom" value={name} onChange={e => setName(e.target.value)} />
        <input placeholder="Symbole" value={symbol} onChange={e => setSymbol(e.target.value)} />
        <input placeholder="Quantité" value={quantity} onChange={e => setQuantity(e.target.value)} />
        <button onClick={handleAdd}>Ajouter</button>
      </div>
    </div>
  );
}
// hello