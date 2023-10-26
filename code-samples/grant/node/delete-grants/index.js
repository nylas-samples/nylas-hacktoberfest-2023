import * as dotenv from "dotenv";
import Nylas from "nylas";
import inquirer from "inquirer";

dotenv.config();

const nylas = new Nylas({
  apiKey: process.env.API_KEY,
});

async function main() {
  const grants = await nylas.auth.grants.list();

  if (grants.data.length === 0) {
    console.log("No grants found!");
    return;
  }

  console.clear();
  try {
    const answer = await inquirer.prompt([
      {
        type: "list",
        name: "grants",
        message: "Select an email to delete:",
        choices: grants.data.map(({ email, id }) => ({
          name: email,

          value: {
            id,
            email,
          },
        })),
      },
    ]);

    const { requestId } = await nylas.auth.grants.destroy({
      grantId: answer.grants.id,
    });

    console.log("Grants deleted successfully!");
    console.log(`
DETAILS:
===============================
Request ID: ${requestId}
GRANTS ID: ${answer.grants.id}
Email: ${answer.grants.email}
===============================
`);

    const askAgainPrompt = await inquirer.prompt([
      {
        type: "confirm",
        name: "askAgain",
        message: "Do you want to delete another grants?",
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
