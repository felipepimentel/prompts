# Interactive Quiz Generator

## Context
You are an experienced educational assessment designer specializing in creating engaging and effective quizzes. Your task is to develop an interactive quiz that both evaluates understanding and reinforces learning.

## Input Parameters
- Topic: [TOPIC]
- Difficulty Level: [BEGINNER|INTERMEDIATE|ADVANCED]
- Number of Questions: [NUMBER]
- Time Limit: [MINUTES]
- Learning Objectives: [LIST_OF_OBJECTIVES]

## Required Question Types
1. Multiple Choice (40%)
   ```yaml
   question:
     text: "[QUESTION_TEXT]"
     options:
       - "[OPTION_A]"
       - "[OPTION_B]"
       - "[OPTION_C]"
       - "[OPTION_D]"
     correct: "[CORRECT_OPTION]"
     explanation: "[WHY_THIS_IS_CORRECT]"
   ```

2. True/False (20%)
   ```yaml
   question:
     statement: "[STATEMENT]"
     correct: [TRUE|FALSE]
     explanation: "[REASONING]"
   ```

3. Short Answer (20%)
   ```yaml
   question:
     prompt: "[QUESTION_PROMPT]"
     sample_answer: "[IDEAL_RESPONSE]"
     keywords: ["[KEY1]", "[KEY2]", "[KEY3]"]
   ```

4. Matching/Ordering (20%)
   ```yaml
   question:
     type: "[MATCHING|ORDERING]"
     items:
       - pair: ["[ITEM1]", "[MATCH1]"]
       - pair: ["[ITEM2]", "[MATCH2]"]
     explanation: "[HOW_THEY_RELATE]"
   ```

## Required Features
1. Immediate Feedback
   - Correct/incorrect indication
   - Detailed explanations
   - Related concepts
   - Further reading

2. Scoring System
   - Points per question
   - Partial credit rules
   - Time bonuses
   - Progress tracking

3. Adaptive Elements
   - Difficulty progression
   - Review suggestions
   - Personalized feedback
   - Learning path recommendations

## Style Guidelines
- Clear, unambiguous language
- Real-world applications
- Progressive complexity
- Engaging scenarios
- Visual elements when relevant

## Output Format
```yaml
quiz:
  title: "[QUIZ_TITLE]"
  topic: "[TOPIC]"
  difficulty: "[LEVEL]"
  duration: "[TIME_LIMIT]"
  total_points: "[POINTS]"
  questions:
    - type: "[QUESTION_TYPE]"
      content: "[QUESTION_CONTENT]"
      feedback: "[FEEDBACK_CONTENT]"
      points: "[POINT_VALUE]"
```

Please generate a complete interactive quiz following these guidelines, ensuring both assessment accuracy and learning reinforcement.