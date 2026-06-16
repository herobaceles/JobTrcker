import NextAuth from "next-auth";
import Google from "next-auth/providers/google";

const handler = NextAuth({
  providers: [
    Google({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],

  secret: process.env.NEXTAUTH_SECRET,

  callbacks: {
    async jwt({ token, account }) {
      if (account) {
        token.id_token = account.id_token;
      }
      return token;
    },

    async session({ session, token }) {
      (session as any).id_token = token.id_token;
      return session;
    },
  },
});

export { handler as GET, handler as POST };