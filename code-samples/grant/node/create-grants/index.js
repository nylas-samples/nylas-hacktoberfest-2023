import * as dotenv from "dotenv";
import express from "express";
import Nylas from "nylas";

dotenv.config();

const nylas = new Nylas({
  apiKey: process.env.API_KEY,
});

const app = express();

app.use(express.json());

app.get("/oauth", async (_, res) => {
  const authUrl = await nylas.auth.urlForOAuth2({
    clientId: process.env.CLIENT_ID,
    redirectUri: "http://localhost:3000/oauth/exchange",
    provider: "google",
  });

  return res.redirect(authUrl);
});

app.get("/oauth/exchange", async (req, res) => {
  const { code } = req.query;

  const resp = await nylas.auth.exchangeCodeForToken({
    code,
  });

  const newGrants = await nylas.auth.grants.create({
    requestBody: {
      provider: "google",
      settings: {
        refreshToken: resp.refreshToken,
      },
    },
  });

  console.log(newGrants.data);

  return res.send("hello");
});

app.listen(3000, () => {
  console.log("App running on port 3000.");
});
