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
        name: "grantId",
        message: "Select an email:",
        choices: grants.data.map(({ email, id }) => ({
          name: email,

          value: id,
        })),
      },
    ]);

    const { data: selectedGrants } = await nylas.auth.grants.find({
      grantId: answer.grantId,
    });

    console.log(`
    ============================================
    Selected Email: ${selectedGrants.email} 
    ID: ${selectedGrants.id}
    Status: ${selectedGrants.grantStatus}
    Provider: ${selectedGrants.provider}
    Created At: ${new Date(selectedGrants.createdAt)}
    Scopes: ${selectedGrants.scope.reduce(
      (acc, cur) => `${acc} ${cur.split("/").at(-1)},`.trim(),
      ""
    )}
    ============================================
  `);

    const askAgainPrompt = await inquirer.prompt([
      {
        type: "confirm",
        name: "askAgain",
        message: "Do you want to continue?",
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
