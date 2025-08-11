<h1>🔐 Password Retry System</h1>

<h2>📝 Project Task:</h2>

<p>The program should:</p>
<ul>
  <li>Prompt the user to enter a password.</li>
  <li>Allow <strong>up to 3 tries</strong> using a <code>while</code> loop.</li>
  <li>If the user enters the correct password (<code>"python123"</code>) within 3 attempts, display:
    <pre><code>Access granted.</code></pre>
  </li>
  <li>If the entered password is incorrect, display:
    <pre><code>Incorrect password. Try again.</code></pre>
  </li>
  <li>If the user fails all 3 attempts, display:
    <pre><code>Too many attempts. You are locked out.</code></pre>
  </li>
</ul>

<h2>💡 Notes</h2>
<ul>
  <li>The correct password is hardcoded as <strong><code>python123</code></strong> for this exercise.</li>
  <li>This program is for learning purposes only and should not be used for real authentication systems.</li>
</ul>

<h2>💻 Example Solutions</h2>

<details>
  <summary><strong>Approach 1 – While Loop with Early Exit</strong></summary>
  <p>This method uses a <code>while</code> loop and stops execution immediately when the correct password is entered using <code>break</code>.</p>
</details>

<details>
  <summary><strong>Approach 2 – For Loop with Else Block</strong></summary>
  <p>This version uses a <code>for</code> loop with an <code>else</code> clause, which only runs if the loop completes all attempts without hitting a <code>break</code>.</p>
</details>

<h3>📊 Side-by-Side Overview</h3>
<ul>
  <li><strong>While Loop Method:</strong> More step-by-step control, good for customizing the flow.</li>
  <li><strong>For Loop Method:</strong> Shorter and makes use of Python’s loop–else feature.</li>
</ul>

<p>Both styles are correct — test them and see which feels more natural for you!</p>
