# Timeline

## 1. **Gantt Chart**

Gantt charts are often used to represent timelines in project management. Here’s the list of Gantt chart components in Mermaid:

### Components for Gantt Charts:

- **Title**: Defines the title of the Gantt chart.
  ```
  gantt
    title Project Timeline
  ```
  
- **DateFormat**: Specifies the format of dates used in the chart (e.g., `YYYY-MM-DD`).
  ```
  dateFormat  YYYY-MM-DD
  ```

- **Section**: Groups tasks under a specific category or phase.
  ```
  section Phase 1
  ```

- **Tasks**: Define tasks or events with a start date and duration.
  - `Task name`: Describes the task.
  - `Start date`: The task's start date.
  - `Duration`: The number of days the task lasts.
  ```
  task1 :a1, 2024-10-01, 10d
  ```

- **Dependencies**: Represents dependencies between tasks using arrows.
  ```
  task2 :a2, after a1, 7d
  ```

### Example Gantt Chart (Timeline Representation):

```
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Design :a1, 2024-10-01, 10d
    Development :a2, after a1, 20d
    Testing :a3, after a2, 5d
    Deployment :a4, after a3, 3d
```

```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Design :a1, 2024-10-01, 10d
    Development :a2, after a1, 20d
    Testing :a3, after a2, 5d
    Deployment :a4, after a3, 3d
```

## 2. **Flowchart** for Timelines

Although Mermaid doesn't have a specific timeline component, you can create a simple flowchart to represent events or milestones on a timeline.

### Components for Flowcharts (adapted for a timeline)

- **Rectangles (Standard Steps)**: Use rectangles to represent events or milestones.
  ```
  A[Event 1]
  ```

- **Arrows (Time Progression)**: Use arrows to represent the flow of time.
  ```
  A --> B
  ```

- **Dates/Time Labels**: You can add time labels or other notes to arrows or nodes to indicate dates or periods.
  ```
  A -->|2024-10-01| B
  ```

### Example Flowchart (Timeline Representation)

```
graph LR
    A[Start] -->|2024-10-01| B[Event 1]
    B -->|2024-10-10| C[Event 2]
    C -->|2024-11-01| D[Event 3]
    D -->|2024-12-01| E[End]
```

```mermaid
graph LR
    A[Start] -->|2024-10-01| B[Event 1]
    B -->|2024-10-10| C[Event 2]
    C -->|2024-11-01| D[Event 3]
    D -->|2024-12-01| E[End]
```

## 3. **Sequence Diagrams for Timelines**

While not traditionally used for timelines, **sequence diagrams** could be adapted to represent a series of events over time by displaying interactions between objects or participants.

### Components for Sequence Diagrams

- **Participants**: Define entities involved in the timeline.
  ```
  participant Alice
  participant Bob
  ```

- **Messages/Interactions**: Represent the interaction or event happening at a certain time.
  ```
  Alice -> Bob: Event 1
  ```

### Example Sequence Diagram (Timeline Representation)

```
sequenceDiagram
    participant Time
    Time ->> Event1: 2024-10-01
    Time ->> Event2: 2024-10-10
    Time ->> Event3: 2024-11-01
    Time ->> End: 2024-12-01
```

```mermaid
sequenceDiagram
    participant Time
    Time ->> Event1: 2024-10-01
    Time ->> Event2: 2024-10-10
    Time ->> Event3: 2024-11-01
    Time ->> End: 2024-12-01
```

## Conclusion

While there isn't a dedicated "timeline" component in Mermaid, you can creatively use **Gantt charts**, **flowcharts**, or even **sequence diagrams** to represent timelines. Each of these components allows you to visually depict events over time in a structured way, depending on the complexity and type of timeline you wish to build.

## Sample

Here’s an example of a **Mermaid timeline** that illustrates a project timeline with various milestones:

```
timeline
    title Project Timeline
    2024-01-01 : Project Kickoff
    2024-02-15 : Requirement Gathering
    2024-03-30 : Design Phase Completed
    2024-04-15 : Development Phase Started
    2024-06-30 : First Prototype Released
    2024-07-15 : User Testing
    2024-08-01 : Final Adjustments
    2024-09-01 : Project Launch
```

```mermaid
timeline
    title Project Timeline
    2024-01-01 : Project Kickoff
    2024-02-15 : Requirement Gathering
    2024-03-30 : Design Phase Completed
    2024-04-15 : Development Phase Started
    2024-06-30 : First Prototype Released
    2024-07-15 : User Testing
    2024-08-01 : Final Adjustments
    2024-09-01 : Project Launch
```

### Explanation

- **Title**: The title of the timeline is "Project Timeline."
- **Dates**: Each line represents a milestone with a date followed by a description of the event.

This timeline provides a clear overview of the significant events and milestones in a project. You can customize the dates and events according to your specific needs.

![](./images/project-plan.png)

## Sample 2

```
gantt
    title Proje Planı
    dateFormat  YYYY-MM-DD
    section Tasarım
    Araştırma         :a1, 2024-10-01, 3d
    Planlama          :a2, after a1, 2d
    section Geliştirme
    Kodlama           :b1, 2024-10-04, 4d
    Test              :b2, after b1, 2d
```


```mermaid
gantt
    title Proje Planı
    dateFormat  YYYY-MM-DD
    section Tasarım
    Araştırma         :a1, 2024-10-01, 3d
    Planlama          :a2, after a1, 2d
    section Geliştirme
    Kodlama           :b1, 2024-10-04, 4d
    Test              :b2, after b1, 2d
```

![](./images/timeline.png)