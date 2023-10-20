import * as dotenv from "dotenv";
import express from "express";
import Nylas from "nylas";

dotenv.config();

const nylas = new Nylas({
  apiKey: process.env.API_KEY,
});

const redirectUri = "http://localhost:3000/oauth/exchange";

const app = express();

app.use(express.json());

app.get("/oauth", async (_, res) => {
  const authUrl = await nylas.auth.urlForOAuth2({
    clientId: process.env.CLIENT_ID,
    provider: "google",
    redirectUri,
  });

  return res.redirect(authUrl);
});

app.get("/oauth/exchange", async (req, res) => {
  const { code } = req.query;

  try {
    const resp = await nylas.auth.exchangeCodeForToken({
      clientSecret: process.env.CLIENT_SECRET,
      clientId: process.env.CLIENT_ID,
      code,
      redirectUri,
    });

    console.log("===========================");
    console.log(resp);
    console.log("===========================");

    const newGrants = await nylas.auth.grants.create({
      requestBody: {
        provider: "google",
        scope: resp.scope,
        settings: {
          refreshToken: resp.refreshToken,
        },
      },
    });

    console.log(newGrants.data);
  } catch (error) {
    return res.json(error);
  }

  return res.send("hello");
});

app.listen(3000, () => {
  console.log("App running on port 3000.");
});
