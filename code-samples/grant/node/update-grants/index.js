import * as dotenv from "dotenv";
import Nylas from "nylas";
import inquirer from "inquirer";

dotenv.config();

const nylas = new Nylas({
  apiKey: process.env.API_KEY,
});

const grants = await nylas.auth.grants.list();

async function main() {
  if (grants.data.length === 0) {
    console.log("No grants found!");
    return;
  }

  console.clear();
  try {
    const answer = await inquirer.prompt([
      {
        type: "list",
        name: "grant",
        message: "Please select a Gmail account to update:",
        choices: grants.data.map(({ email, id }) => ({
          name: email,

          value: {
            id,
            email,
          },
        })),
      },
      {
        type: "checkbox",
        name: "scopes",
        message: "Scopes:",
        choices: [
          {
            name: "Gmail ReadOnly",
            value: "gmail.readonly",
          },
          {
            name: "Gmail Send",
            value: "gmail.send",
          },
          {
            name: "Gmail Modify",
            value: "gmail.modify",
          },
          {
            name: "Calendar",
            value: "calendar",
          },
          {
            name: "Contacts",
            value: "contacts",
          },
        ],
      },
    ]);

    const { requestId, data: grant } = await nylas.auth.grants.update({
      grantId: answer.grant.id,
      requestBody: {
        scope: answer.scopes,
      },
    });

    const greenColorCode = "\x1b[32m%s\x1b[0m";
    console.log(greenColorCode, "\n❯ Grant updated successfully!");
    console.log(
      greenColorCode,
      `
  UPDATED GRANT DETAILS:
  ===============================
  Request ID: ${requestId}
  Grant ID: ${grant.id}
  Email: ${answer.grant.email}
  Scopes: ${grant.scope}
  ===============================
    `
    );

    const askAgainPrompt = await inquirer.prompt([
      {
        type: "confirm",
        name: "askAgain",
        message: "Do you want to update another grant?",
      },
    ]);

    if (askAgainPrompt.askAgain) {
      await main();
    } else {
      console.log("Goodbye!");
    }
  } catch (error) {
    console.error("An error occurred:", error);
  }
}

main();
