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

    console.log("GRANT ID: ", resp.grantId);

    return res.statusCode(201).json(resp);
  } catch (error) {
    return res.statusCode(400).json(error);
  }
});

app.listen(3000, () => {
  console.log("App running on port 3000.");
});
