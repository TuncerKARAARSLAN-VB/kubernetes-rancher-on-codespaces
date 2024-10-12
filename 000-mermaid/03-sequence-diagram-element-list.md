# Sequence Diagram Elements

## 1. **Participants**

- Represents the actors or objects in the sequence diagram.
- Syntax: `participant Name`
   
   ```mermaid
   participant Alice
   participant Bob
   ```

## 2. **Messages**

- Used to show the flow of messages or actions between participants.
- **Solid Arrow**: `->` for regular messages.
- **Dashed Arrow**: `-->` for asynchronous messages.
   
   ```mermaid
   Alice -> Bob: Hello
   Bob --> Alice: Hi back
   ```

## 3. **Activation (Lifeline)**

- Indicates when an object is active during the sequence.
- Syntax: `activate Name` and `deactivate Name`

   ```mermaid
   Alice -> Bob: Activate Bob
   activate Bob
   Bob -> Alice: Response
   deactivate Bob
   ```

## 4. **Loops**

- Represents repeating messages or actions.
- Syntax: `loop Description ... end`
   
   ```mermaid
   loop Check every second
     Alice -> Bob: Ping
   end
   ```

## 5. **Alt/Else Blocks (Conditional Branching)**

- For decisions and alternate paths.
- Syntax: `alt Condition ... else ... end`
   
   ```mermaid
   alt Successful
     Alice -> Bob: OK
   else Failed
     Alice -> Bob: Retry
   end
   ```

### 6. **Parallel (Concurrency)**

- Represents concurrent processes.
- Syntax: `par ... and ... end`
   
   ```mermaid
   par Task 1
     Alice -> Bob: Start task 1
   and Task 2
     Alice -> Charlie: Start task 2
   end
   ```

### 7. **Notes**

- You can add notes for clarification or comments.
- Syntax: `Note left of Name: text` or `Note right of Name: text`
   
   ```mermaid
   Note right of Bob: Thinking...
   ```

### 8. **Message to Self**

- Represents a message that a participant sends to themselves.
- Syntax: `Name ->> Name: Action`
   
   ```mermaid
   Alice ->> Alice: Reflecting
   ```

### 9. **Break**

- Used to indicate an interruption in the flow.
- Syntax: `break Description ... end`
   
   ```mermaid
   break System error
     Alice -> Bob: Error message
   end
   ```

### 10. **Critical**

- Shows critical sections.
- Syntax: `critical Description ... end`
   
   ```mermaid
   critical Critical operation
     Alice -> Bob: Do something critical
   end
   ```

### 11. **Rect**

- Groups actions together for emphasis.
- Syntax: `rect color`
   
   ```mermaid
   rect rgb(191, 223, 255)
     Alice -> Bob: Grouped action
   end
   ```

### 12. **Opt (Optional Section)**

- For optional steps.
- Syntax: `opt Description ... end`
   
   ```mermaid
   opt Optional step
     Alice -> Bob: Can skip this
   end
   ```

These components help you build complex and detailed **sequence diagrams** using Mermaid syntax.