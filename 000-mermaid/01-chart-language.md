### **Objects and Tags in Mermaid Flowcharts**

In Mermaid, flowcharts are created using various objects represented by specific tags. Below are the basic elements and their corresponding tags for constructing flowcharts:

### 1. **Rectangle (Standard Process/Box)**
Represents a standard process or box.

```mermaid
graph td

    A[Standard Process]
```

- **Syntax**: `A[Text]`
- **Explanation**: By writing text inside square brackets `[ ]`, you create a rectangular process box.

### 2. **Rounded Rectangle (Sub-process)**
A rectangle with rounded corners.

```mermaid
B(Rounded Process)
```

- **Syntax**: `B(Text)`
- **Explanation**: Using parentheses `( )` around the text creates a rounded rectangle.

### 3. **Ellipse (Start/End)**
Generally represents start and end points.

```mermaid
C((Start/End))
```

- **Syntax**: `C((Text))`
- **Explanation**: Double parentheses `(( ))` are used to create an ellipse shape.

### 4. **Diamond (Decision Point)**
Represents decision points or conditional branching.

```mermaid
D{Decision}
```

- **Syntax**: `D{Text}`
- **Explanation**: Curly braces `{ }` are used to create a diamond shape.

### 5. **Circle**
Represents a node in a circular shape.

```mermaid
E(Circle Event)
```

- **Syntax**: `E((Text))`
- **Explanation**: Double parentheses `(( ))` are used to create a circle.

### 6. **Hexagon (Input/Output)**
Represents data input or output.

```mermaid
F{{Input/Output}}
```

- **Syntax**: `F{{Text}}`
- **Explanation**: Double curly braces `{{ }}` are used to create a hexagonal shape.

### 7. **Arrows for Connecting Elements**
Used to connect nodes in the diagram.

- **Straight Arrow**: `-->`
  Indicates a directional flow between two elements.
  
    ```mermaid
    A --> B
    ```

- **Dashed Arrow**: `-.->`
  Represents a dashed connection.

    ```mermaid
    A -.-> B
    ```

- **Bold Arrow**: `==>`
  Indicates a bold connection.

    ```mermaid
    A ==> B
    ```

### 8. **Directions**
You can specify the direction of the flowchart.

- **TD** (Top Down): Flows from top to bottom.
  
    ```mermaid
    graph TD
    ```

- **LR** (Left to Right): Flows from left to right.

    ```mermaid
    graph LR
    ```

- **BT** (Bottom to Top): Flows from bottom to top.

    ```mermaid
    graph BT
    ```

- **RL** (Right to Left): Flows from right to left.

    ```mermaid
    graph RL
    ```

### 9. **Labeled Arrows**
You can add labels to arrows, useful for showing conditions in decision points.

```mermaid
A -->|Yes| B
A -->|No| C
```

- `|Yes|`: Adds a label to the arrow.

### 10. **Subgraphs**
Used to divide the diagram into subgroups.

```mermaid
subgraph SubGroup1
    A --> B
end

subgraph SubGroup2
    C --> D
end
```

- **subgraph**: Starts a subgroup.
- **end**: Ends the subgroup.

### 11. **Cross Arrows (Link Routing)**
You can add text between arrows to describe connections.

```mermaid
A -- Description --> B
```

### 12. **Shape Styling**
You can style shapes to customize the appearance of elements.

```mermaid
classDef green fill:#9f6,stroke:#333,stroke-width:2px;
A --> B
B --> C
class A,B green
```

- **classDef**: Defines a class for styling.
- **fill**: Sets the background color.
- **stroke**: Sets the border color.
- **stroke-width**: Adjusts the border thickness.

### 13. **Loops**
You can represent loops or repeated actions by connecting the same elements.

```mermaid
A --> B
B --> A
```

### 14. **Notes**
You can add notes to diagrams for clarification.

```mermaid
A --> B
B --> C
C --> A
A ---|Note| B
```

Using these tags and elements, you can create flowcharts of any complexity with Mermaid.