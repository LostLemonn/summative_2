# Hitachi Rail Safety Quiz 🚄

## Introduction
As a business operating on *critical national infrastructure*, safety is at the forefront of our principles. Hence, I have designed and developed a brief safety related quiz that serves as a **MVP**, and would hopefully help in increasing awareness of safety practices and knowledge overall within the organisation. Essentially, it's been created with the mindset that anyone should be able to go through it, whether that be using it as a tool for induction of new employees, or perhaps as a refresher for existing staff, or perhaps even just as a baseline resource for managers to review their team. Currently, there is no standardised way to check whether staff have a working knowledge of key safety topics - this application exists to bridge that gap.

Built using [Python](https://docs.python.org/3/) for the backbone and [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI, my app works initially by prompting participants to enter their name, followed by asking 5 multiple choice questions on topics such as PPE, fire procedures and UK legislation.

One of the cool things about the app is the validation rules/checks. If something goes against the rules *(e.g. entering numerical values in name box)* and the user attempts to submit, an [error](docs_assets/error_message.png) message will pop up - the user is unable to proceed until this is fixed. Once a submission is made, the name, answers, and a timestamp all get written to a [CSV file](https://docs.python.org/3/library/csv.html) that can be viewed conveniently, using standard software like [MS Excel](https://www.microsoft.com/en-gb/microsoft-365/excel), making the process of analysing the data quite easy and accessible!

Naturally as a MVP, comprehensive features are out of scope; this app only presents the bare minimum to users at its current stage, allowing for plenty of room for improvement in the future😊

Let's move on to the <ins>**exciting**</ins> bits now⬇️

## Design

### GUI Design
![Figure 1: Wireframe](docs_assets/wireframe.png)
**Figure 1:** Wireframe

Through **Figure 1** we can see the very early wireframe during the design stage of my application, prior to any code being written. Using the design platform [Figma](https://www.figma.com/), I was able to build and visualise an idea of how I wanted the user journey to look like, both successful and unsuccessful (error message). Frame 2 (bottom left) shows the app in an error state which would activate if the user goes against any validation rules, whereas Frame 3 (bottom right) conveys a successful submission, exemplified by the green font! Visually, you'll notice it's quite a far fetch from the final application, but the wireframe was not used to focus on visual presentation, rather just the journey of a user and screen layouts. Laying these foundations is much more important than emphasising presentation. Although, one visual aspect I did want to identify at this stage was the focus on using the brand colour scheme so users would know that this is an official communication. As we see in **Figure 1**, I used a red background to highlight the primary colour of the company. Once it came to actually coding the GUI however, I realised that this was simply too much red and wasn't very pleasing to the eye after a few minutes, so red was turned into an accent colour instead, still reflecting the brand identity.

[View Figma Wireframe](https://www.figma.com/design/RHAnN1kOKP6Ibnj0Q6p2F0/Hitachi-Rail-Quiz-Design?node-id=0-1&t=OpVAHXUjfVeYXzuA-1)

### Functional & Non-Functional Requirements

#### Functional Requirements

| ID  | Requirement |
|-----|-------------|
| FR1 | The application must write the name, answers and timestamp to a CSV file. |
| FR2 | The application must validate the name before submission. |
| FR3 | The application must allow a user to enter a name. |
| FR4 | The application must display a confirmation screen after a successful submission. |
| FR5 | The application must display 5 Multiple Choice Questions. |

#### Non-Functional Requirements

| ID  | Requirement |
|-----|-------------|
| NFR1 | The application should follow Hitachi branding. |
| NFR2 | The application should be easy on the eyes when viewing for a long period. |
| NFR3 | The application should convey why an error has occured within the message. |
| NFR4 | The application should implement accessibilty features e.g. speech reader. |
| NFR5 | Stored data should be readable using standard software e.g. MS Excel. |

### Tech Stack
- [Python 3](https://docs.python.org/3/) — core programming language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — desktop graphical user interface
- [csv](https://docs.python.org/3/library/csv.html) — local data storage in CSV format
- [re](https://docs.python.org/3/library/re.html) — regular expressions for input validation, ensures that the name does not contain any numerical values
- [datetime](https://docs.python.org/3/library/datetime.html) — timestamp generation to then use for csv log
- [unittest](https://docs.python.org/3/library/unittest.html) — automated unit testing for testing parts of the app before it's fully complete

### Code Design
![Figure 2: Class Diagram](docs_assets/class_diagram.png)

## Development



## Testing





## Documentation

### User

### Technical




## Evaluation
