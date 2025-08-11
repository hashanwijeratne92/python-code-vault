<h1>⏳ Countdown Timer with Custom Message</h1>

<h2>📝 Project Task</h2>

<p>The program should:</p>
<ul>
  <li>Prompt the user to enter a starting number (e.g., <code>10</code>).</li>
  <li>Count down to <code>1</code> using a <code>for</code> or <code>while</code> loop, printing each number with a 1-second delay between prints.</li>
  <li>After the countdown, display a final message like <code>Time’s up!</code> or <code>Go!</code>.</li>
  <li>Ensure the user enters a positive integer before starting.</li>
  <li>Allow the user to choose the final message before the countdown begins.</li>
</ul>

<p>This is a fun utility app that helps you practice loops, timing, and user input handling in the terminal.</p>

<h2>💻 Example Solutions</h2>

<details>
  <summary><strong>Method 1 – Basic Countdown with Input Check</strong></summary>
  <p>Validates the user’s entry to ensure it’s a positive digit, then runs the countdown using <code>range()</code> and <code>time.sleep()</code> for timing.</p>
</details>

<details>
  <summary><strong>Method 2 – Enhanced Countdown with Error Handling</strong></summary>
  <p>Adds stronger input validation by wrapping the process in a <code>try-except</code> block to catch non-integer values, and applies <code>.strip()</code> to clean unwanted spaces from the user’s entry.</p>
</details>

<h3>📊 Approach Overview</h3>
<ul>
  <li><strong>Basic Version:</strong> Minimal code and easy to read — good for beginners or quick scripts.</li>
  <li><strong>Enhanced Version:</strong> More defensive programming — ideal for a polished and user-friendly tool.</li>
</ul>

<p>If you’re aiming for a more reliable, production-style script, go with the enhanced version.</p>

<h2>📌 Acknowledgments</h2>
<p>This project challenge is inspired by <a href="https://dailypythonprojects.substack.com/" target="_blank">Daily Python Projects</a>, a platform that provides daily coding exercises to improve Python skills.</p>
<p>All credit for the original challenge idea goes to <strong>Daily Python Projects</strong>.
