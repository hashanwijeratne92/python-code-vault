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
  <summary><strong>Approach 1 – Basic Input Validation</strong></summary>
  <p>Checks if the input is a positive number using <code>isdigit()</code>, then performs the countdown using <code>range()</code> and <code>time.sleep()</code>.</p>
</details>

<details>
  <summary><strong>Approach 2 – Robust Input Handling</strong></summary>
  <p>Uses <code>try-except</code> to catch invalid (non-integer) inputs and applies <code>.strip()</code> to clean up extra whitespace before processing.</p>
</details>

<h3>📊 Approach Comparison</h3>
<ul>
  <li><strong>Basic Validation:</strong> Easier to read and quick to implement.</li>
  <li><strong>Robust Handling:</strong> More reliable, especially if the user might enter unexpected values.</li>
</ul>

<p>Choose the robust method if you want a more polished, error-proof application.</p>

