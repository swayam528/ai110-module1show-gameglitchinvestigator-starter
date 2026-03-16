# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The enter button didn't work to submit the guess. I expected that pressing enter would submit my guess, but it didn't do that.
The new game button doesn't work. I expected that clicking new game button would start a new game, but when attempting to start a new guess for the new game nothing happens or gets populated to the history.
The hints were backwards. Pretty self explanatory: the hints were the opposite of what was actually true.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot in chat and inline-editing style to fix buggy game logic, suggest refactors, and generate test ideas.

 One correct AI suggestion was to move shared logic like `check_guess` out of `app.py` into `logic_utils.py` so the UI and tests could use one source of truth. I verified that suggestion by running `pytest` after the refactor and checking that the Streamlit app still imported and used the same helper functions.

 One misleading AI path was stopping after only fixing the high/low comparison, because the app still had state bugs like alternating secret types and incomplete reset behavior. I caught that by reading the rest of the code carefully.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated a bug as fixed only after both the code path and the game behavior matched what I expected. For example, I did not stop after changing the hint text because I also checked whether the app was still mutating state in a way that could make the comparison fail again on later turns. I ran `pytest` to verify the guessing logic, including a case for a string secret value, and I also used `python -m streamlit run app.py` to confirm the game loaded without crashing. AI helped by suggesting what to test around `check_guess`, but I still had to review whether the tests matched the actual return value of the function.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the script each time someone interacts with a widget, so local variables are not enough to preserve game progress. Session state is what lets the app remember values like the secret number, score, attempts, and history between reruns. I would explain it to a friend by saying that every click redraws the app, and session state is the backpack that carries the important values from one redraw to the next.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is isolating the logic from the UI first, because that made the bugs easier to reason about and easier to test. Next time I work with AI on a coding task, I would narrow each prompt to one bug at a time even earlier so I can review each proposed change more critically. This project changed the way I think about AI-generated code because I saw that a suggestion can be partially right while still missing the larger problem. AI is useful for speed, but it still needs a human to check behavior, state management, and test coverage.
