# owlsay

`owlsay` is a tiny Python terminal toy inspired by `cowsay`, but wiser, moodier, and slightly unhinged.
It prints an ASCII owl that speaks your message — with hidden easter eggs and secret modes 🥚.

"A minimalist cowsay-style terminal toy written in Python — featuring a wise ASCII owl, speech bubbles, secret mood flags, and easter eggs."

---

## Features

* ASCII owl with speech bubble
* Automatic text wrapping
* Multiple secret owl moods (eyes + messages)
* Fly-away mode
* Accepts arguments **or** piped input
* Zero dependencies (Python standard library only)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/owlsay.git
cd owlsay
```

(Optional) Make it executable:

```bash
chmod +x owlsay.py
```

---

## Usage

Basic usage:

```bash
python3 owlsay.py "Hoot hoot!"
```

Pipe text:

```bash
echo "Night shift again..." | python3 owlsay.py
```

---

## 🥚 Easter Eggs & Modes

Modes are triggered by passing the flag **as the message itself**
(intentionally *not* traditional CLI flags).

|   Flag | Mode     | Eyes    | Description          |
| -----: | -------- | ------- | -------------------- |
| `-man` | Manual   | 👀      | Show built-in manual |
|   `-g` | Greed    | `$ $`   | Capitalist owl       |
|   `-b` | Borg     | `==`    | Resistance is futile |
|   `-d` | Dead     | `X X`   | The owl is done      |
|   `-t` | Tired    | `- -`   | Needs coffee         |
|   `-s` | Stoned   | `* *`   | Everything is vibes  |
|   `-p` | Paranoid | `@ @`   | They’re watching     |
|   `-c` | Confused | `? ?`   | What is reality      |
|   `-l` | Love     | `<3 <3` | Pure hoot energy     |
|   `-f` | Fly away | —       | Owl leaves entirely  |

Examples:

```bash
python3 owlsay.py -t
python3 owlsay.py -s
python3 owlsay.py -p
python3 owlsay.py -f
python3 owlsay.py -man
```

---

## Design Philosophy

* Flags are **hidden messages**, not CLI options
* One mode at a time
* Sensible defaults
* Unix humor over correctness

---

## Requirements

* Python **3.8+**
* No external libraries

---

## License

MIT License.
Do whatever you want.
If the owl judges you, that’s on you.

---

🦉 *The owl knows things.*
