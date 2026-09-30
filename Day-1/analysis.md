# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

The private-data scenario used in this project is a student study assistant.

The private data contains the student's name, subject-wise progress, and pending study tasks. The subjects and their progress are stored in `student_data.json`.

The user request used for all three approaches is:

> "What should I study today?"

The same scenario is implemented using a plain chatbot, a rule-based workflow, and an AI agent.

---

## 2. Plain Chatbot

The plain chatbot is implemented in `chatbot.py`.

The chatbot mainly provides a response without directly accessing the student's private data. It does not read `student_data.json`, so it does not know the student's actual subject scores or pending tasks unless the user provides that information.

The chatbot does not require any external tool or predefined decision-making rules in this implementation. It simply responds to the user's request and asks the user to provide their subject names and progress.

The main limitation is that it cannot automatically use the student's private data. Therefore, its response is general rather than personalized to the student's actual progress.

For example, when the user asks, "What should I study today?", the chatbot asks the user to provide their subject names and current progress.

---

## 3. Rule-Based Workflow

The rule-based workflow is implemented in `rule_based_workflow.py`.

This approach reads the student's private information from `student_data.json`. It does not use an LLM. Instead, it uses predefined programming rules.

The main rule used is:

```text
If a subject's marks are below 50, identify that subject as a priority.
```

The workflow reads each subject and its marks. It checks the predefined condition and adds subjects below 50 to the priority list.

In this scenario, Java has a score of 45 and DSA has a score of 35. Therefore, the workflow recommends Java and DSA.

The main limitation is flexibility. The workflow can only make decisions that have been explicitly programmed. If the requirements change, the rules in the program must also be changed.

---

## 4. AI Agent

The AI agent is implemented in `agent.py`.

The agent demonstrates the main idea of an AI agent using a tool and an agent-style process. The tool `read_student_data()` reads the student's private data from `student_data.json`.

The process starts when the user enters a request. The agent identifies that it needs the student's private study data and uses the data-reading tool. It then observes the retrieved information and determines which subjects require attention.

The agent then produces a final recommendation based on the retrieved information.

The important concept demonstrated here is that an AI agent can combine an LLM, tools, and a loop to work through a task. In this simplified implementation, the tool is the function that reads the private data.

Compared with the plain chatbot, the agent can access the private data through a tool. Compared with a purely rule-based workflow, an agent can be extended with additional tools and more flexible decision-making.

A limitation of this project is that the implementation is a simplified local demonstration. It does not connect to a real external LLM API. Therefore, the agent structure demonstrates the tool-using process rather than a production-level autonomous AI agent.

---

## 5. Comparison Table

| Basis for comparison     | Plain chatbot                                                              | Rule-based workflow                          | AI agent                                                              |
| ------------------------ | -------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------- |
| Flexibility              | Can respond to general user questions but does not access the private file | Limited to predefined rules                  | Can be extended with tools and more flexible decision-making          |
| Decision-making          | Provides a response based on the available conversation                    | Uses fixed `if/else` conditions              | Uses an agent-style process to decide what information/tool is needed |
| Tool usage               | No tool                                                                    | Uses file access through normal program code | Uses `read_student_data()` as a tool                                  |
| Private-data access      | Does not directly access the private file                                  | Reads `student_data.json`                    | Accesses `student_data.json` through its tool                         |
| Multi-step task handling | Limited                                                                    | Follows predefined program steps             | Can perform multiple tool and reasoning steps                         |
| Automation               | Low for this scenario because the user must provide the data               | High for the programmed rule                 | Higher potential because tools can be added and selected as needed    |
| Reliability              | Depends on the information provided by the user                            | Consistent for the programmed conditions     | Depends on the quality of the agent's reasoning and tools             |

---

## 6. Suitability Analysis

For this particular student study-data scenario, the AI agent approach is the most suitable when the system needs to grow beyond the simple rule used in this project.

The plain chatbot is useful when the student wants general study guidance and is willing to provide the required information. It is simple, but it cannot automatically access the student's private data in this implementation.

The rule-based workflow is useful when the decision is simple and predictable. For example, the rule "if marks are below 50, recommend the subject" is easy to implement and produces consistent results. However, every new type of decision needs to be programmed as a new rule.

The AI agent provides more flexibility because it can be extended with additional tools. For example, a larger version could use tools for reading study data, checking pending tasks, creating a study plan, and updating the student's progress.

Therefore, for a simple fixed condition, the rule-based workflow is sufficient. For a more complex study assistant that needs multiple tools and multi-step actions, the AI agent provides a more suitable architecture.

---

## 7. Conclusion

A plain chatbot, a rule-based workflow, and an AI agent solve problems in different ways.

A plain chatbot is appropriate when the main requirement is conversational interaction and the system does not need to perform complex actions or access private data directly.

A rule-based workflow is appropriate when the problem has clear, predictable conditions and the required decisions can be represented using predefined rules. It is useful when consistent and deterministic behavior is important.

An AI agent is appropriate for tasks that require multiple steps, tool usage, access to relevant data, and more flexible decision-making. An agent can use tools, observe their results, and continue working toward completing a task.

The main difference demonstrated in this project is that the plain chatbot mainly provides responses, the rule-based workflow follows predefined conditions, and the AI agent combines an agent-style decision process with tools and iterative task handling.
