# Why good commit messages are important, or in more sophisticated terms: gitgud
This repository contains a collection of guidelines and python scripts to build and maintain a cleaner git environment.

## The seven rules of a great Git commit message
This section deals with the topic of how to compose great git commit mesages. There are seven simple rules based on the insert name here.

To enable good teamwork, it is worth committing to a common set of rules. The problems often start to show when everyone writes git messages in their own style. Often, the messages can be so inane that you doubt you wrote them yourself. And if not even you know what you wanted to say, how should your colleague know? To avoid this, the following seven rules should be followed.
### 1. **Separate subject from body with a blank line**
First of all: Not every change needs a subject and a body. First of all: Not every change needs a subject and a body to describe it. In most cases a single line is sufficient. However, if the change is more far-reaching, you should consider writing a body. This speperation pays off when you browse through the git log.
### 2. **Limit the subject line to 50 characters**
The 50 character limit is not set in stone, but keeping subject lines shorth ensures that they are readable, and forces the author to think for a moment about the most concise way to explain what’s going on. Also it's a good indicator when too many changes have been made at once. If you need more than 50 characters, you should commit less. So shoot for 50 characters, but consider 72 as a hard limit.
### 3. **Capitalize the subject line**
Just start with a capital letter, like you would start any normal sentence.
### 4. **Do not end the subject line with a period**
The root of this rule is very simple in fact. Trailing punctuation is unnecessary in subject lines. Besides, space is precious when you’re trying to keep them to 50 chars or less.
### 5. **Use the imperative mood in the subject line**
Imperative mood just means “spoken or written as if giving a command or instruction”. A few examples:
* Clean your room
* Close the door
* Take out the trash

As you may have already noticed, each of the seven rules you’re reading about right now are written in the imperative (“Wrap the body at 72 characters”, etc.).

The imperative can sound a little rude; that’s why we don’t often use it. But it’s perfect for Git commit subject lines. One reason for this is that Git itself uses the imperative whenever it creates a commit on your behalf. Writing this way can be a little awkward at first. We’re more used to speaking in the indicative mood, which is all about reporting facts. That’s why commit messages often end up reading like this:
* ~~Fixed bug with X~~
* ~~Changing behavior of Y~~

And sometimes commit messages get written as a description of their contents:
* ~~More fixes for broken stuff~~
* ~~Sweet new API methods~~

To remove any confusion, this is a simple rule just to get it right every time. A properly formed Git commit subject line should always be able to complete the following sentence:

If applied, this commit will *your subject line here*
For example:
* If applied, this commit will **Refactor subsystem X for readability**
* If applied, this commit will **Update getting started documentation**
* If applied, this commit will **Remove deprecated methods**
* If applied, this commit will **Release version 1.0.0**
* If applied, this commit will **Merge pull request #123 from user/branch**
 
**Remember:** The use of the imperative is important only in the subject line. You can relax this restriction when you’re writing the body.

### 6. **Wrap the body at 72 characters**
Git never wraps text automatically. When you write the body of a commit message, you must mind its right margin, and wrap text manually.

The recommendation is to do this at 72 characters, so that Git has plenty of room to indent text while still keeping everything under 80 characters overall.

A good text editor can really help here. It’s easy to configure Vim, for example, to wrap text at 72 characters when you’re writing a Git commit. Traditionally, however, IDEs have been terrible at providing smart support for text wrapping in commit messages (although in recent versions, IntelliJ IDEA has finally gotten better about this).

### 7. **Use the body to explain what and why vs. how**
In most cases, you can leave out details about _**how**_ a change has been made. Code is generally self-explanatory in this regard (and if the code is so complex that it needs to be explained in prose, that’s what source comments are for). Just focus on making clear the reasons _**why**_ you made the change in the first place — the way things worked before the change (and what was wrong with that), the way they work now, and why you decided to solve it the way you did.

The future maintainer that will thank you may be yourself :)
