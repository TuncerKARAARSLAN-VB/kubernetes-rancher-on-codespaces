# Sequence Diagram Elements

## 1. **Participants**

- Represents the actors or objects in the sequence diagram.
- Syntax: `participant Name`
   
   ```
   participant Alice
   participant Bob
   ```

## 2. **Messages**

- Used to show the flow of messages or actions between participants.
- **Solid Arrow**: `->` for regular messages.
- **Dashed Arrow**: `-->` for asynchronous messages.
   
   ```
   Alice -> Bob: Hello
   Bob --> Alice: Hi back
   ```

## 3. **Activation (Lifeline)**

- Indicates when an object is active during the sequence.
- Syntax: `activate Name` and `deactivate Name`

   ```
   Alice -> Bob: Activate Bob
   activate Bob
   Bob -> Alice: Response
   deactivate Bob
   ```

## 4. **Loops**

- Represents repeating messages or actions.
- Syntax: `loop Description ... end`
   
   ```
   loop Check every second
     Alice -> Bob: Ping
   end
   ```

## 5. **Alt/Else Blocks (Conditional Branching)**

- For decisions and alternate paths.
- Syntax: `alt Condition ... else ... end`
   
   ```
   alt Successful
     Alice -> Bob: OK
   else Failed
     Alice -> Bob: Retry
   end
   ```

### 6. **Parallel (Concurrency)**

- Represents concurrent processes.
- Syntax: `par ... and ... end`
   
   ```
   par Task 1
     Alice -> Bob: Start task 1
   and Task 2
     Alice -> Charlie: Start task 2
   end
   ```

### 7. **Notes**

- You can add notes for clarification or comments.
- Syntax: `Note left of Name: text` or `Note right of Name: text`
   
   ```
   Note right of Bob: Thinking...
   ```

### 8. **Message to Self**

- Represents a message that a participant sends to themselves.
- Syntax: `Name ->> Name: Action`
   
   ```
   Alice ->> Alice: Reflecting
   ```

### 9. **Break**

- Used to indicate an interruption in the flow.
- Syntax: `break Description ... end`
   
   ```
   break System error
     Alice -> Bob: Error message
   end
   ```

### 10. **Critical**

- Shows critical sections.
- Syntax: `critical Description ... end`
   
   ```
   critical Critical operation
     Alice -> Bob: Do something critical
   end
   ```

### 11. **Rect**

- Groups actions together for emphasis.
- Syntax: `rect color`
   
   ```
   rect rgb(191, 223, 255)
     Alice -> Bob: Grouped action
   end
   ```

### 12. **Opt (Optional Section)**

- For optional steps.
- Syntax: `opt Description ... end`
   
   ```
   opt Optional step
     Alice -> Bob: Can skip this
   end
   ```

## Sample

```
sequenceDiagram
    participant User
    participant System

    User->>System: Request Login
    System->>User: Display Login Form
    User->>System: Submit Credentials
    System->>System: Validate Credentials
    alt Successful Login
        System->>User: Display Dashboard
    else Failed Login
        System->>User: Display Error Message
    end
```

```mermaid
sequenceDiagram
    participant User
    participant System

    User->>System: Request Login
    System->>User: Display Login Form
    User->>System: Submit Credentials
    System->>System: Validate Credentials
    alt Successful Login
        System->>User: Display Dashboard
    else Failed Login
        System->>User: Display Error Message
    end
```

### Explanation

- **Participants**: There are two participants, `User` and `System`.
- **Arrows**: The arrows indicate the messages being sent between the user and the system.
- **alt/else**: The `alt` block shows an alternative flow depending on whether the login is successful or failed.

![](./images/sequence-diagram.png)