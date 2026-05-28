# Hate the Game

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F35%2Fc9%2F33%2F35c93381f2a65582e6dfc5d077e71cbd.jpg&f=1&nofb=1&ipt=905c02b0639659df279ef6e1b9288303d74e8817315646f4bad5815999c2dc49" align="right"
alt="Sweaty" width="260" height="178">

When you wake up at 5:30am to book a desk and they're all gone 😐. If you can't beat them... join them.

## How It Works

Firstly, this took way longer than it should have. The CondecoBooker just mimics the same http requests made by the browser. It is not fully fleshed yet (and I probs won't be bothered to add more functionality).

_TODO: Verify booking was successful as a 200 status code unfortunately is not enough_

## Usage

### Specify the Environment

The project expects a .env file in the project root. e.g.

```sh
# .env file
CONDECO_HOST="exampledomain.com"
CONDECO_USER_EMAIL="exampleemail@blah.com"
CONDECO_USER_PWD="plaintextpassword"
```

### Poetry :)

Install poetry if you haven't already. https://python-poetry.org/

<details><summary><b>Show instructions</b></summary>

1. Install the dependencies:

   ```sh
   poetry install
   ```

2. You might need to set your PYTHONPATH environment variable:

   ```sh
   export PYTHONPATH=$(pwd)
   ```

3. Then you're ready to go. You might need to set your PYTHONPATH environment variable:

   ```sh
   poetry run python ./examples/autobook.py
   ```

</details>

### 🚀 Alternative Recommended Easy Setup

Follow these steps to deploy your own automated desk booker using GitHub Actions.

<details><summary><b>Show instructions</b></summary>

#### 1. Retrieve your Desk ID
Before configuring the code, you need to identify which desk you want to book.
1. Open your browser and navigate to the Condeco booking page.
2. Open **Developer Tools** (`F12` or `Cmd+Opt+I`) and go to the **Network** tab.
3. Perform a "Book" or "Unbook" action on your desk.
4. Look for the network request triggered by this action.
5. Inspect the **Payload** (or Request Body) of that message.
6. Locate and copy your `desk_id`.

#### 2. Prepare the Repository
1. **Fork** this repository to your own GitHub account.
2. In your fork, open `condeco.py`.
4. Locate **line 164** and replace the placeholder string with your retrieved `desk_id`.
5. Now, open `autobook.py`.
6. Locate **line 8** and replace it with your timezon in `Region/City` format (e.g., `Australia/Brisbane` or `America/New_York`).
   *If unsure, search Google for "IANA timezone" or check the [Wikipedia List](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).*
7. Commit your changes.

#### 3. Configure GitHub Secrets
To keep your credentials secure, do **not** hardcode them. Use GitHub Actions Secrets instead:
1. Navigate to your repository on GitHub.
2. Go to **Settings** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
3. Click **New repository secret** and add the following (do not include curly braces):
    * `CONDECO_HOST`: Your Condeco website address (e.g., `exampledomain.com`)
    * `CONDECO_USER_EMAIL`: Your Condeco login email.
    * `CONDECO_USER_PWD`: Your Condeco login password.

#### 4. Generate a GitHub Personal Access Token (PAT)
The cron job needs permission to trigger your GitHub Action.
1. Click your GitHub profile picture $\rightarrow$ **Settings**.
2. Scroll down to **Developer settings** (bottom of left sidebar).
3. Select **Personal access tokens** $\rightarrow$ **Fine-grained tokens**.
4. Click **Generate new token**.
5. Give it a name and ensure it has permissions to "Actions: Read and Write."
6. **Copy this token immediately**; you will need it for the next step.

#### 5. Automate with a Cron Job
We will use [cron-job.org](https://cron-job.org) to trigger the booking script daily.
1. Create an account and log in to [cron-job.org](https://cron-job.org).
2. Click **'CREATE CRONJOB'**.
3. **Title:** `Hate the Game - Daily Desk Booking`
4. **URL:** Enter the following, replacing `{your_username}` with your GitHub username:
   `https://api.github.com/repos/{your_username}/hatethegame/actions/workflows/autobook.yml/dispatches`
5. **Schedule:** Select your preferred execution time (e.g., every day at 5:25 AM).
6. **Advanced Settings (Headers):** Add the following headers:

| Key | Value |
| :--- | :--- |
| `Accept` | `application/vnd.github+json` |
| `Authorization` | `Bearer YOUR_GITHUB_TOKEN_HERE` |
| `Content-Type` | `application/json` |
| `X-GitHub-Api-Version` | `2022-11-28` |

7. **Request Method:** `POST`
8. **Request Body:** `{"ref": "main"}`
9. **Timezone:** Enter your timezone in `Region/City` format (e.g., `Australia/Brisbane` or `America/New_York`). 
10. Click **Save**.

> [!TIP]
> **Testing:** To verify everything is working, set your cron job to run in 5 minutes, or manually trigger the workflow in your GitHub "Actions" tab.

</details>

## Disclaimer

I'm not responsible for anything that goes wrong if you choose to use this. Enjoy responsibly.
