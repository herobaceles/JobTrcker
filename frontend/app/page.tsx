"use client";

<<<<<<< HEAD
=======
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
>>>>>>> ea4caaf (Initial commit)
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

export default function Home() {
<<<<<<< HEAD
=======
  const { status } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (status === "authenticated") {
      router.push("/dashboard"); // Automatically skip the landing page
    }
  }, [status, router]);

  if (status === "loading") {
    return null; // Prevents the login panel from flashing briefly on refresh
  }

>>>>>>> ea4caaf (Initial commit)
  return (
    <main className="min-h-screen bg-gray-50">
      <Navbar />
      <Hero />
    </main>
  );
}