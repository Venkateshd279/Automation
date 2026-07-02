# Prompt Engineering 
System Prompt Vs User Prompt 

- System prompt framework RTCFR (Role Task Context Fewshot Report/Response)

## RTCFR 

### Role 
Doctor, Nurse, Engineer, Architect like AI can do with 2 lakh professionals. 
Ex: You are an Doctor who is having 10 years of experience, Act as Engineer, You are an expert in AWS cloud. 

### Task 
- What work is going to do tell in the task. Assigning the work AI need to do. 
- Do: Explain what is AI agent and give me 3 real use case. You need clearly explain. 
- Don't: Tell me about AI

### Context 
- Giving the real background. 
- Without context AI guess, with context AI will give relavance answer. 
- Audience, purpose, situtation, tools, negative constrain. 

Ex: without context - create a email 
with context - Create an email template, for student with google form, the doubt sheet stored in google sheet and give in professional ticket you need to submit. 

### Fewshots 
- Fewshots means examples. 
- I need in Q&A format, give some example for Q&A. 
- How the output you wants? you need to provide the examples. 
-  style examples, output examples

### Responses 
- This is output response
1. Bullet points 
2. JSON
3. Check list  - with tick mark 
4. File create, pdf 
5. Markdown  .md 

- Normal prompt : Give me content 
- Response prompt: Give me 7 days of content with 1,2,3,4 

### Prompt tricks

- Prompt should not be straight forward and should not crystal clear.
- don't bring too much data in the prompt 
- keywords use: think, think a lot, think a more, ultra think 
- formating: It's importance. 

### Reverse prompting 
- Ask the AI to create the RTCFR framework. ex: write a give me the prompt in below format. 

### Prompt chaining 
- one prompt output another prompt input
- We can't get answer in single prompt for writing code. And reduce halucinate and improve reasoning. 
- breakdown of complex items.

#### prompting techniques

1. Sequential chaining
- One output goes another output

2. COT - Chain of Thoutgs 
- Key word: Think step by step 

3. TOT - Three of thoughts 
Generate multiple output and give me best output. 

4. REACT - Reasoning and Acting 
First do the reason and do act on it. 

5. Multi agent prompt
We give different prompts to different agent and it should communicate and work like that. 

### Advance prompt

Create a prompt example for the sequential prompting - Youtube script 
