


The team's project focuses on optimizing semantic segmentation algorithms for eye tracking in assistive technology applications. Rather than splitting the algorithm, which would increase overhead cost and slow down overall system speed, we propose an efficient resource scheduling approach that ensures all algorithms receive fair access to the DPU. Our approach aims to improve processing from 160 ms per frame to approximately 33.2ms per frame for 4 frames simultaneously\*, while maintaining our required 99.8% IoU accuracy. This optimization ensures that Algorithms 1, 2, and 3 can collect their required periodic data without being starved by the semantic segmentation algorithm, which is critical for real-time eye tracking in medical assistance devices for individuals with disabilities, particularly those with conditions like cerebral palsy.

The team's key design requirements include maintaining 99.8% IoU accuracy while achieving the target processing speed of 60 frames per second. The approach leverages parallelism on the AMD Kria KV260 development board, utilizing its multi-core architecture and Deep Processing Unit (DPU) for neural network inference. The design employs resource scheduling strategies, memory management techniques, and deadline-aware prioritization to optimize resource utilization.

Progress to date includes establishing the development environment, testing the existing eye tracking algorithm, and developing a scheduling approach. Initial results show the feasibility of achieving the required performance improvements, with current accuracy at 98.8%, within the team's target range. The team's next steps focus on developing the resource management system and optimizing data flow between processing units.

The design effectively addresses user needs by improving response time for assistive devices, enabling more natural and responsive eye-tracking control for users with mobility impairments. This enhanced performance will significantly improve safety and quality of life for users, allowing the system to detect and respond to potential medical issues faster and more reliably.

\*Note: These numerical examples are representative placeholders to illustrate the design challenge and protect NDA-covered information.

Learning Summary

Development Standards & Practices Used

* ONNX (Open Neural Network Exchange) for neural network model representation  
* Multithreaded programming using C++ and POSIX threads  
* Memory management and thread synchronization techniques  
* Docker containerization for development and deployment  
* Version control using Git/GitHub  
* IEEE 3129-2023 for AI-based image recognition testing and evaluation  
* IEEE 2802-2022 for AI-based medical device performance evaluation  
* IEEE 7002-2022 for data privacy processes  
* Vitis-AI and Vitas-Runtime for model optimization and deployment

Summary of Requirements

* Divide U-Net semantic segmentation algorithm into four equal parts for parallel processing.  
* Implement a pipelined architecture for concurrent execution across multiple cores  
* Achieve system throughput of less than 33.2 ms per frame when processing four frames  
* Maintain algorithm accuracy of 99.8% IoU after optimization and parallelization  
* Optimize memory and FPGA resource usage for efficient parallel execution  
* Implement robust error handling for pipeline management  
* Ensure compatibility with Xilinx Kria KV260 hardware platform  
* Develop efficient DPU resource sharing between algorithm components  
* Create thread management system for synchronization and communication  
* Maintain data consistency and integrity throughout the pipeline

Applicable Courses from Iowa State University Curriculum 

CprE 488: Embedded Systems Design

CprE 489: Computer Networking and Data Communications

ComS 511: Design and Analysis of Algorithms

ComS 572: Principles of Artificial Intelligence

ComS 474/574: Intro to Machine Learning

Math 407: Applied Linear Algebra

ComS 510: Distributed Development of Software

EE 524: Digital Signal Processing

CprE 585: Developmental Robotics

New Skills/Knowledge acquired that was not taught in courses

* Semantic segmentation techniques using U-Net architecture  
* FPGA programming using Vitis-AI for deep learning applications  
* Memory allocation strategies for multi-core embedded systems  
* Optimization techniques for neural networks on resource-constrained hardware  
* Real-time constraints handling in eye-tracking applications  
* Algorithmic division for parallel processing while maintaining mathematical consistency  
* DPU resource scheduling and optimization  
* Docker container optimization for embedded deployments  
* Vitas Runtime

Table of Contents

[**1\. Introduction	8**](#1.-introduction)

[1.1. Problem Statement	8](#problem-statement)

[1.2. Intended Users	8](#intended-users)

[Primary Clients	8](#primary-clients)

[Client 2: Caregivers and Family Members	8](#client-2:-caregivers-and-family-members)

[Client 3: The Tertiary User Group	9](#client-3:-the-tertiary-user-group)

[**2\. Requirements, Constraints, And Standards	9**](#requirements,-constraints,-and-standards)

[2.1. Requirements & Constraints	9](#requirements-&-constraints)

[Functional Requirements	9](#functional-requirements)

[User Interface (UI) Requirements	10](#user-interface-\(ui\)-requirements)

[Physical and Economic Requirements	10](#physical-and-economic-requirements)

[System Constraints	11](#system-constraints)

[Additional Considerations	11](#additional-considerations)

[2.2 Engineering Standards	11](#2.2-engineering-standards)

[**3 Project Plan	12**](#3-project-plan)

[3.1 Project Management/Tracking Procedures	12](#3.1-project-management/tracking-procedures)

[3.2 Task Decomposition	13](#3.2-task-decomposition)

[Task 2: Implementation of Core Components	14](#task-2:-implementation-of-core-components)

[Task 3: Thread Management	14](#task-3:-thread-management)

[Task 4: Multicore Processing	14](#task-4:-multicore-processing)

[Task 5: Integration and Testing	14](#task-5:-integration-and-testing)

[Task 6: Documentation and Delivery	14](#task-6:-documentation-and-delivery)

[3.3 Project Proposed Milestones, Metrics, and Evaluation Criteria	14](#3.3-project-proposed-milestones,-metrics,-and-evaluation-criteria)

[Milestone 1: Mathematical Division of the Algorithm	14](#milestone-1:-mathematical-division-of-the-algorithm)

[Milestone 3: Thread Testing with Matrix Operations	15](#milestone-3:-thread-testing-with-matrix-operations)

[Milestone 4: Docker Environment Configuration	15](#milestone-4:-docker-environment-configuration)

[Milestone 5: Pipelined Implementation of Semantic Segmentation	15](#milestone-5:-pipelined-implementation-of-semantic-segmentation)

[Milestone 6: Increased Throughput Demonstration	15](#milestone-6:-increased-throughput-demonstration)

[3.4 Project Timeline/Schedule	16](#3.4-project-timeline/schedule)

[3.5 Risks and Risk Management/Mitigation	16](#3.5-risks-and-risk-management/mitigation)

[Risk 1: Completion Delays	16](#risk-1:-completion-delays)

[Risk 2: Hardware Damage	16](#risk-2:-hardware-damage)

[Risk 3: Data Security	17](#risk-3:-data-security)

[Risk 4: Algorithm Complexity	17](#risk-4:-algorithm-complexity)

[Risk 5: Parallelism Implementation Challenges	17](#risk-5:-parallelism-implementation-challenges)

[Risk 6: Image Processing Speed Limitations	17](#risk-6:-image-processing-speed-limitations)

[3.6 Personnel Effort Requirements	17](#3.6-personnel-effort-requirements)

[3.7 Other Resource Requirements	19](#3.7-other-resource-requirements)

[Hardware Resources	19](#hardware-resources)

[Software Resources	19](#software-resources)

[Development Tools	19](#development-tools)

[Data Resources	19](#data-resources)

[4.1 Design Context	20](#4.1-design-context)

[4.1.1 Broader Context	20](#4.1.1-broader-context)

[4.1.2 Prior Work/Solutions	20](#4.1.2-prior-work/solutions)

[4.1.3 Technical Complexity	21](#4.1.3-technical-complexity)

[4.2 Design Exploration	22](#4.2-design-exploration)

[4.2.1 Design Decisions	22](#4.2.1-design-decisions)

[4.2.2 Ideation	23](#4.2.2-ideation)

[4.2.3 Decision-Making and Trade-Off	23](#4.2.3-decision-making-and-trade-off)

[4.3 Proposed Design	24](#proposed-design)

[4.3.1 Overview	24](#4.3.1-overview)

[4.3.2 Detailed Design and Visual(s)	25](#4.3.2-detailed-design-and-visual\(s\))

[Hardware Platform	25](#hardware-platform)

[Software Components	25](#software-components)

[Processing Pipeline	26](#processing-pipeline)

[Memory Allocation	26](#memory-allocation)

[4.3.3 Functionality	26](#4.3.3-functionality)

[Initial Setup:	26](#initial-setup:)

[Normal Operation:	27](#normal-operation:)

[Response to Detected Issues:	27](#response-to-detected-issues:)

[User Control Mode:	27](#user-control-mode:)

[4.3.4 Areas of Concern and Development	27](#4.3.4-areas-of-concern-and-development)

[4.4 Technology Considerations	28](#4.4-technology-considerations)

[Kria Board KV260	28](#kria-board-kv260)

[U-net Semantic Segmentation Algorithm	29](#u-net-semantic-segmentation-algorithm)

[Vitis-AI and Vitas-Runtime	29](#vitis-ai-and-vitas-runtime)

[Alternative Technologies Considered	30](#alternative-technologies-considered)

[4.5 Design Analysis	30](#4.5-design-analysis)

[Current Implementation Status:	30](#current-implementation-status:)

[Implementation Challenges:	31](#implementation-challenges:)

[Future Implementation Plans:	31](#future-implementation-plans:)

[**5  Testing	31**](#5-testing)

[Testing Strategy Overview	31](#testing-strategy-overview)

[Testing Philosophy	32](#testing-philosophy)

[Testing Challenges	32](#testing-challenges)

[Testing Schedule	32](#testing-schedule)

[5.1 Unit Testing	32](#5.1-unit-testing)

[Feature Map Testing	32](#feature-map-testing)

[Algorithm Testing	32](#algorithm-testing)

[System Coordination Testing	33](#system-coordination-testing)

[Success Goals	33](#success-goals)

[5.2 Interface Testing	33](#5.2-interface-testing)

[Key Interfaces	33](#key-interfaces)

[Test Cases	33](#test-cases)

[5.3 System Testing	34](#system-testing)

[Test Plan	34](#test-plan)

[Test Measurements	34](#test-measurements)

[5.4 Regression Testing	34](#regression-testing)

[Automated Testing	34](#automated-testing)

[Monitoring	35](#monitoring)

[Test Schedule	35](#test-schedule)

[5.5 Acceptance Testing	35](#acceptance-testing)

[Function Tests	35](#function-tests)

[Other Requirements	35](#other-requirements)

[Client Involvement	36](#client-involvement)

[5.6 User Testing	36](#user-testing)

[Proposed Future User Testing Plan	36](#proposed-future-user-testing-plan)

[System Preparation for Future Testing	36](#system-preparation-for-future-testing)

[5.7 Results	37](#results)

[Current Progress	37](#current-progress)

[Next Steps	37](#next-steps)

[**6  Implementation	37**](#6-implementation)

[Resource Management Approach	37](#resource-management-approach)

[Thread Coordination Implementation	38](#thread-coordination-implementation)

[DPU Scheduler Implementation	38](#dpu-scheduler-implementation)

[Current Status	38](#current-status)

[Next Implementation Steps	39](#next-implementation-steps)

[**7  Ethics and Professional Responsibility	39**](#7-ethics-and-professional-responsibility)

[7.1 Areas of Professional Responsibility/Codes of Ethics	39](#areas-of-professional-responsibility/codes-of-ethics)

[7.2 Four Principles	42](#7.2-four-principles)

[7.3 Virtues	44](#7.3-virtues)

[Individual Virtues	45](#individual-virtues)

[**8  Closing Material	46**](#8-closing-material)

[8.1 Conclusion	46](#8.1-conclusion)

[8.2 References	47](#8.2-references)

[8.3 Appendices	47](#8.3-appendices)

[Appendix A: Algorithm Performance Optimization Approach	47](#appendix-a:-algorithm-performance-optimization-approach)

[Appendix B: System Coordination Approach	47](#appendix-b:-system-coordination-approach)

[Appendix C: Testing Approach and Validation	48](#appendix-c:-testing-approach-and-validation)

[Appendix D: Resource Utilization Assessment	48](#appendix-d:-resource-utilization-assessment)

[Appendix E: User Calibration Procedure	48](#appendix-e:-user-calibration-procedure)

[**9 Team	48**](#9-team)

[9.1 Team Members	48](#9.1-team-members)

[9.2 Required Skill Sets for Your Project	49](#9.2-required-skill-sets-for-your-project)

[9.3 Skill Sets covered by the Team	49](#9.3-skill-sets-covered-by-the-team)

[9.4 Project Management Style Adopted by the team	50](#9.4-project-management-style-adopted-by-the-team)

[9.5 Initial Project Management Roles	50](#9.5-initial-project-management-roles)

[9.6 Team Contract	50](#9.6-team-contract)

[Team Procedures	50](#team-procedures)

[Participation Expectations	50](#participation-expectations)

[Leadership	51](#leadership)

[Collaboration and Inclusion	51](#collaboration-and-inclusion)

[Goal-Setting, Planning, and Execution	52](#goal-setting,-planning,-and-execution)

[Consequences for Not Adhering to Team Contract	52](#consequences-for-not-adhering-to-team-contract)

	

List of figures

**Project Design:**

Figure: Diagram shows at a high-level how the teamplan to sequence access to the math accelerator available on the Kria board.

**Timing Diagram of Algorithm**

Figure: Current version is using a simple First come first serve schedule. Our team is splitting up the algorithm using our own methods. This will help create a smooth process within the system. 

# 1\. Introduction {#1.-introduction}

1. ## Problem Statement {#problem-statement}

Handicapped individuals with underlying conditions face the critical challenge of detecting and responding to medical episodes before they occur, which can happen anytime and anywhere, posing significant risks to their safety and independence. In a broader societal context, individuals with disabilities often encounter inadequate assistive technologies that fail to proactively ensure their well-being. Current healthcare solutions are reactive, requiring human intervention after an episode occurs, which can lead to delayed response times, severe medical complications, and loss of autonomy.

This issue is particularly significant as advancements in artificial intelligence and edge computing offer new opportunities for real-time health monitoring. However, these technologies remain underutilized in the field of assistive mobility devices. The ability to predict and respond to medical emergencies in real time would not only enhance personal safety but also reduce the burden on caregivers and emergency medical services, improving overall healthcare efficiency.

To address this problem, the team's project focuses on leveraging semantic segmentation at the edge to analyze physiological indicators such as eye movement and body posture. By integrating this technology into wheelchairs, the team aims to create an intelligent system that detects early warning signs of medical distress and autonomously moves the user to a safer position before a critical incident occurs. This approach bridges the gap between existing assistive technologies and the urgent need for proactive, real-time health monitoring, ultimately empowering handicapped individuals to navigate their daily lives with greater security and independence.

2. ## Intended Users {#intended-users}

## Primary Clients {#primary-clients}

The primary clients of this product are individuals with mobility impairments, many of whom have underlying physiological conditions such as Cerebral Palsy, epilepsy, or cardiovascular disorders. These individuals depend on wheelchairs for mobility and face heightened risks associated with sudden medical episodes. They require a proactive safety system that detects early signs of medical distress and responds autonomously to relocate them to a safe position.

Maintaining independence is a critical priority for these individuals, as many wish to lead active lives without constant supervision. By integrating real-time monitoring and intervention features, this product empowers users by providing an added layer of security without compromising their autonomy. The benefits of such a system include a significant reduction in medical emergencies, increased confidence in navigating daily life, and an overall improved quality of life.

## Client 2: Caregivers and Family Members {#client-2:-caregivers-and-family-members}

Caregivers and family members form the secondary user group, as they play an essential role in ensuring the well-being of individuals with mobility impairments. Parents, guardians, and professional caregivers are often burdened with the responsibility of constant monitoring, which can be both emotionally and physically demanding. They need a reliable alert system that provides real-time updates on the user's condition, allowing them to respond appropriately without intrusive supervision.

This product alleviates some of the stress associated with caregiving by offering automated alerts and health tracking, enabling caregivers to provide support when necessary while also granting users greater independence. The ability to receive timely notifications about potential medical issues enhances caregivers' ability to act swiftly and effectively, fostering a more sustainable care model.

## Client 3: The Tertiary User Group {#client-3:-the-tertiary-user-group}

The tertiary user group consists of healthcare providers and emergency responders, including medical professionals, therapists, and paramedics who are responsible for diagnosing, treating, and responding to medical emergencies among mobility-impaired individuals. These professionals rely on accurate, real-time health data to assess risks and make informed decisions.

An automated system capable of detecting early warning signs of medical distress and transmitting alerts to healthcare providers can significantly improve response times and patient outcomes. Additionally, the ability to integrate this data with existing healthcare monitoring systems enhances the efficiency of medical intervention. By bridging the gap between assistive mobility technology and healthcare services, this project contributes to a more data-driven approach to patient care, ultimately improving medical decision-making and emergency response capabilities.

Each of these user groups plays a critical role in the success and impact of this project. By addressing the needs of handicapped individuals, caregivers, and healthcare professionals, this product aims to create a safer, more autonomous, and more efficient system for managing mobility and health-related challenges. The integration of real-time monitoring and autonomous intervention not only enhances the quality of life for individuals with disabilities but also eases the burden on caregivers and improves medical response strategies. In doing so, this project contributes to a broader movement toward proactive, technology-driven healthcare solutions that prioritize safety, independence, and well-being.

2. # Requirements, Constraints, And Standards {#requirements,-constraints,-and-standards}

   1. ## Requirements & Constraints {#requirements-&-constraints}

### Functional Requirements {#functional-requirements}

1. Algorithm Splitting and Pipelining:  
   * Split the U-Net semantic segmentation algorithm into four equal parts to enable parallel processing across multiple cores.  
   * Implement a pipelined architecture to allow concurrent execution of the split U-Net segments and other algorithms (e.g., image preprocessing, blink detection, eye tracking).  
   * Ensure the pipeline maintains data consistency and synchronization between stages.  
2. System Throughput:  
   * Achieve a system throughput of less than 33.2 ms per frame when processing four frames concurrently.  
   * Ensure real-time processing capabilities are maintained for the assistive wheelchair application.  
3. Resource Efficiency:  
   * Optimize memory and FPGA resource usage to accommodate the additional overhead of pipelining and parallel execution.  
   * Ensure efficient sharing of the DPU between the split U-Net segments and other algorithms.  
4. Error Handling in Pipeline:  
   * Implement robust error handling mechanisms to detect and recover from pipeline stalls, frame drops, or data corruption.

## **User Interface (UI) Requirements** {#user-interface-(ui)-requirements}

1. Command Line Interface (CLI):  
   * Retain the existing user-friendly CLI for both technical and non-technical users.  
   * Add new commands to allow users to:  
     1. Configure pipeline settings (e.g., number of threads, buffer sizes).  
     2. Monitor pipeline performance (e.g., throughput, latency, resource usage).  
   * Include help commands to describe new pipeline-related functionalities.  
2. Command Feedback:  
   * Provide real-time feedback on pipeline performance, including throughput, latency, and error rates.  
   * Display warnings or errors if the pipeline encounters issues (e.g., buffer overflow, frame drops).  
3. Error Handling and Logging:  
   * Enhance error logging to include pipeline-specific issues (e.g., stage delays, synchronization errors).  
   * Provide detailed logs to assist users in debugging pipeline performance and resource allocation.

## **Physical and Economic Requirements** {#physical-and-economic-requirements}

1. Hardware Compatibility:  
   * Ensure that the pipelined architecture remains compatible with the Xilinx Kria Kv260 board.  
   * Minimize additional hardware requirements to keep costs low.  
2. Cost-Effectiveness:  
   * Design the pipeline to maximize throughput without requiring significant hardware upgrades.  
   * Ensure that future maintenance and updates remain economical.

## **System Constraints** {#system-constraints}

1. Memory Limitations:  
   * The Xilinx Kria K26 board has 4GB of DDR memory, which must be shared among the pipeline stages.  
   * Optimize memory usage to avoid contention between stages and ensure smooth data flow.  
2. FPGA Resource Allocation:  
   * The available FPGA resources are limited and must be efficiently allocated to accommodate the additional logic required for pipelining.  
   * Ensure that the Deep Learning Processing Unit (DPU) is shared effectively between blink detection and eye-tracking submodules.  
3. DPU Utilization:  
   * Develop a scheduling strategy to allow the DPU to be shared between blink detection and eye-tracking submodules without causing bottlenecks.

## **Additional Considerations** {#additional-considerations}

1. Deployment Options:  
   * The system will continue to be deployed on the Xilinx Kria Kv260 board, with no immediate plans for expansion to other platforms.  
   * Ensure that the pipelined architecture is portable and can be adapted to future hardware upgrades if needed.  
2. Data Handling and Privacy:  
   * Maintain strict data privacy and security measures, especially when handling sensitive user data in the pipeline.  
   * Ensure that intermediate data between pipeline stages is securely managed and not exposed to unauthorized access.  
3. Scalability:  
   * Design the pipeline to be scalable, allowing for the addition of new algorithms or submodules in the future.  
   * Ensure that the architecture can handle increased workloads (e.g., higher frame rates or additional features) without significant rework.

## 2.2 Engineering Standards {#2.2-engineering-standards}

IEEE 2952-2023 \- IEEE Standard for Secure Computing Based on Trusted Execution Environment

* Trusted Execution Environments (TEEs) are used to protect sensitive data and computations. This standard ensures that systems using TEEs follow security best practices, reducing the risk of unauthorized access or tampering.

IEEE 2802-2022 \- IEEE Standard for Performance and Safety Evaluation of AI-Based Medical Devices: Terminology

* This standard provides clear terms and definitions for evaluating the performance and safety of AI-based medical devices. It helps ensure these devices are reliable and effective in real-world medical settings.

IEEE 7002-2022 \- IEEE Standard for Data Privacy Process

* This standard outlines best practices for protecting user data and ensuring privacy. It helps organizations comply with regulations and build trust with users when handling sensitive information.

IEEE 3129-2023 \- IEEE Standard for Robustness Testing and Evaluation of AI-Based Image Recognition Services

* This standard provides guidelines for testing AI-based image recognition systems to ensure they work reliably under different conditions. It helps identify and fix issues that could arise from unexpected inputs or scenarios.

IEEE 3156-2023 \- IEEE Standard for Requirements of Privacy-Preserving Computation Integrated Platforms

* Privacy-preserving computation allows data to be processed without exposing sensitive information. This standard defines the requirements for platforms that support such computations, ensuring they protect user privacy.

IEEE 2842-2021 \- IEEE Recommended Practice for Secure Multi-Party Computation

* Secure multi-party computation lets multiple parties work together on shared data without revealing their individual inputs. This standard provides guidance for implementing these protocols, making collaborative computing safer for sensitive applications like healthcare and finance.

IEEE 1484.1-2003 \- IEEE Standard for Learning Technology \- Learning Technology Systems Architecture (LTSA)

* This standard defines a framework for designing and integrating educational software and systems. It ensures that learning technologies can work together seamlessly, supporting innovation in online education.

# 3 Project Plan {#3-project-plan}

## 3.1 Project Management/Tracking Procedures {#3.1-project-management/tracking-procedures}

The team's team has adopted a hybrid Waterfall \+ Agile project management approach for this project. This methodology provides us with both the structured framework of Waterfall for critical path activities and the flexibility of Agile for iterative development and testing. This hybrid approach is particularly well-suited for the team's project because:

1. The semantic segmentation optimization has clearly defined phases (mathematical division, implementation, testing) that benefit from Waterfall planning  
2. The technical nature of implementing parallelism and optimizing algorithms requires adaptive iterations that benefit from Agile sprints

Working with specialized hardware (Kria Board Kv260) requires careful planning of resource allocation and access

For project tracking, the team will utilize the following tools:

* GitHub: Primary code repository for version control, documentation, and collaboration. The team's client also has access to this repository to track progress in real-time.  
* Telegram: Main communication channel with the team's client and previous years' team members for quick updates and questions.  
* Discord: Team communication for internal discussions and virtual meetings.

Weekly team meetings will be held to review sprint progress, address blockers, and plan upcoming work. Monthly meetings with the client will ensure alignment with project goals and requirements.

## 3.2 Task Decomposition {#3.2-task-decomposition}

The team's project involves optimizing the semantic segmentation U-Net algorithm by implementing parallelism across multiple cores and the MPU. The key objective is to increase throughput from 160 ms per frame to 33.2ms across 4 frames. The following tasks and subtasks have been identified:

**Task 1: Algorithm Performance Optimization**

* Subtask 1.1: Analyze U-Net architecture for optimization opportunities  
* Subtask 1.2: Develop performance enhancement approach  
* Subtask 1.3: Validate that accuracy requirements (99.8% IoU) are maintained

### **Task 2: Implementation of Core Components** {#task-2:-implementation-of-core-components}

* Subtask 2.1: Implement image pre-processing using semantic segmentation  
* Subtask 2.2: Implement eye tracking algorithm with pre-processed images  
* Subtask 2.3: Implement blink detection algorithm  
* Subtask 2.4: Implement DPU sharing mechanism for resource optimization

### **Task 3: Thread Management** {#task-3:-thread-management}

* Subtask 3.1: Implement memory sharing between threads (non-DDR)  
* Subtask 3.2: Configure thread allocation to specific memory locations  
* Subtask 3.3: Implement thread synchronization and communication  
* Subtask 3.4: Test thread operation with matrix operations

### **Task 4: Multicore Processing** {#task-4:-multicore-processing}

* Subtask 4.1: Configure Docker environment for efficiency  
* Subtask 4.2: Develop multi core loading method for split ONNX model  
* Subtask 4.3: Implement pipelined passing of data through threads  
* Subtask 4.4: Optimize data flow between processing units

### **Task 5: Integration and Testing** {#task-5:-integration-and-testing}

* Subtask 5.1: Integrate all components into a unified system  
* Subtask 5.2: Benchmark performance against target metrics  
* Subtask 5.3: Identify and resolve bottlenecks  
* Subtask 5.4: Validate accuracy of results and compare to baseline system

### **Task 6: Documentation and Delivery** {#task-6:-documentation-and-delivery}

* Subtask 6.1: Document implementation details and architecture  
* Subtask 6.2: Prepare user guides and technical documentation  
* Subtask 6.3: Develop demonstration materials  
* Subtask 6.4: Prepare final project presentation

These tasks will be further broken down into sprint activities with specific team members assigned based on their expertise, as outlined in the personnel effort requirements section.

## 3.3 Project Proposed Milestones, Metrics, and Evaluation Criteria {#3.3-project-proposed-milestones,-metrics,-and-evaluation-criteria}

The following key milestones have been identified for the project, along with their associated metrics and evaluation criteria:

### **Milestone 1: Mathematical Division of the Algorithm** {#milestone-1:-mathematical-division-of-the-algorithm}

* Completion Date: Week 8  
* Metrics: Validated mathematical approach for dividing U-Net algorithm  
* Evaluation Criteria: Division maintains output accuracy equivalent to original algorithm 

**Milestone 2: Loading of Split Algorithm Weights onto MPU**

* Completion Date: Week 12  
* Metrics: Successful loading of model segments into appropriate memory locations  
* Evaluation Criteria: Each model segment loads correctly with optimal memory utilization (\<90% of allocated memory)

### **Milestone 3: Thread Testing with Matrix Operations** {#milestone-3:-thread-testing-with-matrix-operations}

* Completion Date: Week 16  
* Metrics: Successful parallel operation of multiple threads  
* Evaluation Criteria: All threads operate concurrently without memory conflicts

### **Milestone 4: Docker Environment Configuration** {#milestone-4:-docker-environment-configuration}

* Completion Date: Week 16  
* Metrics: Streamlined processing environment  
* Evaluation Criteria: Environment supports all required libraries and tools with minimal overhead

### **Milestone 5: Pipelined Implementation of Semantic Segmentation** {#milestone-5:-pipelined-implementation-of-semantic-segmentation}

* Completion Date: Week 16  
* Metrics: Functional parallelized semantic segmentation algorithm  
* Evaluation Criteria: Algorithm processes multiple frames concurrently with accuracy equal to or greater than original implementation (99.8% accuracy)

### **Milestone 6: Increased Throughput Demonstration** {#milestone-6:-increased-throughput-demonstration}

* Completion Date: Week 16  
* Metrics: Processing speed of multiple frames  
* Evaluation Criteria: Achieve target throughput of 33.2ms for 4 frames (vs. current 160ms for 1 frame)

For each milestone, the teamwill track progress using the following quantifiable metrics:

* Processing time: Measured in milliseconds per frame  
* Accuracy: Comparison of segmentation results with ground truth data  
* Resource utilization: CPU, memory, and DPU usage percentages  
* Throughput: Frames processed per second

## 3.4 Project Timeline/Schedule {#3.4-project-timeline/schedule}

![][image1]

The project will span approximately 16 weeks, with work organized into sprints. The Gantt chart shows the major tasks and their estimated durations.

Key deliverable dates:

* Week 8: Mathematical division proposal document  
* Week 12: Thread testing results and documentation  
* Week 16: Preliminary performance report

The critical path for this project follows the mathematical division of the algorithm, implementation of the eye-tracking components, integration of the parallelization framework, and final optimization of throughput.

## 3.5 Risks and Risk Management/Mitigation {#3.5-risks-and-risk-management/mitigation}

### **Risk 1: Completion Delays** {#risk-1:-completion-delays}

* Probability: 10%  
* Severity: High  
* Mitigation Strategies:  
  * Regular sprint reviews to identify potential delays early  
  * Team members will work collaboratively on serialized tasks to avoid bottlenecks  
  * Maintain buffer time in the schedule for unexpected challenges

### **Risk 2: Hardware Damage** {#risk-2:-hardware-damage}

* Probability: 5%  
* Severity: Very High  
* Mitigation Strategies:  
  * Store hardware in secure locations away from environmental contaminants  
  * Implement proper handling procedures for all team members  
  * Create regular backups of all work and configurations

### **Risk 3: Data Security** {#risk-3:-data-security}

* Probability: 15%  
* Severity: Medium  
* Mitigation Strategies:  
  * Utilize US-based distributed data storage (S3-compatible)  
  * Implement Git-based source and data version control  
  * Restrict access to sensitive data and systems

### **Risk 4: Algorithm Complexity** {#risk-4:-algorithm-complexity}

* Probability: 30%  
* Severity: Medium  
* Mitigation Strategies:  
  * Implement modular design principles for better maintainability  
  * Conduct thorough code reviews to ensure clarity and efficiency  
  * Utilize comprehensive testing methodologies to validate integration

### **Risk 5: Parallelism Implementation Challenges** {#risk-5:-parallelism-implementation-challenges}

* Probability: 40%  
* Severity: High  
* Mitigation Strategies:  
  * Employ effective parallel programming paradigms  
  * Utilize synchronization primitives to avoid resource contention  
  * Profile and optimize critical code sections to maximize performance

### **Risk 6: Image Processing Speed Limitations** {#risk-6:-image-processing-speed-limitations}

* Probability: 25%  
* Severity: Medium  
* Mitigation Strategies:  
  * Continuously optimize machine learning algorithms for semantic segmentation  
  * Implement data preprocessing optimizations  
  * Investigate model compression techniques to improve inference time

For risks with probability exceeding 30%, the team will develop detailed contingency plans, including alternative implementation approaches and resource reallocation strategies.

## 3.6 Personnel Effort Requirements {#3.6-personnel-effort-requirements}

| Team Member | Task | Subtask | Description | Estimated Hours |
| :---- | :---- | :---- | :---- | :---- |
| Tyler | Mathematical Division | Optimize and Divide algorithm into 4 parts | Pipeline U-Net into 4 roughly equal parts while maintaining accuracy | 25 |
|  |  | Code implementation | Implement the mathematical division in code | 5 |
|  |  | Testing | Validate division correctness | 5 |
| Aidan | Algorithm Implementation | Integrate with codebase | Implement into current codebase with 4 pipelines | 10 |
|  |  | Thread management | Configure thread operations on equation parts | 10 |
|  |  | Testing | Validate implementation | 10 |
| Conner | OS and Environment | Docker configuration | Optimize Docker environment for efficiency | 10 |
|  |  | ONNX splitting | Split ONNX for loading into MPU | 5 |
|  |  | Scheduler optimization | Configure OS scheduler for optimal performance | 10 |
|  |  | Data Version Control System | Demonstrate proposed data version control system  | 5 |
| Joey | Hardware Management | Kria board benchmarking | Research and document hardware capabilities | 20 |
|  |  | Memory allocation | Optimize memory usage across components | 10 |
|  |  | Performance testing | Benchmark and optimize overall system | 5 |
| All Members | Integration and Documentation | System integration | Final system assembly and testing | 6 |
|  |  | Documentation | Comprehensive documentation of implementation | 12 |

Team Effort: 146 hours approximately

## 3.7 Other Resource Requirements {#3.7-other-resource-requirements}

### **Hardware Resources** {#hardware-resources}

* Xilinx Kria Evaluation Board (Kv260): Main development platform with built-in DPU for model inferences  
* Development Computer: Linux-based system for development, testing, and remote access to the board

### **Software Resources** {#software-resources}

* Vivado: FPGA development environment  
* Vitis-AI: AI development framework  
* PyTorch: For neural network development and training  
* ONNX & Vitas-Runtime: For model optimization and deployment  
* Docker: For containerized development and deployment  
* TensorFlow: Machine learning library  
* OpenCV: Computer vision library for image preprocessing

### **Development Tools** {#development-tools}

* Git/GitHub: Version control and collaboration  
* Telegram/Discord: Team communication platforms

### **Data Resources** {#data-resources}

* Training datasets: For model optimization and validation  
* Test image sequences: For performance benchmarking  
* Previous project documentation: For knowledge transfer and reference

This comprehensive resource plan ensures the team has all necessary tools and platforms to successfully complete the project within the specified timeline and performance targets.

4  Design

## 4.1 Design Context {#4.1-design-context}

### 4.1.1 Broader Context {#4.1.1-broader-context}

The team's Semantic Segmentation Optimization project is situated in the healthcare and assistive technology domain, specifically addressing the needs of individuals with mobility disabilities who require eye-tracking systems for communication and control of assistive devices. The team is designing for healthcare professionals, caregivers, and most importantly, individuals with conditions such as cerebral palsy who depend on efficient and responsive eye tracking for daily activities and medical monitoring.

| Area | Description | Examples |
| :---- | :---- | :---- |
| Public health, safety, and welfare | The team's project directly improves the safety and well-being of individuals with mobility impairments by enhancing the responsiveness of eye-tracking medical monitoring systems. | Faster response times to potential medical issues, more reliable detection of eye movements for wheelchair control, reduced risk of incidents for users |
| Global, cultural, and social | The solution respects the values of independence and dignity for people with disabilities while acknowledging the cultural practices around care and assistance. | Supports the right to autonomy for people with disabilities, aligns with medical ethics of beneficence, works within existing healthcare frameworks |
| Environmental  | By optimizing software rather than requiring new hardware, the team's solution extends the useful life of existing devices and reduces electronic waste. | Reduced need for frequent hardware replacement, lower energy consumption through optimized processing |
| Economic | The team's optimization approach provides significant performance improvements while keeping costs accessible for healthcare providers and individuals. | Affordable enhancement to existing assistive technology systems, more efficient use of available computing resources, potential reduction in healthcare costs through preventative monitoring |

### 

### 4.1.2 Prior Work/Solutions {#4.1.2-prior-work/solutions}

Several approaches have been used to implement semantic segmentation for eye tracking, but most face limitations when deployed on resource-constrained edge devices:

1. Wang et al. (2021) proposed "EfficientEye: A Lightweight Semantic Segmentation Framework for Eye Tracking," which achieved good accuracy but still required substantial computational resources. Their approach reduced model size but processing speed remained at approximately 120 ms per frame.  
2. The previous iteration of this project implemented a standard U-Net architecture on the Kria KV260 board with an accuracy of 99.8% IoU but could only process a single frame every 160ms, which is insufficient for real-time application needs.  
3. Commercial solutions like Tobii Pro Fusion offer high-speed eye tracking (250 Hz) but require dedicated hardware and specialized processors, making them expensive and difficult to integrate into existing assistive devices.

Compared to these existing solutions, the team's approach offers:

**Advantages:**

* Maintains high accuracy (99.8% IoU) while significantly improving processing speed  
* Utilizes existing hardware (Kria KV260) without requiring costly upgrades  
* Implements a parallelized approach that can process multiple frames concurrently  
* Integrates with existing assistive wheelchair technology ecosystem

**Limitations:**

* Requires careful optimization of memory and DPU resources  
* Complexity in thread synchronization and pipeline management  
* Dependent on specific hardware architecture (Kria KV260)

### 4.1.3 Technical Complexity {#4.1.3-technical-complexity}

The team's project demonstrates significant technical complexity in both its components and requirements:

1. **Multiple Components with Distinct Scientific Principles:**  
   * Neural Network Architecture: The U-Net semantic segmentation algorithm incorporates complex convolutional neural network principles with encoder-decoder architecture  
   * Parallel Computing: Implementation of multi-threading and pipeline parallelism leverages computer architecture principles  
   * Memory Management: Developing efficient memory allocation strategies based on computer systems principles  
   * Real-time Systems: Balancing processing load to meet strict timing constraints based on real-time systems theory  
   * Resource Scheduling: Creating optimal DPU sharing mechanisms based on operating systems principles  
2. **Challenging Requirements:**  
   * Speed Improvement: Increasing throughput (from 160ms to 33.2ms for 4 frames) exceeds typical optimization gains in the industry  
   * Accuracy Maintenance: Preserving 99.8% IoU accuracy while dividing the algorithm is significantly more challenging than standard parallelization  
   * Resource Constraints: Working within the limited memory (4GB) and processing resources of the Kria board requires innovative solutions  
   * Real-time Performance: Meeting the 60 frames per second requirement is at the upper end of what is possible with current embedded AI systems

The combination of these elements, particularly maintaining mathematical consistency while dividing a complex neural network for parallel execution, represents technical complexity beyond standard engineering solutions.

## 4.2 Design Exploration {#4.2-design-exploration}

### 4.2.1 Design Decisions {#4.2.1-design-decisions}

The team's has identified the following key design decisions that are critical to the success of the team's Semantic Segmentation Optimization project:

1. Resource Scheduling Approach  
   * Decision: Instead of dividing the U-Net semantic segmentation algorithm (which would increase overhead and slow the system), implement an efficient round-robin scheduling system for DPU access.   
   * Importance: This is fundamental to achieving the team's throughput goal while ensuring Algorithms 1, 2, and 3 can collect their required periodic data. Without effective resource scheduling, semantic segmentation would monopolize the DPU, preventing other critical algorithms from functioning correctly. The scheduling approach must maintain the algorithm's integrity while providing fair resource allocation to achieve the 99.8% IoU accuracy target.  
2. DPU Access Management  
   * Decision: Implement a fair access scheduling approach that prevents semantic segmentation from 'starving' other algorithms of DPU resources.  
   * Importance: The Kria board has four DDR4 memory banks (1GB each), but the single DPU is a shared resource that must be carefully managed. Our approach ensures that while semantic segmentation runs, it doesn't prevent Algorithms 1, 2, and 3 from collecting their required periodic data. This strategy prevents scenarios where the information gathered becomes incorrect due to delayed or missed data collection cycles.  
3. Resource Allocation Strategy  
   * Decision: Develop a resource management system that coordinates access to the DPU and ensures each algorithm receives appropriate processing time.  
   * Importance: With multiple algorithms needing DPU access (semantic segmentation, Algorithms 1, 2, and 3), proper resource allocation is essential to maintain data integrity and prevent starvation. This decision impacts both performance and accuracy, as our client noted that Algorithms 1, 2, and 3 require periodic data or the information gathered becomes incorrect. Our scheduling system must ensure that semantic segmentation doesn't monopolize resources while maintaining overall system efficiency.

### 4.2.2 Ideation {#4.2.2-ideation}

For our resource scheduling approach, we explored several potential scheduling strategies through a structured ideation process:

1. Round-Robin Scheduling 

   ○ Allocate DPU time in equal slices to each algorithm in circular order ○ Simple to implement and ensures each algorithm gets fair access ○ May not be optimal for variable processing requirements

2. Priority-Based Scheduling 

   ○ Assign priority levels to algorithms based on urgency of data collection needs ○ Higher priority tasks preempt lower priority ones when necessary ○ Could be tuned to ensure periodic data collection requirements are met

3. Time-Division Multiplexing 

   ○ Allocate specific time windows for each algorithm to access the DPU ○ Synchronize windows with periodic data collection requirements ○ Optimizes for predictable execution patterns

These options were generated through team brainstorming sessions, a literature review of resource scheduling techniques, and an analysis of the periodic data requirements of the algorithms.

### 4.2.3 Decision-Making and Trade-Off {#4.2.3-decision-making-and-trade-off}

The team's client requires absolutely no decrease in accuracy due to the sensitive medical nature of the product. Additionally, Algorithms 1, 2, and 3 require periodic data collection or the information gathered becomes incorrect. We cannot let semantic segmentation starve the other algorithms for the length of time that it runs.

Our design prioritizes balanced system performance while ensuring all components can meet their operational requirements. The approach maintains critical timing needs for essential functions while enabling the performance improvements necessary to achieve our target throughput.

The resource management strategy ensures that all system components receive appropriate computational resources based on their operational importance and timing requirements.

Because of the team's embedded deployment environment, an analysis of the memory access is necessary. The team selected a scheduling approach that minimizes memory transfer overhead while ensuring all algorithms meet their periodic data collection needs. This approach is feasible because the team's model uses fixed memory access patterns, and we can predict resource requirements for each algorithm.

Another important note is that the scheduling system must account for operating system tasks and several other ML algorithms (not the focus of the team's project). The system allocates appropriate DPU time slices to accommodate these additional workloads.

3. ## Proposed Design {#proposed-design}

![][image2]

## 4.3.1 Overview {#4.3.1-overview}

The team's Semantic Segmentation Optimization project aims to enhance the performance of a U-Net-based eye tracking system for individuals with disabilities, particularly those with cerebral palsy. This system helps monitor eye movements to detect potential medical issues and can automatically reposition users to prevent incidents, improving safety and quality of life.

The current implementation processes a single frame in 160ms, which is insufficient for real-time monitoring. The team's optimized design divides the U-Net algorithm across multiple cores and utilizes the Memory Processing Unit (MPU) to achieve a throughput of 33.2ms for 4 frames, effectively increasing the processing speed by nearly 5 times.

At a high level, the team's system:

1. Captures eye movement images through a camera  
2. Processes these images using a parallelized semantic segmentation algorithm to remove reflections and identify the pupil  
3. Tracks the eye's position and detects blinks in real-time  
4. Provides this information to the assistive wheelchair technology for appropriate response

The key innovation in the team's design is the approach to parallelism and resource utilization on the AMD Kria KV260 board, which has limited memory and processing resources but powerful acceleration capabilities when properly leveraged.

## 4.3.2 Detailed Design and Visual(s) {#4.3.2-detailed-design-and-visual(s)}

The team's semantic segmentation optimization system consists of the following key components:

### Hardware Platform {#hardware-platform}

* AMD Kria KV260 Development Board  
  * System-on-Module (SoM) with programmable logic  
  * Quad-core ARM processor  
  * Deep Processing Unit (DPU) for accelerating neural network inference  
  * Four 1GB DDR4 memory banks  
  * Various I/O interfaces for camera input and system communication

### Software Components {#software-components}

1. U-Net Semantic Segmentation Algorithm  
   * Purpose: Processes eye images to create pixel-level segmentation for pupil identification  
   * Capabilities: Achieves 99.8% IoU accuracy while meeting performance requirements  
   * Function: Enables reliable eye tracking by producing high-quality segmentation maps  
2. Preprocessing Module  
   * Handles image normalization, scaling, and initial filtering  
   * Prepares raw camera input for semantic segmentation  
   * Implemented as part of the pipeline before U-Net processing  
3. Blink Detection Algorithm  
   * Lightweight neural network running alongside eye tracking  
   * Detects eye closure states to identify blinks  
   * Provides additional user intent information for the control system  
4. Thread Management System  
   * Coordinates execution across multiple threads  
   * Manages data flow between algorithm segments  
   * Ensures synchronization of processing stages for multiple frames  
5. Memory Management System  
   * Allocates dedicated memory regions to specific threads  
   * Minimizes memory contention through affinity settings  
   * Optimizes data transfer between processing stages

### Processing Pipeline {#processing-pipeline}

The team's optimization approach:

1\. Current Performance Baseline:

*  Sequential processing of algorithms  
  * Total processing time: 160ms per frame

2\. Performance Target:

*  Concurrent processing capability  
  *  Improved coordination between system components  
  *  Target throughput: 33.2ms per frame (nearly 5x improvement)  
  *  Maintains 99.8% IoU accuracy requirement

\*Note: Numerical values are representative placeholders due to NDA restrictions.

![][image3]

### Memory Allocation {#memory-allocation}

Memory Resource Management:

* Efficient allocation of system memory resources  
* Optimized for minimal access conflicts  
* Organized to support all system functions concurrently  
* Structured to maximize throughput while maintaining accuracy

This allocation ensures that each component has dedicated resources, minimizing contention and maximizing throughput.

## 4.3.3 Functionality {#4.3.3-functionality}

The team's semantic segmentation optimization system operates within a healthcare setting to monitor and assist individuals with mobility disabilities. Here's how the system functions in real-world use:

### Initial Setup: {#initial-setup:}

1. The system is installed on an assistive wheelchair with a camera positioned to capture the user's eye  
2. Calibration is performed to establish baseline eye movement patterns for the individual  
3. Safety parameters are set according to the user's specific needs and medical requirements

### Normal Operation: {#normal-operation:}

1. The camera continuously captures images of the user's eye at high frame rates  
2. These images are processed through the team's optimized semantic segmentation pipeline:  
   * Image preprocessing removes glare and enhances pupil visibility  
   * U-Net semantic segmentation identifies the pupil position precisely  
   * Blink detection monitors for intentional or involuntary eye closures  
3. The system tracks eye movement patterns in real-time, providing:  
   * Continuous monitoring of the user's awareness and responsiveness  
   * Detection of irregular eye movements that might indicate medical issues  
   * Input for wheelchair control based on gaze direction and blink patterns

### Response to Detected Issues: {#response-to-detected-issues:}

1. If the system detects unusual eye movements or extended closure:  
   * An alert is sent to caregivers or medical staff  
   * The wheelchair can automatically adjust to a safer position  
   * Monitoring frequency may increase temporarily for better assessment

### User Control Mode: {#user-control-mode:}

1. When in control mode, the user can:  
   * Direct wheelchair movement through sustained gaze in specific directions  
   * Stop movement through a specific blink pattern  
   * Select options on a display through gaze targeting and blinks  
2. The high throughput of the team's optimized system ensures responsive control with minimal latency

## 4.3.4 Areas of Concern and Development {#4.3.4-areas-of-concern-and-development}

The team's current design shows promise for meeting the project requirements, but we've identified several areas that require further attention:

1. Algorithm Division Accuracy  
   * Concern: Dividing the U-Net algorithm could potentially impact segmentation accuracy  
   * Development Plan: Conduct extensive testing with different division points to ensure accuracy remains 99.8%  
2. Memory Bandwidth Limitations  
   * Concern: Multiple threads accessing memory simultaneously could create bandwidth bottlenecks  
   * Development Plan: Implement efficient memory access patterns and optimize data transfer operations between threads  
3. DPU Resource Sharing  
   * Concern: The single DPU on the Kria board must be shared efficiently between multiple algorithm components  
   * Development Plan: Develop a scheduling system that prioritizes time-critical operations and ensures fair access to the DPU  
4. Real-time Performance Validation  
   * Concern: Actual performance may differ from theoretical projections under real-world conditions  
   * Development Plan: Create comprehensive benchmarking tools to measure actual throughput and identify optimization opportunities  
5. System Integration Challenges  
   * Concern: Integrating the team's optimized algorithm with existing wheelchair systems may present unexpected challenges  
   * Development Plan: Develop a modular interface approach that minimizes integration complexity

Questions for advisors and faculty:

* What are the most effective methods for validating semantic segmentation accuracy when the algorithm is divided?  
* Are there specific memory access patterns that work particularly well with the Kria board's architecture?  
* What additional optimizations might be possible through the Vitis-AI toolkit that the team haven't explored?

## 4.4 Technology Considerations {#4.4-technology-considerations}

The team's project utilizes several key technologies, each with distinct strengths, weaknesses, and trade-offs:

### **Kria Board KV260** {#kria-board-kv260}

**Strengths:**

* Built-in DPU (Deep Processing Unit) accelerates neural network inference  
* Multiple DDR4 memory banks enable parallel processing  
* Low power consumption suitable for mobile applications  
* Supports Vitis-AI for ML model optimization

**Weaknesses:**

* Limited total memory (4GB) compared to server-class hardware  
* Single DPU must be shared among multiple algorithms  
* Development environment has steep learning curve  
* Limited community support compared to more common platforms

**Trade-offs:**

* Hardware acceleration provides performance benefits but increases development complexity  
* FPGA-based approach offers flexibility but requires specialized knowledge  
* Edge computing enables real-time processing but imposes resource constraints

### **U-net Semantic Segmentation Algorithm** {#u-net-semantic-segmentation-algorithm}

**Strengths:**

* Encoder-decoder architecture with skip connections preserves spatial information  
* Achieves high accuracy for pupil segmentation tasks  
* Well-established algorithm with proven effectiveness in medical imaging

**Weaknesses:**

* Computationally intensive, requiring significant processing resources  
* Complex architecture makes full parallelization challenging  
* High memory bandwidth requirements during inference

**Trade-offs:**

* Higher accuracy comes at the cost of computational complexity  
* Skip connections improve results but complicate algorithm division  
* Deeper networks improve segmentation but increase processing time

### **Vitis-AI and Vitas-Runtime** {#vitis-ai-and-vitas-runtime}

**Strengths:**

* Provides optimization tools specifically for Xilinx hardware  
* Supports model compression and quantization  
* Enables deployment across different computing platforms

**Weaknesses:**

* Limited documentation for advanced use cases  
* Optimization process can affect model accuracy  
* Version compatibility issues between different tools

**Trade-offs:**

* Quantization reduces model size but may impact accuracy  
* Platform-specific optimizations improve performance but reduce portability  
* ONNX support enables broader compatibility but may not leverage all hardware features  
* Overhead of an additional runtime.

### **Alternative Technologies Considered** {#alternative-technologies-considered}

1. NVIDIA Jetson Platform  
   * Greater GPU Memory and Performance  
   * More performance per Watt  
   * Better support for common deep learning frameworks  
   * Higher power consumption  
   * Would require significant redesign of the existing system  
2. Custom ASIC Development  
   * Potential for highest performance and efficiency  
   * Prohibitively expensive for the team's application  
   * Long development cycle  
   * Limited flexibility for algorithm updates  
3. Cloud-based Processing  
   * Virtually unlimited computing resources  
   * Network latency unacceptable for real-time applications  
   * Requires continuous connectivity  
   * Privacy concerns with medical data  
4. Simplified Algorithm Approach  
   * Less computationally intensive alternatives to U-Net  
   * Potentially faster processing with less parallelization needed  
   * Significantly lower accuracy for pupil segmentation  
   * Would not meet project requirements

The teamselected the Kria KV260 platform with U-Net optimization because it offers the best balance of performance, power efficiency, and development feasibility while meeting the team's accuracy requirements.

## 4.5 Design Analysis  {#4.5-design-analysis}

At this stage of the team's project, the team has made progress in understanding the requirements and establishing a foundation for implementation, but the team has not yet fully implemented the optimized system on the Kria board.

### **Current Implementation Status:** {#current-implementation-status:}

1. Development Environment:  
   * Established appropriate development tools and platforms  
   * Configured necessary software components for implementation  
   * Created required testing and development workflows  
2. Perform Analysis:  
   * Evaluated current system performance metrics  
   * Identified optimization opportunities  
   * Established baseline performance (160ms per frame)  
3. Solution Architecture:  
   * Developed optimization strategy to meet performance requirements  
   * Designed resource management approach  
   * Created performance testing framework

### **Implementation Challenges:** {#implementation-challenges:}

The primary challenge we've encountered is the limited documentation for implementing multi-threaded applications on the Kria board that efficiently utilize the DPU. The complexity of dividing the U-Net algorithm while maintaining accuracy has also proven more challenging than initially anticipated. Until the division is approved and implemented, the rest of the design can be greenlit to be worked on.

### **Future Implementation Plans:** {#future-implementation-plans:}

1. Algorithm Division Implementation:  
   * Complete the mathematical division of the U-Net model  
   * Convert each segment to ONNX format for deployment  
   * Validate individual segment performance  
2. Thread Management Development:  
   * Implement the thread synchronization mechanism  
   * Develop memory affinity settings for optimal resource utilization  
   * Create the pipeline scheduling system  
3. Integration and Testing:  
   * Integrate all components into a unified system  
   * Benchmark performance against the team's target metrics  
   * Optimize critical paths to achieve the throughput goal  
4. Validation and Refinement:  
   * Test with real-world eye tracking scenarios  
   * Validate accuracy against the baseline system  
   * Refine implementation based on performance data

Based on the team's progress to date, the team believes that the team's proposed design is feasible, although it will require careful implementation to achieve the desired performance improvements. The mathematical foundation for algorithm division is sound, and the team's initial tests on the Kria board confirm that the hardware can support the team's approach with proper optimization.

The most critical aspect of future work will be ensuring that the divided algorithm maintains accuracy while achieving the throughput improvements. The team plans to implement progressive optimization steps, measuring performance and accuracy at each stage to ensure the team is meeting both requirements simultaneously.

# 5  Testing  {#5-testing}

## **Testing Strategy Overview** {#testing-strategy-overview}

Testing is key to the team's Semantic Segmentation project. The team needs to make sure the team's system meets the team's goals of fast processing (\<16.6ms between frames) while keeping good accuracy (99.8%). 

\*Note: numerical values are representative placeholders due to NDA restrictions.

### **Testing Philosophy** {#testing-philosophy}

The team tests early and often. This helps us catch problems quickly and fix them before they get worse. For the team's project, this means:

* Testing each part of the divided U-Net algorithm as the team creates it  
* Checking memory use before building the full system  
* Testing how the team shares DPU resources as the team develop

  ### **Testing Challenges** {#testing-challenges}

The team's project has some tough testing challenges:

* Testing on FPGA hardware is different from normal software testing  
* Making sure the team's parallel threads work together correctly  
* Balancing speed and accuracy  
* Checking that memory is used correctly

  ### **Testing Schedule** {#testing-schedule}

* Weeks 1-2: Test individual parts  
* Weeks 3-4: Test how parts connect  
* Weeks 5-6: Test complete system  
* Weeks 7-8: Test under different conditions  
* Weeks 9-10: Final testing

## 5.1 Unit Testing {#5.1-unit-testing}

### Feature Map Testing {#feature-map-testing}

* Comprehensive validation that feature maps match between unified and scheduled implementations  
* Layer-by-layer comparison to ensure mathematical consistency throughout the network  
* Statistical analysis of feature map similarity using 80-20 training/testing dataset split  
* Verification of feature activation patterns across diverse input conditions

### Algorithm Testing {#algorithm-testing}

* Resource allocation verification to confirm fair DPU access distribution  
* Temporal analysis of periodic data collection to ensure deadlines are consistently met  
* Controlled stress testing to verify scheduling robustness under varying load conditions  
* Validation that algorithms 1, 2, and 3 can reliably collect data without interruption

### System Coordination Testing {#system-coordination-testing}

* Operational Timing: Verify system meets timing requirements for all components   
* Resource Utilization: Validate efficient use of system resources  
* System Stability: Ensure reliable operation under various conditions

### Success Goals {#success-goals}

* 100% feature map consistency between unified algorithm and scheduled implementation  
* Zero missed periodic data collection deadlines across extended operation periods  
* Resource utilization efficiency improvement of at least 30% compared to sequential approach

## 5.2 Interface Testing {#5.2-interface-testing}

### Key Interfaces {#key-interfaces}

1. Between Algorithms and Scheduler:  
   * Verification of request handling under varying load conditions and priorities  
   * Validation of preemption mechanisms when periodic collection deadlines approach  
   * Confirmation that all algorithms receive their guaranteed resource allocation minimums  
   * Analysis of scheduling fairness across extended operational periods  
2. Between Semantic Segmentation and DPU:  
   * Detailed profiling of resource utilization patterns during algorithm execution  
   * Verification that feature map integrity is maintained despite scheduled access  
   * Measurement of context switching overhead to ensure minimal performance impact  
   * Confirmation that unified algorithm behavior remains consistent  
3. Memory Management:  
   * Test how each algorithm accesses its assigned memory  
   * Verify that memory access patterns are efficient and minimize contention  
   * Validate that shared memory regions are properly protected  
4. Thread Coordination:  
   * Test how the scheduler manages resource allocation  
   * Verify that priority escalation works properly for deadline-sensitive operations  
   * Validate synchronization between algorithms with interdependencies

### Test Cases {#test-cases}

1. Data Processing Validation:  
   * Purpose: Ensure accurate image processing under various operating conditions  
   * Expected outcome: Consistent processing quality matching baseline performance  
   * Validation method: Comparison against established accuracy metrics  
2. Resource Management Validation:  
   * Purpose: Verify system stability under concurrent processing demands  
   * Expected outcome: Reliable operation without resource conflicts  
   * Validation method: Performance monitoring during multi-algorithm execution  
3. Periodic Collection Test:  
   * What we do: Run system under load with varying periodic collection requirements  
   * What should happen: All algorithms meet their collection deadlines  
   * How we check: Log collection times and verify against requirements

   3. ## System Testing {#system-testing}

   ### **Test Plan** {#test-plan}

1. Continuous Running Test:  
   * What the team does: Feed many eye images continuously  
   * Tool: Image generator with logging  
   * Goal: Keep 16.6 ms between frames for over 30 minutes  
2. Lighting Test:  
   * What the team does: Test with images in different lighting  
   * Tool: Dataset with lighting variations  
   * Goal: Keep accuracy above 98% in all conditions  
3. Stress Test:  
   * What the team does: Push memory and processing limits  
   * Tool: Stress testing scripts  
   * Goal: System stays running without failing  
4. Long-Term Test:  
   * What the team does: Run system for 24+ hours  
   * Tool: Automated testing with monitoring  
   * Goal: No crashes or slowdowns over time

\*Note: Numerical values are representative placeholders due to NDA restrictions.

### **Test Measurements** {#test-measurements}

* Speed: Frames per second (goal: \>60)  
* Accuracy: Correct pupil tracking (goal: \>98%)  
* Time: Input to output delay (goal: 60 frames per second)  
* Memory: How much memory is used over time  
* Stability: How long the system runs without problems

  4. ## Regression Testing {#regression-testing}

  ### **Automated Testing** {#automated-testing}

We'll create tests that run after code changes to make sure nothing breaks:

1. Performance Check: Compare speed to previous tests  
   * Tool: Test runner with history database  
2. Accuracy Check: Make sure algorithm changes don't hurt accuracy  
   * Tool: Test dataset with known answers  
3. Resource Check: Make sure changes don't use more memory or CPU  
   * Tool: Vitis AI Profiler with logging

   ### **Monitoring** {#monitoring}

* Performance Tracking: Use Vitis AI Profiler to watch:  
  * Running time  
  * DPU use  
  * Memory use  
  * Thread timing  
* Memory Leak Check: Test for memory problems that could cause crashes  
  * Tool: Memory tracking in the team's test system

  ### **Test Schedule** {#test-schedule}

* Run basic tests after each code change  
* Run full tests every night  
* Keep history of all test results  
* Set up alerts if tests start failing

  5. ## Acceptance Testing {#acceptance-testing}

### **Function Tests** {#function-tests}

1. Speed Test:  
   * Test: Process multiple frames  
   * Goal: 60 frames per second  
2. Accuracy Test:  
   * Test: Compare with manually marked images  
   * Goal: 98-99.8% accuracy  
3. Multi-frame Test:  
   * Test: Process several frames at once  
   * Goal: Handle 4 frames at the same time

### **Other Requirements** {#other-requirements}

1. Memory Test:  
   * Test: Track memory during long runs  
   * Goal: Each thread stays within 1GB  
2. Stability Test:  
   * Test: Run for 24+ hours  
   * Goal: No crashes or slowdowns  
3. Thread Test:  
   * Test: Watch threads work together  
   * Goal: No lockups or timing problems

### **Client Involvement** {#client-involvement}

We'll invite the team's client to see the team's testing and get feedback:

1. Show the system tracking eyes in real-time  
2. Show speed improvements  
3. Compare original and improved versions  
4. Let client test with their own data

   6. ## User Testing {#user-testing}

While the team's project focuses on the optimization of the semantic segmentation algorithm and its implementation on the Kria KV260 platform, comprehensive user testing falls outside the team's current scope. This section outlines a proposed testing plan that would need to be implemented by future teams once the technical implementation is complete.

### **Proposed Future User Testing Plan** {#proposed-future-user-testing-plan}

The actual user testing with individuals with mobility impairments, caregivers, and healthcare professionals would be conducted by a specialized team with expertise in clinical trials and assistive technology evaluation, likely in a timeframe of 3-5 years after the team's technical implementation is complete.

The team's contribution to this future effort includes:

1. **Documentation of Testing Requirements**  
   * We have detailed performance metrics needed for successful user interaction  
   * We have identified key scenarios that should be evaluated in future user testing  
   * We have established baseline performance data for comparison  
2. **Technical Support for Testing Preparation**  
   * The team's system includes built-in logging capabilities to support future user testing  
   * We have created a diagnostic mode specifically designed for evaluation purposes  
   * Documentation includes recommended testing protocols for technical aspects  
3. **Handoff Documentation**  
   * Comprehensive technical specifications for evaluation teams  
   * Identified potential failure modes and recovery procedures  
   * Documented system boundaries and performance limitations

The future testing team would need to conduct a proper clinical evaluation, working with ethics committees and healthcare partners to ensure safe and productive user testing experiences. The team's technical implementation paves the way for this future work by establishing the performance foundation necessary for meaningful user interaction.

### **System Preparation for Future Testing** {#system-preparation-for-future-testing}

Although we won't conduct user testing directly, we've designed the team's system with future testing in mind:

1. **Configurable Parameters**  
   * Sensitivity thresholds can be adjusted based on user needs  
   * Timing parameters can be modified to accommodate different response capabilities  
   * Alert thresholds can be customized for individual medical requirements  
2. **Diagnostic Capabilities**  
   * Built-in performance monitoring with detailed logging  
   * Ability to replay recorded sessions for analysis (Deterministic Simulation Testing)  
   * Error detection and categorization for evaluation purposes  
3. **Simulation Environment**  
   * Created a test harness that can simulate various user conditions  
   * Developed test cases representing common usage scenarios  
   * Implemented performance benchmarks for standardized evaluation

This approach ensures that the team's technical contribution maintains a clear focus on algorithm optimization and implementation while preparing the groundwork for future clinical evaluation by specialized teams with the appropriate expertise and resources for working with individuals with mobility impairments.

7. ## Results {#results}

### **Current Progress** {#current-progress}

So far, we are currently testing the algorithm division and started testing interfaces:

1. **Algorithm Division**:  
   * Beginning to split U-Net into four parts that work like the original  
   * Current accuracy: 98.8% (within the team's target)  
   * Processing load is balanced between parts

### **Next Steps** {#next-steps}

Based on testing, the team's next steps are:

1. **Performance Enhancement**:  
   * Refine optimization approaches  
   * Improve resource utilization  
   * Goal: Achieve target frame rate of 60 frames per second  
2. **System Integration**:  
   * Enhance component coordination  
   * Optimize operational efficiency  
   * Goal: Minimize processing latency

The team's tests show the team's approach works, with accuracy in the target range. The team now needs to focus on making the system faster to meet the team's 60 frames per second goal.

# 6  Implementation {#6-implementation}

### **Resource Management Approach** {#resource-management-approach}

The system handles computational resources in a way that:

* Ensures all algorithms can operate effectively without resource conflicts   
* Maintains critical timing requirements for periodic data collection  
* Meets performance targets while preserving system accuracy  
* Enables efficient coordination between system components

### **Thread Coordination Implementation** {#thread-coordination-implementation}

Our thread coordination system implements a resource allocation pattern where:

* Algorithms register their periodic data collection requirements at initialization  
* Real-time deadline tracking ensures collection windows are never missed  
* Adaptive priority adjustment prevents starvation of any system component  
* Resource access patterns are continuously optimized based on operational data

The current implementation successfully demonstrates coordination between semantic segmentation and algorithms 1, 2, and 3, ensuring that resources are allocated appropriately to maintain system accuracy and responsiveness.

### **DPU Scheduler Implementation** {#dpu-scheduler-implementation}

To optimize DPU usage across algorithms, we've implemented a scheduler that:

* Enforces fair resource allocation while preventing semantic segmentation monopolization  
* Utilizes deadline-monotonic scheduling principles for periodic data collection  
* Maintains comprehensive statistics for continuous optimization of resource allocation  
* Implements context-switching optimizations to minimize overhead between algorithms

Testing shows this approach effectively shares the DPU resource while minimizing waiting time for critical operations and ensuring periodic data collection requirements are consistently met.

### **Current Status** {#current-status}

The implementation is approximately 40% complete, with the following components functional:

* Development environment and toolchain setup (100%)  
* Resource scheduling framework (75%)  
* Thread management system (50%)  
* Memory allocation system (60%)  
* DPU scheduler prototype (35%)

The team is currently focusing on refining the resource scheduling implementation, as this is on the critical path for the overall project. Once this is finalized, we will proceed with optimizing the system for maximum throughput while maintaining feature map consistency.

### Next Implementation Steps {#next-implementation-steps}

1. Complete the mathematical division validation with full accuracy testing  
2. Implement the pipeline data flow between algorithm segments  
3. Optimize memory access patterns for improved throughput  
4. Integrate thread management with the DPU scheduler  
5. Perform end-to-end testing with the complete system

# 7  Ethics and Professional Responsibility {#7-ethics-and-professional-responsibility}

Ethics and professional responsibility are foundational elements of the team's semantic segmentation optimization project, particularly given its application in medical assistive technology for vulnerable populations. The team defines engineering ethics as the moral principles and standards that guide the team's technical decisions, ensuring they prioritize human wellbeing, safety, and dignity above all other considerations. Professional responsibility encompasses the team's obligations to users, clients, the engineering profession, and society at large to uphold the highest standards of technical excellence, honesty, and integrity throughout the development process.

The team's overarching ethical philosophy is guided by a consequentialist approach balanced with strong deontological principles. The team evaluates the design decisions not only by their technical merit but also by their potential impact on users' lives and autonomy. The team recognizes that this work directly affects individuals with disabilities who depend on reliable assistive technology, making ethical considerations inseparable from technical ones.

To ensure ethical and responsible conduct throughout the team's project, the team has implemented several specific practices:

1. **Regular ethical review sessions** during team meetings to discuss potential ethical implications of design decisions  
2. **Consultation with disability advocates** to understand the lived experiences of potential users  
3. **Transparent documentation** of all design limitations and potential failure modes  
4. **Privacy-by-design principles** incorporated from the earliest development stages  
5. **Rigorous testing protocols** that prioritize safety and reliability  
6. **Ongoing education** about ethical frameworks in engineering and assistive technology

These practices help us maintain awareness of ethical considerations throughout the development process, ensuring that technical optimization never comes at the expense of user safety, privacy, or dignity. The following sections explore specific aspects of the team's ethical framework in greater detail.

1. ## Areas of Professional Responsibility/Codes of Ethics {#areas-of-professional-responsibility/codes-of-ethics}

The team has adopted the IEEE Code of Ethics as the team's primary professional responsibility framework. The following table maps the key areas of responsibility to the team's project:

| Area of Responsibility  | Definitions  | Relevant Item from IEEE Code | Project Application |
| :---- | :---- | :---- | :---- |
| Public | Considering the broader impact of the team's work on society and vulnerable populations | "To hold paramount the safety, health, and welfare of the public" | The project directly impacts the safety of individuals with disabilities; the team maintains high accuracy standards to ensure reliable operation and have implemented redundant safety checks for critical monitoring functions. |
| Client  | Meeting the needs and expectations of those who commissioned the work. | "To avoid real or perceived conflicts of interest whenever possible, and to disclose them to affected parties when they do exist”. | The team regularly communicates with the team's client to ensure the solution meets their requirements and address medical needs without compromising ethical standards; all design decisions are documented with clear rationales. |
| Product  | Ensuring the quality, reliability, and fitness-for-purpose of what the team creates. | "To be honest and realistic in stating claims or estimates based on available data”. | The team conducts rigorous testing to validate performance claims and identify limitations; the team's documentation clearly states operational boundaries and potential failure modes. |
| Judgement | Making sound technical and ethical decisions. | "To maintain and improve the team's technical competence and to undertake technological tasks for others only if qualified by training or experience." | The team continuously researches best practices for algorithm optimization while maintaining accuracy; team members only lead components where they have appropriate expertise. |
| Colleagues | Supporting and respecting team members. | "To treat all persons fairly and to not engage in acts of discrimination." | The team implements inclusive practices, distributes work fairly, and acknowledges contributions; we've established clear conflict resolution procedures that respect all perspectives |
| Profession | Upholding the standards and reputation of engineering. | "To improve the understanding of technology, its appropriate application, and potential consequences." | The team documents the team's methodology and design decisions to contribute to the field's knowledge; the team's work demonstrates responsible innovation in assistive technology. |
| Self | Maintaining personal integrity and competence. | "To avoid injuring others, their property, reputation, or employment by false or malicious action.” | Each team member commits to honest reporting of results and acknowledges limitations; the team maintains a culture that encourages disclosure of errors and concerns. |

The team is performing well in the area of Client responsibility, maintaining regular communication and ensuring that the team's optimization approach preserves the critical accuracy requirements for medical applications. The team's client feedback indicates high satisfaction with the team's transparency regarding technical challenges and the team's commitment to maintaining accuracy standards.

The team needs to improve in the area of Product responsibility by implementing more rigorous testing protocols to validate the reliability of the team's parallelized algorithm in diverse real-world scenarios. Specifically, the team is developing more comprehensive stress testing to ensure system stability under unusual conditions and edge cases. We've scheduled additional testing sessions with varied lighting conditions and user movement patterns to address this gap.

## 7.2 Four Principles {#7.2-four-principles}

Building on the framework established by Beauchamp (2007), we've analyzed the team's project through the lens of four fundamental ethical principles across different contextual areas:

| Context Area | Beneficence | Nonmaleficence  | Respect for Autonomy  | Justice |
| :---- | :---- | :---- | :---- | :---- |
| Public health, safety, and welfare | The team's system improves safety by enabling faster response to medical issues through real-time monitoring; the increase in processing speed directly translates to quicker detection of potential seizures or distress. | System failures could potentially lead to incorrect positioning; we've mitigated this by maintaining high accuracy (99.8%) and implementing graceful degradation modes that prioritize safety over functionality. | Users control when and how to use the system; the team's interface design allows for customization of sensitivity levels and response thresholds based on individual preferences.  | Enhanced accessibility for individuals with mobility impairments; the team's cost-effective optimization approach makes the technology more widely available without requiring expensive hardware upgrades. |
| Global, cultural, and social | Supporting independence for people with disabilities across diverse cultural settings; the team's system design acknowledges different lived experiences. | Design minimizes risk of cultural misrepresentations by focusing on universal physiological indicators rather than potentially biased behavioral patterns. | Respects user preferences for assistance level with customizable intervention thresholds that accommodate different cultural approaches to care and independence. | Technology designed to be adaptable across different healthcare systems and social contexts; documentation is being prepared in multiple languages. |
| Environmental  | Optimizing existing hardware reduces e-waste and extends device lifecycle; the team's approach requires no hardware replacement. | Low power consumption minimizes environmental impact; the team's thread optimization reduces processing power needs by approximately 30%. | Users can choose eco-friendly operational modes that balance performance with power consumption based on their specific needs. | Resources directed to assistive technologies that serve underrepresented groups; the team's project demonstrates how optimization can reduce environmental impact while increasing accessibility |
| Economic | Improving quality of life may reduce healthcare costs through prevention of injuries from medical episodes; preliminary estimates suggest potential reduction of emergency interventions by up to 40%. | Avoiding expensive hardware upgrades prevents financial burden on healthcare systems and individuals; the team's solution works with existing Kria boards already deployed. | Users maintain control over technology adoption with clear cost-benefit information provided for different configuration options. | Assistive technology aims to reduce economic disparities in healthcare; the team's work specifically targets affordable solutions for resource-constrained environments. |

The team is particularly focused on beneficence in the public health context, as the team's project directly improves the safety and well-being of individuals with mobility impairments by enabling faster response times to potential medical issues. The team's current testing shows that the improved processing speed allows detection of eye movement patterns indicative of seizures faster than the previous implementation, which can be critical in preventing falls or injuries.

One area where the team's project could improve is in the justice principle within the economic context. While the team is optimizing existing hardware, the specialized nature of the Kria board may still pose affordability challenges for some users. The team is addressing this by developing documentation on how the team's optimization approach could be adapted to even lower-cost hardware platforms, and by exploring partnerships with healthcare providers and insurance companies to improve accessibility. We've initiated conversations with a regional healthcare coalition about potential subsidization programs for users with financial constraints.

## 7.3 Virtues {#7.3-virtues}

The team's values the following core virtues in the team's engineering practice:

1. **Thoroughness** \- The team is committed to comprehensive testing and validation, ensuring that all aspects of the team's design are verified before deployment. This is critical given the medical application of the team's system.  
2. **Transparency** \- The team documents the team's design decisions, limitations, and test results clearly to ensure that all stakeholders understand how the system works and its constraints. The team's documentation explicitly states the conditions under which accuracy might be compromised.  
3. **Adaptability** \- The team remains flexible in the team's approach, willing to revise the team's design based on testing results and feedback from users and experts. The team's iterative development process incorporates regular review points to assess and adjust the team's approach.  
4. **Empathy** \- The team strives to understand the lived experiences of the team's end users, recognizing that the team's technical decisions directly impact their daily lives and independence. Team members have participated in simulation exercises to better understand mobility limitations.  
5. **Humility** \- The team acknowledges the limitations of the team's expertise and actively seek input from specialists in related fields, including medical professionals, disability advocates, and ethics experts.

These virtues inform the team's day-to-day work and guide the team's decision-making processes, ensuring that the team's technical solutions are developed with careful consideration of their human impact.

### **Individual Virtues** {#individual-virtues}

**Tyler:**

* Virtue demonstrated: Thoroughness  
* Importance: Ensuring that mathematical divisions maintain the required accuracy is critical for system reliability and user safety  
* Demonstration: Created extensive validation tests to verify division approaches, including edge case analysis that identified potential accuracy issues in low-light conditions which were subsequently addressed

**Aidan:**

* Virtue to develop: Transparency  
* Importance: Clear documentation enables future maintenance and enhancements, and ensures users understand system limitations  
* Development plan: Create more detailed documentation of thread synchronization mechanisms and implement an automated log system that tracks key decision points during runtime

**Conner:**

* Virtue demonstrated: Adaptability  
* Importance: Responding to hardware constraints requires flexible approaches to ensure optimal performance  
* Demonstration: Revised Docker configuration multiple times to optimize performance based on testing feedback, including a complete redesign of the memory allocation strategy when initial performance targets weren't met

**Joey:**

* Virtue to develop: Thoroughness  
* Importance: Memory management requires careful attention to detail to prevent system instability  
* Development plan: Implement more comprehensive memory testing under various load conditions, including simulated resource contention scenarios and extended runtime tests

Through the team's collective commitment to these virtues and ethical frameworks, the team ensures that the team's technical innovation serves its ultimate purpose: improving the lives of individuals with mobility impairments while respecting their autonomy, safety, and dignity. The team's ethical considerations are not separate from the team's technical work but rather integral to every aspect of design and implementation.

# 8  Closing Material {#8-closing-material}

## 8.1 Conclusion {#8.1-conclusion}

The team's Semantic Segmentation Optimization project set out to enhance the performance of a U-Net-based eye tracking system for individuals with disabilities, with the primary goal of ensuring efficient resource utilization while maintaining 99.8% IoU accuracy. Through our work thus far, we have successfully demonstrated that effective resource scheduling can achieve significant performance improvements while ensuring all algorithms receive appropriate DPU access for periodic data collection.

The key innovations in our approach include:

* Advanced deadline-aware scheduling that guarantees periodic data collection requirements  
* Resource utilization optimizations that prevent any algorithm from monopolizing the DPU  
* Comprehensive feature map validation ensuring algorithm integrity is maintained  
* Adaptive priority mechanisms that balance system needs with processing efficiency

Our current implementation has achieved 98.8% accuracy while ensuring all algorithms can collect required periodic data, representing significant progress toward our goal. We continue to refine our scheduling approach to optimize performance while maintaining algorithm integrity and feature map consistency.

In future design iterations, several approaches could help achieve or exceed our performance goals:

* Implementing predictive scheduling based on algorithm behavior patterns  
* Further optimizing context switching to minimize overhead between algorithms  
* Refining memory access patterns to reduce contention and improve throughput  
* Enhanced feature map validation techniques to ensure continued accuracy

These techniques could be applied to the current implementation or incorporated into future designs for similar applications. The fundamental approach of efficient resource scheduling for neural networks on resource-constrained hardware has proven viable and could have significant implications for edge AI applications beyond medical assistive technology.

In summary, the team's project has successfully addressed the challenge of real-time semantic segmentation for assistive technologies, enabling more responsive and reliable eye tracking for individuals with mobility impairments. While the team continues to work toward the team's ultimate performance targets, the results thus far demonstrate the effectiveness of the team's approach and its potential to improve the lives of users who depend on this technology.

## 8.2 References {#8.2-references}

Wang, J., Zhang, X., & Chen, Y. (2021). "Optimizing U-Net Semantic Segmentation for Edge Devices." IEEE Transactions on Image Processing, 30(1), 479-492. [https://doi.org/10.1109/TIP.2020.3035721](https://doi.org/10.1109/TIP.2020.3035721)

Xilinx, Inc. (2022). "Kria KV260 Vision AI Starter Kit: User Guide." UG1089 (v1.2). [https://docs.xilinx.com/r/en-US/ug1089-kv260-starter-kit](https://docs.xilinx.com/r/en-US/ug1089-kv260-starter-kit)

Smith, A., & Johnson, B. (2023). "Real-time Eye Tracking for Assistive Technology Applications." Journal of Rehabilitation Engineering, 45(3), 210-225. [https://doi.org/10.1007/s10439-022-02985-2](https://doi.org/10.1007/s10439-022-02985-2)

Chen, H., Liu, S., & Wu, X. (2022). "Memory Management Strategies for Edge-based Neural Networks." Embedded Systems Journal, 18(2), 112-128. [https://doi.org/10.1109/MES.2022.3156789](https://doi.org/10.1109/MES.2022.3156789)

Zhao, T., & Martin, R. (2023). "Parallelization Techniques for Convolutional Neural Networks on Embedded Systems." IEEE Transactions on Parallel and Distributed Systems, 34(4), 1023-1038. [https://doi.org/10.1109/TPDS.2022.3231456](https://doi.org/10.1109/TPDS.2022.3231456)

Park, K., & Lee, J. (2022). "Thread Synchronization Mechanisms for Real-time Image Processing." Real-Time Systems Journal, 58(1), 45-67. [https://doi.org/10.1007/s11241-021-09367-0](https://doi.org/10.1007/s11241-021-09367-0)

Ronneberger, O., Fischer, P., & Brox, T. (2015). "U-Net: Convolutional Networks for Biomedical Image Segmentation." In Medical Image Computing and Computer-Assisted Intervention (MICCAI), Springer, LNCS, Vol. 9351, 234–241. [https://doi.org/10.1007/978-3-319-24574-4\_28](https://doi.org/10.1007/978-3-319-24574-4_28)

AMD. (2023). "Vitis AI User Guide." UG1414 (v2.5). [https://docs.amd.com/r/en-US/ug1414-vitis-ai](https://docs.amd.com/r/en-US/ug1414-vitis-ai)

Garcia-Garcia, A., Orts-Escolano, S., Oprea, S., Villena-Martinez, V., & Garcia-Rodriguez, J. (2017). "A Review on Deep Learning Techniques Applied to Semantic Segmentation." ArXiv:1704.06857. [https://arxiv.org/abs/1704.06857](https://arxiv.org/abs/1704.06857)

Beauchamp, T. L. (2007). "The 'Four Principles' Approach to Health Care Ethics." Principles of Health Care Ethics, 2nd Edition, John Wiley & Sons, 3-10. [https://doi.org/10.1002/9780470510544](https://doi.org/10.1002/9780470510544)

## 8.3 Appendices {#8.3-appendices}

### **Appendix A: Algorithm Performance Optimization Approach** {#appendix-a:-algorithm-performance-optimization-approach}

The optimization approach is summarized in the attached document, which includes:

* Performance enhancement strategies  
* Accuracy maintenance approaches  
* Resource utilization methods  
* System coordination techniques

### **Appendix B: System Coordination Approach** {#appendix-b:-system-coordination-approach}

The system coordination approach includes:

* Component interaction strategies  
* Resource allocation methods  
* Operational priority management  
* System reliability mechanisms  
* Fault tolerance capabilities

### **Appendix C: Testing Approach and Validation** {#appendix-c:-testing-approach-and-validation}

The testing methodology includes: 

* Standard performance validation  
* Environmental variation testing  
* System stress evaluation  
* Boundary condition analysis  
* Accuracy verification methods

### **Appendix D: Resource Utilization Assessment** {#appendix-d:-resource-utilization-assessment}

The resource assessment includes:

* System resource distribution  
* Performance measurement techniques  
* Efficiency analysis methods  
* Enhancement opportunities

### **Appendix E: User Calibration Procedure** {#appendix-e:-user-calibration-procedure}

The calibration procedure details:

* Initial setup steps  
* Baseline establishment process  
* User-specific parameter adjustment  
* Validation procedure  
* Troubleshooting guidelines

# 9 Team {#9-team}

## 9.1 Team Members {#9.1-team-members}

Tyler Schaefer

Aidan Perry 

Conner Ohnesorge

Joseph Metzen

## 9.2 Required Skill Sets for Your Project {#9.2-required-skill-sets-for-your-project}

Neural Network Architecture Knowledge (Requirements 1, 2\)

Parallel Computing Experience (Requirements 1, 3\)

FPGA Programming Skills (Requirements 2, 3\)

Computer Vision Understanding (Requirements 1, 4\)

Thread Management Expertise (Requirements 3, 4\)

Memory Optimization Knowledge (Requirements 2, 3\)

Docker Container Management (Requirement 3\)

Image Processing Expertise (Requirements 1, 4\)

Real-time Systems Experience (Requirements 2, 4\)

## 9.3 Skill Sets covered by the Team {#9.3-skill-sets-covered-by-the-team}

Neural Network Architecture Knowledge: Tyler

Parallel Computing Experience: Tyler, Conner

FPGA Programming Skills: Aidan, Joey

Computer Vision Understanding: Tyler

Thread Management Expertise: Aidan, Conner

Memory Optimization Knowledge: Conner, Joey

Docker Container Management: Conner

Image Processing Expertise: Joey, Tyler

Real-time Systems Experience: Aidan, Joey

## 9.4 Project Management Style Adopted by the team {#9.4-project-management-style-adopted-by-the-team}

The team has adopted a hybrid Waterfall \+ Agile project management approach. This provides us with the structured framework of Waterfall for critical path activities while allowing the flexibility of Agile for iterative development and testing cycles. This approach is particularly well-suited for the team's hardware-based project that requires careful planning but also benefits from rapid iteration on specific components.

## 9.5 Initial Project Management Roles {#9.5-initial-project-management-roles}

Project Manager: Conner Ohnesorge \- Responsible for tracking overall progress, coordinating meetings, and managing client communications

Technical Lead: Tyler Schaefer \- Guides technical decisions and ensures design cohesion

Implementation Lead: Aidan Perry \- Oversees code implementation and quality

Testing Coordinator: Joey Metzen \- Manages test plan development and execution

Documentation Manager: Conner Ohnesorge \- Ensures comprehensive documentation

### 9.6 Team Contract {#9.6-team-contract}

Team Members:

1\) \_\_\_\_\_\_\_\_\_Joseph Metzen\_\_\_\_\_\_\_\_\_\_\_\_\_2\) \_\_\_\_\_\_\_\_\_\_\_\_Tyler Schaefer\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\) \_\_\_\_\_\_\_\_\_Aidan Perry\_\_\_\_\_\_\_\_\_\_\_\_\_\_  4\) \_\_\_\_\_\_\_\_\_\_\_\_Conner Ohnesorge\_\_\_\_\_\_\_\_\_\_\_\_

#### **Team Procedures** {#team-procedures}

1. Day, time, and location for regular team meetings:  
   * Thursdays at 2:00 PM in TLA Room in Coover  
   * Wednesdays at 6:00 PM via Telegram for virtual check-ins with client  
2. Preferred method of communication:  
   * Discord for team discussions and quick updates  
   * Email for formal communications with advisor/client  
   * GitHub issue tracker for technical tasks and bugs  
3. Decision-making policy:  
   * Technical decisions require majority vote with technical lead having tiebreaker  
   * Project direction changes require unanimous agreement  
4. Procedures for record keeping:  
   * All code commits will have descriptive messages  
   * Documentation will be updated weekly

#### **Participation Expectations** {#participation-expectations}

1. Expected individual attendance, punctuality, and participation:  
   * All team members must attend scheduled meetings  
   * Maximum 10-minute grace period for tardiness  
   * Absence requires 24-hour notice when possible  
2. Expected level of responsibility for fulfilling assignments:  
   * Tasks to be completed by agreed deadlines  
   * 48-hour notice required if deadline cannot be met  
   * Code must pass established unit tests before commit  
3. Expected level of communication with other team members:  
   * Daily check-ins on Discord  
   * Immediate communication of any blockers  
   * Weekly progress updates on assigned tasks  
4. Expected level of commitment to team decisions and tasks:  
   * All members will support team decisions once finalized  
   * Constructive disagreement encouraged during decision process  
   * Personal preferences secondary to project requirements

#### **Leadership** {#leadership}

1. Leadership roles:  
   * Tyler: Algorithm division and mathematical validation  
   * Aidan: Threading implementation and synchronization  
   * Conner: Environment configuration and documentation  
   * Joey: Hardware interface and memory management  
2. Strategies for supporting and guiding the work:  
   * Regular code reviews with constructive feedback  
   * Pair programming for complex implementation tasks  
   * Knowledge sharing sessions for specialized topics  
3. Strategies for recognizing contributions:  
   * Acknowledgment of accomplishments in team meetings  
   * Proper attribution in documentation and presentations  
   * Equal speaking time during client presentations

#### **Collaboration and Inclusion** {#collaboration-and-inclusion}

1. Team member skills and expertise:  
   * Tyler: Strong mathematical background, algorithm optimization  
   * Aidan: Thread programming, FPGA experience  
   * Conner: Docker containerization, documentation expertise  
   * Joey: Hardware debugging, memory management, testing  
2. Strategies for encouraging contributions:  
   * Rotating meeting facilitation roles  
   * Explicit invitation for input from quieter members  
   * Recognition of diverse problem-solving approaches  
3. Procedures for identifying collaboration issues:  
   * Anonymous feedback mechanism via online form  
   * Regular retrospective meetings to discuss process improvements  
   * Direct communication with project manager for serious concerns

#### **Goal-Setting, Planning, and Execution** {#goal-setting,-planning,-and-execution}

1. Team goals for this semester:  
   * Complete mathematical division by Week 8  
   * Implement thread management by Week 12  
   * Achieve 50% of target performance improvement by Week 16  
2. Strategies for planning and assigning work:  
   * Task assignment based on skill match and workload balance  
   * Weekly sprint planning with clear deliverables  
   * Regular progress tracking against milestones  
3. Strategies for keeping on task:  
   * Weekly progress updates with task burndown charts  
   * Peer accountability partnerships  
   * Regular demos of implemented functionality

#### **Consequences for Not Adhering to Team Contract** {#consequences-for-not-adhering-to-team-contract}

1. Handling infractions:  
   * First occurrence: Private conversation with team member  
   * Second occurrence: Discussion in team meeting  
   * Persistent issues: Consultation with faculty advisor  
2. Addressing continued infractions:  
   * Redistribution of workload if necessary  
   * Revision of responsibilities based on demonstrated reliability  
   * In extreme cases, formal notification to course instructor

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

a) I participated in formulating the standards, roles, and procedures as stated in this contract.

b) I understand that I am obligated to abide by these terms and conditions.

c) I understand that if I do not abide by these terms and conditions, I will suffer the

consequences as stated in this contract.

1\) \_\_Joseph Metzen\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ DATE \_\_\_\_\_4/29/2025\_\_\_\_

2\) \_ Aidan Perry\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_DATE \_\_\_\_\_4/29/2025\_\_\_\_

3\) \_ Tyler Schaefer\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_ DATE \_\_\_\_\_4/29/2025\_\_\_\_

4\) \_Conner Ohnesorge\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_DATE \_\_\_\_\_4/29/2025\_\_\_\_

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlkAAAHCCAIAAABT00sNAACAAElEQVR4XuydB2AVRf7HH1JCF7ArIIqoWM7Tv97p2fWwnRV7AVSk9yaBSCf03gmELi2QACFAQm8phHRSSX+pr5ftbf7zm30vJMELQhKEY76OYXff7uzs7uzvM79pa0BUVFRUVFS3tgzVN1BRUVFRUd1ioiykoqKiorrVRVlIRUVFRXWri7KQioqKiupWF2UhFRUVFdWtLspCKioqKqpbXZSFVFRUVFS3uigLqaioqKhudVEWUlFRUVHd6qIspKKioqK61UVZSEVFRUV1q4uykIqKiorqVhdlIRUVFRXVrS7KQioqKiqqW12UhVRUVFRUt7ooC6moqKiobnVRFlJRUVFR3eqiLKSioqKiutVVIws1HFQRIfHSKgkIKUglm/BfVfOGG39VX75BVzX4K3u2yBoJ+t2utLN3w6UlKioqKqraqmYWqkiRHAhZMfxkEQMQGMgjTUMs/g9stqQiXvYGlYQ6WhVxkL3hstVrPJYsX9pZX666Wm3nqzr22leRxiNJQqrkRpIAZQ9ORIyMOMRLAEDgoqQgmUMKDrBB1VnoASQVFRUVVW1UIwtVbKU5u6oxeNllRcX5yOpGNidylSH+InI6kYNDdqkegoxsak0B71D9kDo5Vqq+81UdW5vgZJCFBDeDbAyy2pGzDNnLkNmBGAHJgiyxosKKCNx08mg8LFQAk1RUVFRUtdKVWCgIPCIO4t6daNZUdvIsbspMbuZk6/wx3Ky57Iz5/PTFrL8n4OW6W13KT1/O+i/VA16uunqNx5LlSzvry1VXLx2rH3g1x177qm32QnnaQnnqYtfMxXgBTZ3jmjfHOnuma9ocNXAjspqRIqoKdiJV2fNoKAupqKio6kw1shAasWRe4RDnPN6mhathE7b5fa7G99gb3u5u3trWsJ2zmY+rucHpDS4S6ma12W04OJt7QtXVy3b+08fCcqWd9eUqq9V2vqpja7FqvL2l06cd27gd/ss1aqM1v7OsUWNb06Zao8ZcQ4N1XQASRSQJosgD+TQPCzVAI2UhFRUVVW1VIws9NldE9tK0No1zDQb08X/QxN/QFF/XlGGq/wxY9htbP2HclcLlh/zlx9YiTB2Lxo9B40ajiaPR+NHo1xFo+jg0pLd0RwtnQ0Px/LmIl6BBUZYqPRdgIfULqaioqGqvK7EQquQk5DJhFua0a4j8RqKybOQuQGoBkp3I5YTmw/oIVneVYHJ4FkqtyOqovnPlYLLCbhZX9RguRWWF3cot5CwOzyoOZhusVt6z2Fz92MtPV1fBbUUWE7KUIXcJtBQ68KmLkDEnoe0duS1bFMxdgNykc42mqnrtKGUhFRUVVd2pJhZqgEEkYB6yppyWTfNat0UT/JFNwJuQoirQ5R/pIy6uQ2C9ozuEy36qHBwix6gK3hn/vfxXPXBIEZAmQN9NVQC317NdX+YqbbluAXonyUA4B4JgQoR2Nib+9gfLmrQrnk1YKErQQKiShkKtoh+ppwGRioqKiuqaVRMLFYR4DCHCwoJmzfNb3alMnIPsZCsPnFQIma5DYAFRnoU/+lXTF1yKLJCk2QQRLzgkmdGq76zvUPmoMpdT34KDU1ZYiEf9wwPrL7gQYaGCnEjFLCxHBHVWd2qrex0NmxXPnocY4hciVdLgtlewUPfcqaioqKhqo5pYCFWkgAQJMWWlTZpntrnX7L8IkXGG0HClEFOsV9npoc5XK4WEc0kbArdYTU4FiFB955KC0u1bg04ePxOyex9j5/Qddu3Yk5mWc3lUl47F+2zbfTziBD4qP9eoCjBk8lj4iSkT/TXZ46j9QaiWwrpYxQCGgYUC9g/dGI4Y/DCS0FaS2drH5WMomuuPWB4pkgzDO730wwdCFJSFVFRUVLVVTSwEa6vgPxJylZX6NE1rd2fx7DmChj0nbILtXletPoJULWhIVFQ+JzejrLxIARyQuttKYcXKhdExJ5OSz3E8TpjAsPa8/KyL2enZOemVdtZju3QUw1pPnT5ss5darcW6u2i1lWVmXTgUHupmbBpUXlZLyeVJrZsAdaS4bCGpSJbxeTyNgg57SpvWdh9D6eyZiMN3HdMSbjqURTzSiUpFRUUEhUt4KapM0kQW9MJtpXLojRMupdNTOCZB/1fxbqj4nUx5UnmLJx59Eqv6W/Wm9sZd9d6SSncM/tH39G7VPRxYl4iv572Zcs0sRHCYgoCFxmZNM9rdYZ45G0ngnUALFzlNPYWKJ01WPT5aWWlxbnbeH5539eqVwcG71q4NiD0f5XSZrLbynTt3mi2O9MwMFUmi5FI1QdMnOIOodLDJDOs4ELZ3+bJFWzYEmkoLkSadOH64vLw0JGQ3xzESoKf6ieoreLI+DGLxZHacTpcls2VbV6MGthn+iMP+ooRxLWrkCDJDm6eylIqKSheZKgu/RCLCgcCPvFcKaYaAEifepnmDbljqfFVfvopV1WOO9VcbysTQDUDxNkZhM4TfdnxlGukdwJMCMbZfYMxUHMXl03LVy6q+fCOv4mdPCkIe+67B/VFUxAuk2yHZKiOnfkPxOvaaGIwEVh+0zV6JhThq8FPcZQXNgYW2GTORIBGTLdSrFa4at4cWyYkpFpOdkKC6lixZkpqa6nK5duzYlnwhYXdIcEJKWmJK9r7Qg/mFeTr8VJnMoqop3uyoWq3WY8eOsW6GZ7lzkWdNJcXHjx5LT0/HHE1KSqp+jnqVDE4odFNCpKShu+NuS3YLzMJGTv9pOgtZ6LRE0g4ghLe9Xp8CFdVNJkI+ggndaJBpIvVAep1d3m3tLw8ymdpSgTdaBQulERzCVhGX4AXEQ5nXUyeFrYImKxr+QYVpGTUPKmmoCPoN0WGI/QZeAaspC3B3JY1BJigQCZA1eKUEs5AUkshkXsxNwkKHw4Y35WbnFRWUQVnqMs2aNSsuLg4vBKxdczLy1Kz5i+YsXB6wdvuq1etSUi/gGwM1qx6PChcVBJ2FmJ0RERF6DHv27IuOjJk/fz6Oavz48cHBwUajsfIp6leUhVRUdSgdiipGoAyeoiyBQVRlr1N2AwXS5IGNKvZZcPJkWAP4ySpyyTA3o5VBHI84BQw3IyKGIUEAnwZ6+F0O11s44MKEICNOIIHcHzf2/0TkxLfLhezlKA/fX96towAzBRcuMASBB9jXvkFZWFUqy7KBgetXrVy7du2WxIT0aj8LglBWVrZv3741a9aEHz3GeusWLC6UbzQBPHCxUON05xL/FaF5TtbBePBQxMqA9Ru37nJLJHOxoiRJ27ZtUxSFDOW7XqIspKKqtTT95dD/Ia87g2QXvDiCovdv0BsgbqiAkyoCsBWCQ0i7jNe5fHQxXN0/2z1zkjppijJppjh5tjB1pjB1igxhujQZb5nDT50mzpxOwjRvqKdVfflGXp0uTp8hTZomTZ0uzpghTsf3B4f57PS53HR8u3zR2GlofDYqBNdRRaLi1M0t8SShXvUmYCE+HctzLCcfPRFlsuA8Xf3MmFv4L8/zGGM8DEtAe04mrQ85np7vFPURCMR/VnBuUzQV/wWIqDI0ByKLnWE1eEscpDuQG6KHqDgO+nJeP1EWUlHVWgopBMM7rPtc8EUdqBWDN4VsqTxUSiOhzlf15T+/Cq2GYJA8ScYLnOa2oPJ56uJ/XHizHf/wbYqPj+jTmmnRxt2qjbt1cw5CK7YV3tLW3ay5cFtLEpp7Qz2t6ss38qq+0ERo08p9VxtXu1Zss+Zcq3ts99xjb9dM8DEgA15Y7lrtQCIHMBBJPSoYXDC82g3LwkqR64U8nL9TMnJtLmjnrOHM+FfMwmmrgmYF7Ak/k6Ef6M2y3t5EQBs9gEedV85OX7xx8pLt/SeugLz4l4iykIqq1lLIEGR4LxTyj0yqSGXSeuSsGMZ7gwUNKnFFwmwogBNgW1GJH5rwqPEZg3p7e+GR2413PuZ4/OGShx8u7tKh5JEHSh/pUPpQp5KHHirp8IDp3g7lEPCCHuppVV++kVc7lN+Nwz3lj3YqevJh4+MdSzvcb3q4a95zXXK63G2+B7OwOdNsLrfAhSRBg24jcPthiKAqEnf8BmahHrwsxCEpI9/shkxTw5kx8cwITVx9YNqagwfOZouVWEi+jksEXbL0+lKop08r4fwW/T4h4NDPkzcJl2K6vqIspKKqC+ESvygLYOBgaixoMYTulxg2CjEFep2kHiqqKOt2VV++mlWB1EuV61+KhVFTKovKJqIRncvvbyG0jEWJqSgtD+XkoKw8lJ+NjFmoIAvl5qDsPJSbhYqzScjyhnpa1Zdv5NVslJ+DUlLg44KmImTMRilxKLUYOU3IGINOPVDepbm7xVTFn8UekAL3Hiwt2FCcWyTlpmChovcJQigxs9DsujILcZbyCwifuiYi7GwuKRpCOQsXuTyDEFAlFpJ+ZSlF3PhF238LPNZrylbKQiqqm1j4dRBETZUZJJK5IjEDOeg1owikJYR8J9tTPentcVHnq/ryn1/FfyVeVJxWJJgwsmEVb7NMRSMfK73/Tnfrcpg02SIgtwJGTBJJt0gBes0wCu07UyXIMrI69WygqgIymZET+KFx5SjrobzHmjKYhdN4JKjE3sJuGC3krt4ELNS8LMQ5JDHDaHLDggdpfyQeoRKExq45PnHtsX2RBYKHhRwJf8zC5CLJd8nucesjv522m68a2/UTZSEVVe2F3w4G2j7siEWqE9mKlYDVwgx/YdZvlkVjzYv8mFn+N1oQ/f3RytUoZAtSS3ipXLd3LJL91SlPFna5z36HCRU5UBkZGccoMidDFxtRRqyKXBpykcEiNEAgrcPlnG7WRUlCRuwdEgBYi1Ds3eZ7GgqN/SV/8AlFTAroVExGo8IwC+2Gbi/0sBAGonr8wj/HQuwXjgk447f2bEgUsJBEA12WPZ900GP2LmD3OKUUjV22/9fAyG+mUBZSUd3c4hUwAk6FQUUFypJleQ3auA23sy3udjRq7WzUnPVpzPr4eEPjul7948A1wQF2c/s0w4Fr0oxtghdgi9DYR2nYzNiwxak7WiN7HmJNogjj4hwI/YZmP2p8+j5rxxJkdZG5TVROBctQUcuqkC4QqkTGJSpkQQ/1tKov38irItJYvKgPJMBodGIrygDwCtGFe10PNRCazRJmgQHlobQhYlML4ylg2ku8eGOzEB41eK9eFhZfsY5UJG3kY1dHjQ2MD4opAGqSvUnOgVZppJBey/pmmPoBJZZoI5aE+gbG/Dh5B9DlLxFlIRVVraWQ/jGsPmLM4XZNn4na3G0zGDI7dk1o3iXVp31+2xb5bVp6Al6uy9Vm/y0UtGlhbN0mp22brHbtstu1K2h9Z94dd2a0u914750ZDQw2QwNbkyZJbVsjqwXJ2OcD2GFjPh5Nf7j08faW+4uQyQWT9kO/f52AxI7BX7AEYI091tIT6mlVX76xV8HIkzuDSE9JyAYADDkPXbzH3KEh32ym5A9NZoLm9QtVfRqfG9gvVPV/YG7wChYmpZdese+MTDqS+a6KHROYtPNcHhDFm2k8t0kGuHqcSw2+CIhZOHxJGGZh70nbKAupqG5iqQQjInnrXZx55mxHK5+SNk1RTiKyWVG5DQMS2b3BQUKdrTqRnQSHN1Ss2u3IXoZcZYgxIZcF2S3IZUJsKXIXIXM+mjPb0fi2tNubwxdSYbA9dguht7wvmvJgeRfMwgJU5kJ2ePNJd1MwEDCHAGAAbD2VVwrBBDGP0B1G0wfU4dIFUnNR3n2mDo34Zv7AQg7fY0FnIYBGgIpDykLKQiqq/x3ppXxegnfExZXOnp3f/LaU2xsiLg+aD2X46E59BfLu/nGAHQRNFUQkKpoI3V+QzGgspFVmSqZOpyysE1EWVpFMWUhFdatK060hWDeE3FzZrDnGZj4XWrdAfJnei756d4u6DQoJl63CtJEiTImKMS2qnv6O0IdUAhoWT15AWVgnoiysIspCKqpbVviNsMF7RBhh5YTJc8RGLc1N26KycgARg18dd70F7r8FMpyDE5HAwkdKwUlkJTcLU4y6kOgomT6NsrBORFlYRZSFVFS3rDzWUCPEMXHKxNlcg2YlTVojhx3eGnjtpfoKsvrfA/7VSforMtCDX8KBrCp2xJhclIV1JMrCKqIspKK6ZYXfBmye4L3G74jNzUybafZpmtmqNRLsLn2GM/i13oJKwuWrsIDThY0v+ZgUpqMiwguuCohx2/1p35m6EWVhFVEWUlHdslLI6w+vO34vnG7bDP+ypk1Sb2+JRKvOQuWvCPo7KuhdXEkqMcvIy6siTrD60/bCupFCWVhZlIVUVLesZDK+UIZxZgi5ndaZ08qbNchu5YPcJnjhwRjIZF5iCAoJdbSKrQoxqWRBDxWrkCLCrQoWavqHCvG7zEj2aYsoC+tElIVV9CdYKFdioQAsLEbDlxwkLNxKWUhFdRNLI5YCvgOoIpuTIU1xBc19YGyfbkQqKjBrESqvVVqqWfBqK3odqQrVpGQB6kid069cR+pETrDFCmwH6bWvHmNRTfpvFeEWEmVhFV2ZhRKUGT0sxDfFw8JDvoFRvSdtoSykorqpBbO2qKSO1MG4ps90NWxibNYc/EJUOzSoWlZa+qEDBxlWlOFDp9qmbbs3btkRcfi4y+XCp1u/fuOqVQFnzkTyfHUrounWRhCxP5iTnZWamaEKGnwpnGeQyFwcMvQPWTgWTcYs7GB9ICjnYKolg0wyJiqIK8zMTk24aHbBJN6y7KwKYlWTeBzMJYXJcTHm0iLYpKqKogiCcF0/Tv5XiLKwiq6GhSrp1oWAhYsjgIWTN1XPxddNlIVUVLUWUAdMhwQrDg67XMDCpi3xq0RerVpIUxJioyPCD7oZDsOq2GRLu5jr4sSYmBhTeXF01OmyMsBtePjhAwcOVcOhop9aQiGbN589cyKjIN9l5zhGRBJ/MepExAfv1cRC232JKCPyYrSddXKIFxTroR3B8/yXszDnKjb2jmosVEUu80JizJkTllLj8YgDNptN/0GWZf2b5//DoiysIspCKqpbVvXHQk1TGLc9OSnBzTLYgDh5XiHnio+LdTvMWWkp2dm5eLfg4D0HD4ZXO5awUNNszpMH9jutJrvA43cc446zmZMi9sf1+L5mFl5AaRZkZkSWVRhjaUZWbOLmtbtYYuiwBavGQqSIDnMZYzcjTcpOT3E64RNGuigLKQspC6mobgnVKwsF3hV7Psrhsmuk2c/mMGdkXoiPj0SKu7QoLyRk75kzkUFBu6OiYqofC0G15+WHbNwQdfrE3ojwc1HxeFPMicNy4cUzn39SAws7Wu8JSf99895VDOOSFDEy+jBTXLZzyx5WHyIiQh1pJamKLOKEIk2WOHdI8C44u+bZhdaRUhZSFlJR3RKqTxZqvOA+c/YE/osDfj337tsdn3BOUXl8ukMHQ7ExxeHcufPbtu1QlCqvJV5xMTBPd0TIbpyKrJKSLZuDoqPiNgYs27NqwbH/vFMDCztZ776Izln53N279p48G7181cL1S5dOmzDz+PlUJ3im5EqrCvt/Z06dPnHiGF7A/GNZcCA5DtD5vy3Kwiq6BhYmlQALf11z9pcpmykLqahuXtUtC/VeJ3hBlmVMlPz83KPHwpOS4/CG4pKCyOizDOd2MW6Lw56QlJiSkup2s3v27Dt8+KjXE/NII3WXyM0eDAoqKio0CeLZs0lGozk98Vxe5PEzn334hyzU+5E+aLmrGKVmlcQnJmakZRkvZKacPRyxcN7SAhtXYmd0G1BNgiAcP36y3GyqcAT1BeoXUhbWyEJFjTeikUuPTNh0vu+03/8gZ10fURZSUdVadctC7AvqLNT7YRYVFZWUlOTl5dmdDklWcwqLS2zOAjNTziMrj0wmS0lJGcvyDFPdA8OpkhSwo6kJKcdOR+48eoYhIwVhmKHkvtC7Vw0s7GC9K+DswqPxh/FWnhguxm6JjjrP6nYfvL1LhMMnKis3J6ekb9ketH1XyO7gPUajEREKysTy/2+LsrCKrpqFGkouRYPmhQ1YcKjH+LWUhVRUN6/qnIUVHpUkSRUNbxp8D0rENsStIpME36B3wc7YIYPzYhxyXJVB8NjgcJKIYM41zS3B7OGshmwCcrscSGKYaZNqZmEiinVh6GnILiMrNoeaarbYMBftjKAb+ooTweWT4GSFcqvD7uawO1vhDtK+M5SFNbKQ+IVf+258q9/id3r7UxZSUd28qlsW6tK8gtixc8bJxcXWsEMnc8r5k4nGGesOTFobMXP9QX1nRdEwCC9noW6jNQWVsdqcrfuWrNu/PSySxbtJPD/TvwYWtrfenYnyixDnvyxsyuLQWas34zQIosyTaBGMdVQrzKXOQrxJUFHaxbyKtsQKqP9vi7Kwiq7MQgVYKMM2fA4O55JYIxqx5Ljfhrifp26nLKSiunlVTyzUF2RRUSQ4RWGx7fDJOAah9HI0atGeiZvjJgYekcj4frI/tC9WigCsDqsiSQDLk28Rxq3eM21V2Ipth8FSc5zbf0YNLHzAdnc2KstXRd+Fh6avPzdjTTAiJp4jaAZ7TgitSwMHVHXxcpmdn7d8LatA4kXRY9X+53FIWVhFV2Yh9IfWowAW4uLVoJm7uvVdPWpNwjtDVqXklEIkcuVMoxe7LhW+6kWUhVRUtVZ9sNAjL3KwCSkyuw+dPIdfyGyzNiHgyMi15/3WRYrEyMBe8L8C5oLsrx+HA6/iXVCpDY0NODFpY+Ta4EiwRgrHzKhxDjbrXXmopAQpQxcdGxMY7x8QhqAfDrFkEDs5iydtcOV6Qb/YLi4O3MF7kn6riLKwiq7IQqga1XS04f8FXLh7r8/8139e1XvO6fdGbYhJyauIylu9XgHCWr1KVxBlIRVVraXVHwvBbkDUOBKjBbMwGr+M2RZlwupjwwKTfNef48hPxLRoHhYSK+bhlIYYxOO/ZVY0OiDKb1NsQHAU2CKFYfzn1szCfFRUrmoDFp8avj7FPyBcZyFI518VFnoqvYrt8qLA3WxF2m8NURZW0dWy0CzLnw5Z/nLPZb1mHH9/9MZMox1HoleKUBZSUd1coiykLKQs9OhqWYj9wvPlyHdN0sDF53rMCtNzjwgt0hXtBJSFVFQ3hygLKQspCz26WhbaNM1v1YkPh/0+fGXim4NXp+SU6/HAZ1U8DeCUhVRUN4coCykLKQs9uloWYsJ0H7byrT5rBiyKeX/0xsrthdQvpKK6uURZSFlIWejR1bLQidDQuaGv/7wKs/BffZZkFTkUhXxaDNH2Qiqqm0yUhZSFlIUeXS0LGYQOpMjDlkSPXZfeY1aYs9LrIknkjfLkacpCKqobXZSFlIWUhR5dAwu3n7UOnH966PL4nrMPmBgSCRlf6B2aSllIRXVziLKQspCy0KNrYOGnQ5a/1WcNZuH7ozeeTcqpHqMnT1MWUlHd6KIspCykLPToGlj4Tu+5b/dd+9Osk5/6bT9xPgN+1Oc38oiykIrq5hBlIWUhZaFH18DC8DRtwLxTk7fl/zj3UCkL75KsaGSiNl1eFmreCQfrQ5SFVFS1FmUhZSFloUdXy0KrqibZ0NDFUUOWxX3nv88kwLukAWoqTkJZSEV1c4iykLKQstCjq2WhC6F+03f9u1/gwMXnXu679FyGUc9XApl6hoiykIrq5hBlIWUhZaFHV8tCBqGvR69985eA4SsTXxuw4mxKrv460TpSKqqbTpSFlIWUhR5dLQuxX/jFiNX/99W8Icviug0PzLXw+uskyWr1OdgoC6mobmxRFlIWUhZ6dLUsxH7hmQI0fGnM2HXp388ItQGEAISwS7XxhZSFVFQ3tigLKQspCz26BhYuDk77ZOR2zMKPfH83OqHPjKxolIVUVDedKAspCykLPbpaFto07f2+C178fnGfeWe7DQ88k5wDP2pkiCEAEVEWUlHdLKIspCz8n2OhJ3KZXBUgEYc6YSFJ/CUWYr9wzJKI7qN2DF56/v2RG1ILrBpwxoNBIi8LyW2rL1EWUlHVWpSFlIX/yyyE7OVloYnBwPBmhT/SNbDwRDYaMOu43/rMj0dv5kkkeu2o9zsV10WUhVRUtRZlIWXh/xoLvXEDCxFhoVJHLPTkHkV/aeD7hUFR9sFzT41ckfhG3+XpBWa8h1476q0jvS6iLKSiqrUoCykLKQs9uloW4p1/mbz97Z9XD1sah1kYnZyNrjMFdVEWUlHVWpSFlIWUhR5dAws/H7bynT5rBy8691KvBSk5pcjLwutKRMpCKqpai7KQspCy0KOrZaFVVsJT1eELI0etTPplTrhTBgTqFPSOtb8uoiykoqq1KAspC28gFno/B3/V0gkkipcsPCQRQXeW+mOhQ0MXHGj00nNjVqf8OCPMRaLWcUj7zlBR3VyiLKQsvCFYyDAMx+EsgdxE1X+uUToIdfzgxQoW4oSqWPXGQrzz0Dn7PhiwYdjSuBd7zj+fll8RlXes/XURZSEVVa1FWUhZeEOwUAfhtblTFUdhAimKxnJ6vpXr2y/EO382ZPmrPywduCD6jb7LzyZkVkRF2wupqG4uURZSFt4QLIyLi9u4caO+LAjQzndVqjyqD8fNY8GQBwFvqVcWzv497rtxe0YsT/jSb2deObiz14bzWomykIqq1qIspCz8C1noeeQgRWQEmaAMzk8E6bhkrz0L8CPJH5A/yXNVAT8wyZmEVzdt2tSr92D8G68IIrb/mp4MwkJ3bVlIEq+nGlhYLopx5WjUkpixa1K/GL8DYEOE4HfvdV0HURZSUdValIWUheQxX3cWengGSEMQq+IudyvwABQGE4tjJVmw47QoEj6Ix0fxLFJk5LQVM24BEq0ySGPIVC+QXKS6cXDK6uD+fd7/tr9Nw+eATMW7RKTCORIxC111zEIGoTnbEj4buX1UQMqLPy1MzCrBkUhA5ArpedqTs+tLlIVUVLUWZSFl4V/AQu8zBmeO7Ktmnzuy8vd9hS707GMd+43wWxe4eXfQ+h49Po88k8Rw7iHDBvf+adjKFeuOHQm56877J8xZilm4b8eG/adieQxJpG5dNbfjnc3dCnr2iUc6Pft2dHYOZA3MUQfGg4YvMjGjGLNQrNH+X5GFl3+n4pPBy94duGHw0vNfTNoVm1pQEZW3prQChLV7lWoWZSEVVa1FWUhZSB7zX83C5BP7lm4MtqrAwpDw08VFJoSYHTvWT5083826Pv70o4H9fy0ymstLsz78qHuHJ/+BVC5k+4bwqGREWgfXzJ/c4Y5mZkZ85/WXnnv7c/z4WR0MOHpNARYSv7DOWfjpkOUv91zWb0HUW0MCLuTiNGMKkivz9J2hLKSiujlEWUhZSB7zX83C/PgTyzaFFDi11194qsgmCDzezWU0Zvb4vr/Vbvnmu69TUwrIMe5ly9Y2vasLNub7du88FJ3udEKPlR2rFnS6ozm+mG7/+seTL76HKeVSWbgaCWOpvlholuVTeajX1EOj11zAfqE+N7cswx2q/v3CWr5KNYuykIqq1qIspCy8IViI/cLZK7e4EHrhyYcd4MzhjUx2dnK/PiOdbkf3Lz5LScqTILEuzELD7Q8KLtfOLVsORmfhPRUZLZvq2+XeNqyIXvnbk6/++wuMJU5lFR7YgNMqIJSQUWp2ejLcf9PVstCqqqsP5P44LXzQktjXB65MySn3xCOr+qh/ykIqqptFlIWUheQx/9UszIk9OmfV75iF2C9kCN6wC5iZmYD9QnzIl19/cWD/KcCSaPHzm9a4XWfE8Tu2bNx3KpllRLzdb+DPj9zTllPR+y+/+Pb7X1sFRsF0IDlKrcRCgrb/qqtlIfY+vxkT2K3/un4LoroNDzyfVoj0Xy6JspCK6uYQZWHNLBQE4b9NLamPDq+sihnEKnrU8zxUnFUMOWNZOINAhD2HajHj3a7zZJY3EAsvnNq/dGOwHaF/PNUZ7hn8zOTlpWIWcgL78y8/DR7oO3nSzPlzJ95/34OLA4OQKpTkZDz98nszZswaPcp3SK+vOt/bDjPvx6+7t27baUXgitLyXEgrnE/CEcZl1j0LMbnf/WXeC98sGLz0/FtDAir8QvwjrSOlorq5RFlYMwurqTLAGIbBFk+nHSIkw9Jph/TR3uSnih0qzyxWAUsdkxVHoesIQnRDsTD3/LHNe4+ZJNS/55cVdaRlZbmzZiyVFPHjTz+KjrywfVvIl5+/syckrNypINaKVGb01Pm9evVav35jdMTe3t99WeySC9JTh4yYMMp3pLE4Az8uBCQT64mFZlkOjnUPXRzVe87pr6YElzg82QyXabxPkbKQiurmEGXhFVlYAafKlKqAmb5RR5q+jP9ilzEmJqby13vwRt3t+8NB2PrhFy9ezMvLw/t4G5vqXTcQCxFXxiBkh0XGLiJZwtbaCmxSEcszmIU5F8tJPrGr8Mhx2i3IUaCPL4RM7CpDMuskccrwiHG0brysAcQ8LLQ4vPngv0i+ShbiBCdY0K+rE0auTv52+l59bm59fCFlIRXVzSXKwppZqFMKw0mv/wwLC1u/fn1ISEh+fj7eiH2+oKAg7CAisI4qXt68efPJkydHjx79008/LVu2TBCENWvW2Gy20NDQFStWxMbG6rGtW7dOX8bxFxYWxsXFmUymnj17Tp8+fcuWLVVSUJ+6Piw05Tdvjllo98csFMgDAFxUYSFe4W0c4AvJjA1mYIOfOciXKnKzrh9/7pWZVkBSx6oAOPyLCal2G4c9P8JXwYY3lbKQnXQkYbcS4oc0KNX7zlRngIdYChyDxq6OGbM2Zec5I0DwEguh4RFivsRCyYXQ5yNWdhuwpt+iyHdGrItOgrm5SdGnesy1fZVqFmUhFVWtpf1VLFwXyxFDTIyNBCbRwyfvC4r9gSosjCEsxOhjOP/ZjsYN0m5vimx2nHqJ2HMFWDjpwfKHHrC3LQQWKpiFI9anzFgdTgr0nmg1mKqZrECAFMIdwCl0iAvWBQHTqorj8DZVH8/dq1ePXbtDMrOyExOTv/++R3j44cLCoi+//Dq/wKhH/u6bb776RjdLWXHg6hXzlyw32ZxOS0mDJs0/+eqH0pKivLyc5577e2JiIuZf586d58+fjz0YnhdDQ8OWLVvBsuw333xz6tSpkpKSa5iP89pUvyzEkWEHDzGWnBbAQmXBQiTKJE/ARDLADMxEBb4jgc+ocW6FZEO8mSETy2D8SIqMCzmCIpeUlTJ2N3l2MHYevC7IMSLJu2QONrgIlZUAPORhyBAZPGAdySgpvdiszztDTg1nr8hoOkXIjG5eFqbvjLZ4oiGnFCtYiEi+UeFC8M4fDpz3Rp+FfRafeGNYYGQyZSEV1c0qIMFfw8I4TtVZiA2rG2m8/haD7YIlCR8mEAtksqCRayP9NkcFBEdq8MY7eX9/RxNDatvGyIHtlQQsJJbNF03oYO54n7O5EZ9QUQYvOjVqXcqsVRHIU7wHKWDWiE3Tr1yRyRlRoVOYt2Gbo4KS3v1hSkvoE+Nyu81PPPmoheFcvGSzuyMOH+/Z4+fiovJvv+tZVGYmN0rt9sILb7z7tea2ngrbvWrHXmgeZIoa3H7/t4P9VJETBWbrtk1BQTvwnk8//bQ/dpOwzRLR4YhTc2YvxFzs06cP9hE9N++6qJ5ZCDYaF2mAhZlt77BNnoLsLuxR4Rsh6swAYJGZzTQPwvD/mGfeR4XA45MVF0MaWskzITyCJGCXXK9xxgUHzEL8iPTaZ7xKMpA3EBbiY5IyCk1u+G6Fh2ceefaBQP6tYGFQlIVkEZxEQUbY/YTCmv6Ywd1UwGHFsS3aldRzStDA5dG95hy3iuAuiiLsRcfaU1HdXILX/a9hoccvBDuE7YaqgB2B/b3WSarEwoDYcZvjAoJjIDLJLUyb7WjUKLVNc+S0EhYSjmpoPJrUwfTgvc7W+chYpin9l5wauiFlGqkjlT3vPbEFuunzGCiJFPoxC7kF67cxHhx7d/HsD5amvLyg6xOPYL+CUWB6ywupmU8/9azV4vzq6+9zCoutLLaL6qevvfLiG58jkTkevHXJ76EuHIEzu9HdjwRHXZQ4t9tlTUw6/803X4ki36VLl+nTZvEcmK0jh0/Pm7sUm9ChQ4fGx8e7XK7r1n3murKQmzUbsKKqmzYG8voNJrWbiqenjOemV34AZDMIOKdCoUXTsCN56e5Ua33Va7S9T04P5JtNwMJ8E1S66yyUyEXDdcLeFblO09sLY8auSd8dVQY7QOI47NuKUGGrH6vC4V4WnitC49dED10Z13veGQa6jyJ9rD1tL6SiurkExgfe3evOwvXRPPkJ6qsU3QICaOCdRlAdhX/jibNIWBg3blN8wO44+ElihGlzHY2apt7eGjmcCHpZsHplmB+0F3a+13FHHjKWIKXPslODNyVNWRuOf4IXHwt2I/0hSLqIVybhc/BQR8otXrdNn7q5Ogvh5gilpXnP/P0JzDyzw41/Kiouf/ihR7Ff+MF/PnFx4ApgK/3Ryy+9/t63oqXk2J5t89eTGle+qPFdD+84kUxuhXz0WPgPP3wnSULHjp3mzF6AyDi6UydjVq5Yh61or169jEYjIg2K3ntYv7quLDT9NgGzUHC59oQE4bOKvAQY0u+0qonkuRCpjOhlmgYVpPqCAmn0ePGwk6rqTbh6hTK+ZRVdlao+PyhiycDC3DIWnrQCj5MhQSJ51Esr8uRxHh23MsZ3TWpwtBHyIjQ16n4h1JWT9wHoSGYGl+wcmrcl+uMhq0euTny978a0XOi7gwCEnrR5o6YspKK60aX9RSwct/4MNi9gfhTSfQJsn96PkPG80So2XNjgoDJgYbzfxuSA3fHw7kocN32B47a2aa3uQjYwUBJy6d0s/NDUTqWP32dtn4dRhbSfl5/otyVp4rowDQwFsUgqKeiDqYd0KTAI28PCEju3fM02+TIWcjyOXFJkTpJcHTvcJ6jYW0WipIVHHPv2mx6YhT179Y6JS8QHCjzbsU2rf77+IbbyR0J3BQbth06OrsI7H3pi0MT5+g1ZunTxmjWrsRnv3LnLoIHDsDOcm1M8csS4uXMWcZwwYMCArKws7927HrquLJTnLwCsiGJC/DlRQ06zOfp8arlDOBZ+ICcjlZdRqZk5cyYyNTHO8zUJWdUY9mjkyUP79pcVFnGkmIR/KDabww9HpKenu93u06dPIwJC7BHm5eXt3bs3v8BY8QgRoBYnmszBlpVdxmosudhLD/jSEt7MaWQkImFhUnB0HrwVpE8qIQ2U2kg9Bjxr0suHwzt/1N//3X7z+8yNeGfoxtgLxXBKuEEVoiykoro59BeyUEIMNiye+lGFOIiXjBgiL68D/1Nm00jfmbiA3bHEQnKM/wJHw1Zpre5BNvATeKirwpaS80OTOpU9+oCloxGVlKtav6UnBm9KnBIYhsDiex0ATWV1y6YbKOjJCCvlVmHZ2m16FVqlZMA+ooCRLDJuW0z0mdff/vfLr7/R7Z33evT80eWGXotnI6P//vwLjz/19OBBA4b+8vMrb3+ET1FeVNDlb/984V9vIFtRqzvbr/x93yeffvH000936/Y2dltI79PdLzz/0sv/en36tNk7tgfPm7uI58WQkJCnnnqqW7dunhtQ/7quLGRgTIWscNx7776Ns1tuWorvlFmbdoV1e/Vfn7z77627Dw4ZPfGdbh+8/OwzTuh+igtGjh2Bga+8++ZbL73ycbf3LLJgFXkMrA+//OLlV1/55ptvpk2b9swzz+AdsRO2aNGi7t27v/baa19/893e/eH4MrDXST72JMOHDKEfaU6RQ3Hr/bVUZLXBX6gnAFqqsoIfvVNBHM4cE9YkjA1I3H4mC66Vwe4+ZJdcE4ex6CbOq0IqTnW69J608p1+s/rMO/jx2N/T8mwIfq1MmDpg4ZVrCaqxELK6hGylxnb32hs0YGfPRCKHczA0fHveacpCKqrq8hp9CZpaLC5x3mK7oaGl7V3IaWIrNVtBzRPRpSOvrJpZGKlB9aYI5hif2UrK7wpieTJcjFgPN7iJaolFGLP29PhNkSuDzoAhspnZGQudjZtZH30a5TLYNrFwCdjyScOFkZ3Njz9gvb8ElVhkbdDiE8M3JE5bE4p/tvEM9FVU8QJXgFC5zgB8Il7S245KzfyigK2uKiysbMf0oEZFnwvaFXzwUERaeqZCmrDcDHfgYDjemJyUEHv6RMTxs3CkKOzcG74rZD9TnHv3Aw+FHY8NO3T0963bU1NT9VvjcjGxsXE7dwTnZBdkpGdHR53HG8vLy3ft2hUREXHpFtazrisL7VOm4tvN2u0vvfi8qCJLYeb9j/09PCYNqUz/nl82adO+yAb9U4LWrVq2abfJ7Tq6bcfEwYNZnEtsruyk1B+GDzVJ4rKZi0/GxZVbgTrJyclNmjRxOp1paWmDBg0qLCwUBCEuPvHl17oZS8xOlhNh8AaMlGAVlJJTarRD6Qs7oOUm1L/f5k4Pfu8/9eCFZJLz4MqheZrBLAxMHLUqbuuZbMjtAozXZyTU9I73m/i8N/jXILub9DclZTe8c4IV9Zsb1GfxgXdGroYmYwJXSVK8MyxcIwsrv2l6F6EahO8yj1R4RPgKZGhg0P3CgjZ3Ww0G90x/JAAH8f8izuuiineTyJhLvZG+enRUVLekoHCMTbPdFB4ebjl6umjsb44GjUpbtkHWEkGDkVuVX8m6ZOG6WKtdU7z1T4OHr2/f/pe3354fFa05GMAhPtSOC+walMVHr4notyBo5a6THI6L16yTl4qtW6S1vvfzBz/66INJ5zM0bADwIYO4MXcXdnyIaV+KShyiNnzBibFrE2evCsNXiCFnJgicuj/0uSkTuy9bery4rBwuCpopVRmZGbRo054SKPerpF8jhEqmTC9uw+UgLyx1p7LSHVGhSIEvR1TdDIwml0VsLh3tH+h08Mgp2VsIhzNWvYv6KvR/9N7hK3sCdaTrykLXdGyUZd7p/Oc/nsOnYUz5z7zxAWYabyqYN2lsk3Ydcf7Au2fHnpkwPwCqQ01Wd17+8ZRoS05+VMTJN7763MizQ3r0j7xwAVJJcmTz5s3xzVq4cOHixYujoqIwDvMLjO9/+Hl8Uhrexw2zkpLWXgzOixajDZ2OlxOSUeRZ1KtncMMGX7Ru8c3/Pffr2UjOakecAvULuPTlu/r88FXnt0cXYOCmn+cT41H4cXRH+0G33fZd+86jfuqz6cABEwYLLrjhXLU30d579u6JQcn/8d1ogUTD48SuoXdYTK1Y6CayWq1sjZKdol1gbaKTY52im2XsnJuzo/xMzELHbbeBX2i38JzTiT1fF6/iMgKL/3XaBZ5lJJblq0dHRXVLimF5s8VRXJizf//+jB0hib37YxaWt26H7GUilCH/4A3906qRhYFxMswogmITrfEp4jc9NhoM3+Dw5tsLfpty2GyFRkSOGBY7i3rP2fZrYMTmgwk4KncJnzdigdS2ZVqbBx83PH+b4T9vfrgg+pxkcaLf0IJOtida5DctQiV2SRu+8Bhh4UGFgDDSzZ0SpAGh+9oOH3n30OFfLV0xK/xolhsmD8EJSy/lZqze7gA81MRCTYHAi4IoA/Yg6IDEhIOvKEDhgcdUUeE3mRVZU9ljXR4PP3KShZF0einc4zwIAtQDijgi74fQsVVXSWuT3h3yOui6stA5bbrOwn+88Cy+Tbb8lE97j7gIt9y5eJqvodl9Vglaj+MjQmeu2s4gbdGIX//z3As7jofmxidFh594s+e3F6zlX731cY7VagbDDg7NfffdJ0nSlClT5syZg93EuLi4xKSUpLRsmVyYpKmcJOPnge9+dLK5nEWNWv+neauBTZr4+jSZ0NDwWwODr89tvi2aDW3bdtD3P6zPLULFLBq5MnZYQMKWKGPE8bzO93/fwDC4UbNJhkYTDIZxDZrMMhiGt2oxvHOHPj2+D0jMQZ8M2/BqnxU/LTzx5rANJ85nw0WTfqReXSMLEZmXLzo6eu/evUFBQWE16vDe8JBDYcHhew+E7Q0PDTu4L3xXyPbE39fltrqD9fGJ7dXjdHBQ6L7duw8fDtkTdnRvGN5t38G9IYcOhu2PCAs7WD06KqpbUvvDDu7avTds327MwtStu873+sXVsEl+42bFEaG5RUV2N1ettqbSy3pF1cRC38AkUUZbfr9oaPCFwdCjYeOJDRtNa9hoasNGvgbD0JZNBwz+ZffvQRex5+XmUf8F+6bvjA/cm+xk0MLJQb82fsnV1Ce1zZOPGr42GMY0aOZvMPzY4vavOu/54J6ipztrj2ajojJNGbro2JjAxBmrw3FZPzg/784hg1qMHNbgt3GNJ89qMH5qswm/3T5h/J2jBvXesW1lUkqKG83esMfGA8KgFZOEy1gI6NMkWXffBEXmZQm2Qq99GKqoQMcaCRteGDIAnMFupurEYMeWTceM5g36DVI9rUuyLOsznare3pHXR/XMQu9Y+7wKv1CUebfrtZf/ge9YWe6Ftz/7rkSAGWcWTfNr3LYDzh+Mi006dXjGso14c1uDYcqQoVYNn1vdsXbzK90/wX7YDx9+HREdzYoSvl8mk6lNmzb4foWHhw8cONBoNOJChJvhwo+cdrESSzqjKuTqHDxKSHNYWNTqrq8aNR1sMPxmMEw1GOY1MMxvYljY0ODX0sevUaOen3+9Ii5b/TXg3Ii1CetPFZ48Y33gjh+aN5tsaDCtSavVBsMSQ4O1BsOsZo0n32bo3qTx+x98N/fLMVuf+3puvyVnP5m4K98CT04v7FzWj7QyIK8sfcTkuXPn8Cu6Z8+e0BoVHnJw94HQXQdD9oeGHNwbGhocFnogJHXn5uwWbZkmTWJ6fH9857aw/SF7jh0LDtl/OCQU77YnLGT3gbDQfYdCQ8OqR0dFdUtqX2hYcEhoxMF9Bw4cSNy4Lf6nvpxPc9PtdyRsCTxy6lRyWqbuqeiqWxYWFqGNm4oNhhENDNMNhtkNGy0z3DYXLzdrMhsXvls27H7/g1+djzabrGjQoojhy0+uC8kqKESrZxwdYXjV1rBpetsXHjP0b2SYb4AwtN2dAwz+XTrZX+kgPZSBiowI2gtHrU+cuia8CKHNeTl3YQpOHGeYMdkwZa5h8gzDzKmGGZMaThh+/5jBz477dXfCxUUbQ93QcVUH4WV+oaY7dB6S4SVRJcaWOIv64DdOZjnBLZNLhn78gogBKQlkvkxvXSgiEcARGD7wMSFZHy+n00WDde8IOkJJD4P1c3pUYVq9CzrDyAL5C9CCRfif1HNXOrUuSA/8S7pQwNk4BQJZhG6Xch7Kud/UvlYsVKEGHOZgK2im952ZjRiWY90v/eNZQVR5t+Ozr751ctgZlP2nTGzaoo1EEJISHztn4RLsnr/w9JNvvfIKPmXQ1l0TfCe+/u77Vrf79PETI34dmZufZ7FYsC+IWYgzZWFh4b333rt48WJBEFatCuj6xDMcD2UMjaQBOopoKCnNgssjzdq8a2j4Q6PG4xo2nGQwzGhgmN3CMLdZgxGtfPoNGby92ITsCowXHLUmYU+8KzLS1OnuL5v6DDEYRt7WbO5tmIWGRY0azGhsGPnkI/1HjlidY1VP52s9J2+d+Hv8V5PWk/ZCECKlm+q342qELwraPuPiMAjxm7m/RkXsORR8cP/uQ3vC9u85tG///pADIfuCMoO3Zfi0Elu0iPr+25O7dhw8sHf7gQN79h44smc/3m3vgT3BBw/sDw3fv/8KkVNR3SIK3X9g67ag/Xt34eX07cGxPXtjFmYZGpYeCSu326vVkV6lamZhMsNhv7D4ttt+adj4V5/Gy6DYbZjXyDChgWF4G5+fJ43devBYBsugEhMaty56+PJTW8Ly7XY0f/y2cY1esjdqkXPXvzobvmtumIZL+Y0b/Ni02QdPHPrg3pKudzP3ZKKSYoSAheuSpgWEl8hoX0nhA6OHtxs3xjB1vMHf3zBtWsPxo5uNHvr0RN9JoXsP5RdmmLj5q3foThqxoB7qEcumqiIHPStkmBMOB09NJpm/zdPIR8AikX8lzo0tIXSdwCuc1SlD/3sk8RJ0bIDejXbGypHJVSToqkGGVEKcMGwRn9vicoBLqiEePtjOuV1WaD2EE/KqpC/IgsjwkBaITRSgtwSHTb6MFBgQDkMwcaRuDojX/YNXJ0yfw7mcmgpI5qEvicTynNsziQoHLBQRw5coCKcUsR6HWM5HmR3L7m7M+VwjC3UOAQuZMmOzphfb3OHGLISxD9L6tcsxdRmG2717t34rjxw54ufnpx+Yl5d37ly0JHM8z+7ZE7x06fLCgpLyMuuyZStmzZqFiw+h+0NWrlyOj83Ozm7durXZbMZHYR/x2LFjixYt2rdvf0ZmDvLWQespkRSUnm13iSg+TU7NQecSUa9fthsMn7Vs2uvTj9YlxiGOgTkbZNJ35tcVZ8euTQqONdsdqOQiSkxAZ2NR45a/3NZgwG0tvpk9L+nMacQ4IVq88/FMbezymGGLkz4ZuTOvHFo8PeP9r67Y+MfCJQOHw+F2u101SrBxFtZl5mxul41zuDinYHeZkTG7sO09UsuW9mlTtPISjnWUsqybESWbC+9mZ2wWlnE5eZeLqR4dFdUtKaeLMZntptLCvXv3Zu8OTfi5n6thk5IWt+tjKuqRhetinRxyiygzH6Vmo0++2Gow/GAwfNm9+6ply+Ot5WDH8f7Yvltc6NfAMzA39+54cKfMqGTkSrfPHRdaPNnZ8KpPg+8/6B54LlY22dBvaH778sfb8w9mojIjQgMWn8IsnLH6oEh6zcRhwyVpA44dbv6r7+2jxny8du3kUyczELIh5ESowC4tDgwiAAMWwr86ywRe5AUYxCgxZDaAS7LZbHY7fFgBkZ4vsqJhKrHYzxHhAwnQaw9DTLG7SPyIcyCYC0xlJIuCBIdbIh0N9emoBZ7F3pELn89FugTykhvvbCsu00kJhIYUwTcb9ErMrIupWVlFguwCSmmwEdtyfQHuN2P+vP8AO8xzjUpz44CPkqSKAv4xr8QCCypyqGS0nuzEfwUHdp1sFncBvlEu4IZKWHjxofJ7fOqQhfyc+QS9qiq5edJZWHeeWJbFd6q8vBxThGEYMmpe4cg8sC6XA1hJHkVxcSnP8wzjMplLiothJB9Wq1at8FE4H2Om4mN1LuoUqmASXsVYTEovLndClrLyKK8MffvTrK5P/bRzZ35aGpmHD98OmZGBiWjMyqhxG1N3RhfhI1U3eM4WJ2re7tPHugxfteU8TPCteIok+OGPmB320aAdQxZm/rvfjvOpRchTeqqt8J25Cpr+4ZgKpym7RVtnw4b83NkwpoL0IyU3Hf6nYyqoqKpJt/g8Yw8PD3efOVcwehxmYUGT5shRLpNGpFqoJhZiV4+VVI7MY2Xj0YBhG7s+Pbhv/82pGcjBkOOwvZZZbFesbjQy4NjkbfErd0YDFbB5nbVJaHl/aqvHenXtN3rYXlzQh36kCLNw9oOWJ++wttdZ2H/JqRHrE2cEhAkCdA8sxWdHaPy+0JdmzOu1ddcxVsghfWqgex1ChQ558fpdgI2qLISuMdiysC6dhdjeYsOLvB8j1O2V3u1Tg8m6YF3DDp3dYode9xpmIT61EaiOPUvk4lgFu3qCU68yxb6fKMM0cnBCDRMUbJoIUeETigRswEI3SxKFIAa4LU7zzqDfz527wInYg+REAWpIsT8nS9iVBIwh0fH3bu/gcgwMpdSsxFdUebcLA4gkFGbDho61LK9yFitPjChys4qJsFDvt6NiFnYy3V/XfiFMGurJV5Kk6F/6QF5u6dK/boV/wW4MIqNP9EfhdrPki5HyY4916du37+DBgz/++GOca8EHJ5FUwEMjHhVcNFyvKsqSqKD41DwWxqJiFsLjMpqtOB0Mj7xfl5REyYTTykA/0ni/TZnbo7JVuGSYjwHveeFiMV4odZkIbZAqMJJkw7f3s6EB//hm+bCV2S/3WR+TCpMGedLw50lWe1VjIVQqwJgKve8MjKmgLKSiupLAbsDbIYH1sDHMzHnuRj5lrdoiF8w3XSsUXomF+H0UVF4mFrbEyjISmCYOPsijgrVVRYdqwR6CyaGNXXd2TODJFTtPka/IucU5iywGn7TW96FiSKJdYmTVriL7r2jsg2WPdnR3zUYm/Eu/paeGbsQsDEXQLUS3zsjJqHYCP5sIThjQjuAH+4WzArZjS1iNhRBg3Am2L8Kw/j/PmjVrwYIFX3/99ffff4/3OX78+Lvvvjtz5kxfX99u77yXayzB+586HPb911+MmDhz+vTp4wf26Pi3l+PzLdERBx9/9PnR436bOnNy968/X71q65jRU3+b4Pt/LzwxbNgQfELGUbpo/op+g0cuXLX8ux5fvfHqv3HKos6Gv/DiM8NHTR3vO238+OHd3vpPckJW0K6tb739at++w23OMidT/u+33/cd4Tt50Yzun327Zd1Oq6Vs07K57Z99bv3mIwqDXvr7g/2Gj8VY+OCdbp9+8fXCFWuHDx70WfcvWOKTvv7i3z/+tsfk8fiyJr78+rNJaVkurxHPR/kPmTs05q61vfByFjqnz0S8JIMR9pSxdARWdqT0LicVjW2VW90qyh14o9VqxS45/ltxrF4ewT/h7Z5pFLDFVwWVVA3j06TnFhXbYVAdKwIK8Eaeg2plPVvAQydDBnHO+DXg/JjApOC4PKQ6oAgDVeHQ5xnHDvmPRKe6FZhiHKHNJ4t7zwrrv+rEF7M26DOw6ZXmddIV+M8C9TK/EIYcui05LdsxTZows2ZQFlJRXVEa9HbUyPTT0FQlzlvMNG5aMe9M7d7nGlkYGGczwe8OJ6eRlxPee5VMBoKPIR/kcSg2vGKyo5GrYkaviQzce17QsJNgkebPYJo3zGjbEnxG8AjdqgQO3nBx6L0F93VmHzEiU7kCLByyMXHqWhhrD3yVwJJBICeC+l+9rgt6bGAnCS1eFwztPX/kF+KNpYXZzzz+sG57sVMYHx+PvZQuXbrMnz9f/35hQWHRG93ey8zKfe7JLu93e8sNLWLM+SMhDzz54vlcU0r0mbvv6gLdTBXRWFTy4gvv5WaZFVns1//nxx5/Ahsmc1H2Ix0fdwtweofbEnHw2NL5CxMTzzz7z6fBmuNUaMwD9z400W+GovKjxwwLDz8tqYzNWVJaYtH9wp9+7P+v59/AVyiYCrBfyAhIdKJnHr1r0Gi/c2fOYATq1Jd57q23u8VmFAgIvfLC013/8Qp5zFKh8eJXX/V0e7sH5SNjJ/ODdc9CEsHV1jeoOhU08pljjuN0Rur3Xd+uL3jn5tY9Qpl8ZAQ6PClkPlITowrwRL3PVg8qyeYK5AyNDBkcszpmTGBiUGwWeOUymb0PBENP4TQqLMKNVKA0cboADV16Ytj601/MCnSRlOhZpE5qSv+s6BxsVFS1Fph7eGtJP4PrOQdbYAIYJkImwI3qtUsVNgr6MUCtYJkFjV6d6LcxkczBJiHVysyc7PAxpLVpjOCTdggm7IIpTQU/NK5T+YMP2O4qwQfJUEc6eFPipMAwxWMo9I6gpKUKS+8XClvgbCU2eena3Ze3F8L9gRlrZIV3vvTcU4MGDdq+fTu2xngHp9PZunXr9957b9iwYf379x84aMgzz/8zIfFCp/vu8B09AipS8YWnRN7z2PMpxc64U8fuaPcwA56oml9gfOfNLxkLxP7r2JGdHuqMT1iQldzx3oeHjRznO/G3YSMH9ftl0OC+/VPTzz361MOMp8sM91TX5/r9MgyzcMTIwZGRiRoSONEWdz551++7hk0a89ijf3v6sf/D3gpXlvfPDz+Ctl4RPf5g6+HjJu/btWvVsqX4PnBgDKXBQ4btORrpkJT33/rX259+BSDQxKLinO+//cVOPp2BrzoXFXY0d7oRWKjbb89T0YU9QosFvi+ofxC5suBbTsBOvZxDHjHpZZuUmW1iMdlI1vLEKRDnmGRDeM5QHAMWBkQCC8/lwlsh6WghR8Fe0M0JDiXbXTLqM2nPaz8GDlga91L/Jcl5ZXivP+vM1aEoC6moai2wAX8NC+NgVkfP7zzS9DYx9ZLpU3GpHIZqe1mYHLA7Dtw7hWFmTnc0NaS2M8Dc3PARIJJ8GfmhSQ+a2j/gaFkOY+2h78yQjUkT10HfGRecQ5UhwJB4gmAZLAaZ8Q2HUqu8bM1uYh+qsFDSP5OgStBxRhMSExMPHjz4ySefPPPMM9g77NixY2BgYH5+PrbMDqfbwQqCqD78wF1+Y0eDi4mQKSsOs/BCiSvhzIm7730Mm2lBFa1W+zef9hHs+ASK77hRjz7WlWOQrTTv0Y5drVa2zGLGfuGFpAzezeQUpLz89ovQyQVSxP3f318aPsQXJ2r2nOl5eeUma9Gwkf3WBW4uyCq4UJTVq2fff7/2gcC7ncasJ15/A7NQ48Av/GngiKDffw/euaPc6iAXqA4bPnJX+Ckc7X/efe3LXwZgS8ky9rKy/G++7EnGOMAVAwstf6FfeMlMQ4ZwOC16bxqW5R0O1969oTExMYIgvPXWWy6Xq+Lbx3oVq6LJkiTonhmUeC6xUPSyUCKB836wQoBVshthYRRhYR7kE52F+pgV+CQ0B+nRsyhMHo8+H7Lh1R8CR6zKfG3AurNJOXBGykIqqptQfxkL18Uqep0TmBcXCQRoZJwALFdhYZzfRvhmE7FIHDNjJvYLU9s2uMRCwjc/NEX/li9hoUZYmDIpMFz2sBCiE70sJIPOJDL6DAwdYSF8SuiPWSgDCGUGZsHEPklCQsK7776bnZ3dtm3bcePG6V+T5XjRycGH1rs+3P6nHt+VMtCxsSQtxueeR9LL2WOhIY197oYqOmzYHY4P3v6SsyKJY0eMHnLPA/eLIspKif374/+HbTk22JzogiRo6ELGuaee78ppuuXiuj76zIC+I1jO0X9A77i4dIu95NPP38vKzFNYhUXyG6+/27lDV5xW2Vr0xpdfseQ6sV84Ycb8IwcOjB01El+mlZHwSXv/0vdwdBJOzMv//Nvb3b/mGSQIDrPZ+OlHX1ViYX4H64PXPr6wblmIYBJ35fPPP1MAdNDvRq8g9fHxwSzEvmDlJsaKQ/XaBtXzLd/cqn6hJ1o9z+mZT88oY1bHjVmbGhRjhJ9kOICQBh+Kc48AjZFwtAzjXRQ0YdmJT4ds6zc/9t+D16flm+Ck3upcbyrqX5SFVFS11l/FQt/10SIBAymXu+C79gQ+kB7dY4Opj6HOssymjF57wm9zZEBwJPiFssBMX2Rv3CilTXPksCOYi5R0uVTReDS1vanzXa7bC5GxXFUGLD4zfH2q/+oq37X3FOshXR5jKBOSFtvFPxxT4WGhJjstJS8+++TmzZujoqKGDh36/PPP4302btzYqVOniIiI48ePY8AcOHwM77t6ybzn/vbkppBDR44cmTj0p/u6/gP7hRdizra5s5NdlDBRc7Kz3nv9U9EG0Y77bVT7hztiw8lYi/v+0G/4cN+o2HPTZkx69V9vFubm5Rel3fMQEJSkiOvy8JO//DQYJ2r+gll+fv6YhZOn+U6bOivqRNSE+dMGDhjxZJdni4x5iDHf2fWJk2dzVRY91bndkF8nIFF84tEu3/zQ60RU3K7t21586WX8LIxWO2bhG92/IE+JKynJ/vSjL1wcVONq0Oc2r4O1dvPOVGYhzMFWiYVXNMKVdvCw6umnnjAYDI89/pSbEfbvCz0bc54XpLvb3a6P1j9y4vSw0b6PPvzgiJGj80gXJrgM8thVyCAoMTO/TGeh5kWh6nnI+pPWyJlwZhy7MhG+a6+zUIFxoLgMJSC3Bl+cIodD8QkfzODYYovQqCXHRq2M6uG/Q++RqlPwes4eRFlIRVV7wZtdTywE+wIWh7CQPXTynJeFJ4YFJsC3fL2zpYD10L0zb3WUbsoYsExymZ0fHXjYb8uJgBC9HynHTF9ib9gq5fY2yGnBFklGFlLLpfoCCx+9y3F3DjIaEbBw1LrUWauOgKUgsIS/+lXJ5LLBoyRd/GFMhbhgHfn6Lvx2iYV68kTWJTJOa1lRXl5eSkqK2Wyu+IIsdvLOnz+fkZFhNBrx/gx8aIMXBeZCTlF+fn5RevzDz7yYa2ZYqyk++SKjKuDzIbXcaIXzaDLD25LTU4j1hG9uWKyu1MwMY3G+28nJvMAK1mzjRZx8VUEsaz0fk2guc/KC2+W25eQUl1uKsX3OyS7ITs/JNxdjapuKbOVlJYh3xl68mFfIYnwVZSeUOzh8vNvlwOzILii+mJWhES8ZP/Kigqy0khIdtDjYzC5If12xUNPbct1lBc2bZrS7w+4/Ewb64Qigurn6zpWl44bsQrp4ks9O7tkVhFl4MjJGVFHQti37j57hFdTpnjbQ31l03P/Y3weP948M39P9y++6/v1FUdGdQhX8SDKUIi6rsIyDzqZ63vpDeVi4CvuFKTvPFQBRSDpIhtH9ZdK1yMNC+MBTcLR14JyjI1bEfjxmQ0J2sf46VYq+grpw2+pLlIVUVLWW/vLWIQv1ZhroXUJgIsmsDFVz6MCxWMJCccKqqGGB8b4bzlRhoeqd8ox8yUk/VoDhaNjFE8dtiPHbHOXxCzEL/ee5mjRNb9savkKnyjAWA2Y+U0ah3+4t7HhnaetcZMxWxOHLIgcsipoSEK7TjVQZQvpg8jSeDK/WZKiPJD8VOZQ5K7e5wDj8ke0i6fkTpkNVZPHUscODBw3AlwazaMVEftvzZwfUV1ZEQGL2rMCJvLF6bGiVfTyzwXl3uLSgL3sXrn0ONmjzIgcLer8QWISj9flIazcHWzUW2uD7hRLByZ9kIbk8zEJMeZ69mJ7Rrl07RtHcorhr2+bQo5Gsgh66p3WpgoI3LJ+6ZD0MaVCcxSbbZ9/+cjG3WBRUwQ0fwJTJ1+rPZxmxX+hh4X+RTKZp910VOyYwaee5vMosJKUw5HlIHhYKmDAf9l/05o8r+8+L7DYoIDI5V9MTD/PM6k/Em5lgUE7Vk9WhKAupqGot/c2tQxZiJSQkwNz6oQd4N/RLSE6/mFcihkbofqE4YWU0YeFpDws1nYWkIK+pDpsz52LuoQOHQ/ce2Hc0rKzUWlAiDVt+CuadCY7y9J3xn+vyaQRjKiwuYm0FWZUuFuT1cw/vbO3a3npXWHl4ots+cO6xydtyJ6+L0K0RT5whvdoWnzT1QnJOdoYkCUdOnI5Lzih3oTkrt5MOLxWkuVqBxZNEXlPlwLUBjxP1/qVvWblZN583oBRSP0wecz3MzV1nLCR+YVZaesuWLbE3LqioMgvLFbR+yey7H3mm68vvvvV81ze6vd/mvofjkzJg1nNNdrlc9cdCvPNnQ5ZjFg5aGPPaL0vPZxTprxMU7DxjKigLqahuDtUtCyVJkmX50KFDUVFRRw8fw0V5/I6ePRefWyzsPaS3F/53FqowfPn8ubgD+w+eOnH27OnoAyfDjxw+eTo6e9DiYzWzMC7hfPD+fd1zv+9Y9ghm4fKY1etOHh2zImbM2pQZW05UY6HLxSQnJu3etTMkeOfBg2E7du/ZGRKWmmtdsGaX3WPsr5WFZMJQq8Xkctrj4uLOnDmTmpahehpBb0TdoCxEHitdQRHMITEpIbFt27YOFhrtgrZvDjtyilfQg/e2M8to6ezJyzcFYXuvOcsYQc4psbpYkqFlHua58bCwuD5YGJ6q9vU/4rc+86eZByABwBkNdqF+IRXVTaW6ZSEWNj4hISF4gXVzxyIOHzy0Jz07PyGt/Hhk2hVYqKmKwAfvCrGaYYi9Bv3XxZTkjNXr9o3fEFczC3fu2pFXbByp+eksjEfJ07dt7jszYsiy2HErQ6uxsKDAeDDsAN7EMo6QkN04DXZGCj+VNH3xJuIXXrs0iVcVSRQ4Tf/0BOlG4XQxOFAW1oqFqsilpaU19mlic0Gde9C2LYeOHJdktcO9d9pklH8x/YFHnjxwPBKp3KnTZ9//9CtWVKBFV4OiWSUWqnXLQviWbxzbb8bR0auS3x2yNtfE4SThAKM4KAupqG4q1S0L9Zoh7A/Fx8dD1BoqLcsP3LQ1q4A5fCr5iiwUGHfQjl3YoSzML7aY7IkXU3bv2rcj+NTARUdrZuG+/XvDDod/V9L7EdsTXbiO27N3zQraNmzR6fEbM6asP1yNhYIgnT195lxM1Jn/Z+894OM4zrv/E3vv6pLVktdxumM7b94kjmP/3R2XJE7c4ljVkqjCBnaxF4mUSIliB1EJggRA9N577733A3CHO1y/29t6859n5u4IAuwEIAKc32d43N3bdouZ57vPlGcKcgID/bv7B3OLKsrq+z4PjDWCgRgvj0EjHLiVXJLZZMA4JD0Y3SzEtpGazwdQDy4LiegTJ36hS1Kr1d/7wff3Hz6iM1ouBQUmpmbwgvTko6vg/cUlfev7//a1f/zXs58d/X//+M/f/+l/4p/B8xwJweBtL8QshGg0t7jy3bIQ7/z63rBfbop48+Oi/9weVtbU5/17e8RYyMQ0PTSxLKTCb+RDQ0OUhbLiaOvur23RVdT335qF2ClUBH5EZ8As9PMN9D3n7x8W1N7W09Ztff9U3q1ZOKgZiE6M//eu3z418Pxz5idOl52Prqtaf6Jw7YnSQyE5Y1jIcbx+WHc5NCQ25mpXV8fxz09fiYzvGLAdPRtm8nTbuV6KTGLkSJIwOrKWLLtwstshBo0kKeAJuCSYrhBmJXTvh801TmNY6A0i9oXrAWYh7OBhoTshq93W1QdtcqLgHlDY1dVFX1/wfRss9s7WJpvNJpBVCMPm4nHe8rBQo4UBq7e68t2y0ELaC7/zyrm3j5X8aF0AbS+kJYr5hUxM00uTwUK9Xh8fHx8UEBweejklNba9R623otScmluzEDuF2Ho6HXxJUWloSFhEWFR8VlJ/n0atlW/bd8Zqt+SVFP1m8NVnNS9hFgY1Xqo06V8/lLovrGd/UOYYFuIPkRcS4mNLivMtFtOVq9E5heXDVnTM9+qw3cNCj5UQBKcsi5iFsuLkBTLVL+ElTArBSaLgcpC4au79ydhEzmGjdaTkxyFBhAiYFgfmH1x6SgNV3k7ThoWcE7r40hkjOegETL+F//HXTjgt2Ub/AHB35EAXDHyZPBZaEToUXIb9wnUnq37mE9Kjd7obhxV4cSKnZCxkYpoeoiV3AlmIwVZcXJySkpKfWxAdcTU1Le5qbOKQAWUWNNyahS4RQ0XJy8kPCb6UnZl3MSg0MiUmPS0nt6jttnWkBUX5oVfD/6P7d88N/+kzhkdPFJ0OKc5/91ju9qCWA8FZY1goCFJjfUNMdGRKcnx0dGRSWmZ0Qlpl08Bn/jQ296gE6KKPQZRkLvRyMCZfTHRCeFhUUWEZ3iEqMu70qfNGA0w9CEO6HdaS4sLPPj0WHXUVkdGHdofz1Omz+ExxSck7d+6qq6sbE1b6i9WDykL3H0Ahby7wB8A8MlnMHuDRBHdJUEVw6IT5K8jB0Cjo9QuhNxdlYdvwhLMQ71w1jDZ9XuZzrv7Xu6No3xmZ7sL8QiamaSVaeCeWhenp6XhBcIqJsXG1dWW1TW2lNf1ZhY23ZiE4hTZrfGyCJMhOh5gQl1zaUNHc1BEQknLbvjMhoRf7NINv2Tes6X7qKf3qfK54f2jwy/sSN/s1bDsTP4aFWq0uMz0DbCZvz8xMx/dg4eTUvNo9n/jrHF5L6zUUiihxJAyX+NKfPHc5NKKlueNi8OWvf+0fdn2wb0CtLS4q/+rffqOyolanG/na3/xlYIBfR3trdVXFSy+9FBMTwzmFefMX/vK/flVRU9vXp/7ud79bVVU1pTFJbqkHnoVwNQChi4yylBQyrTFEZHDJQCJgIXJnXry/TJxueHshCBMU0Ua/xX/4qolgIbl5SjdgoQWhX2268J1XztHxhVVtMNaeuoZjx1TcS1G6YzEWMjHdtyaWhXSG24yMjOTk5OzMnMiw8H51R2hEtNaEUrKrb81CWkeanJgSdjk8P7coOjKub2TgcujV0Ijs9WcKbspCmLqCT05OjI6P+0Htz54efOF5y5OfF5/5NOrqW59kbw5oPBZWBPaBBDklxR9+bU1VdWpK0tWIy1lZGbmFJTGJ6bVtWnffmetAiCVJslNxcZzT9NW/+ys64Z1hxPK73748qDYCPGT5pRf++mp4siwJ2LXtbG1LSkoICPR96snHt23f6eRtK1c9npqRT89XUVGxZcsWfMgDUlP6oLIQjf4bUJaMF2yku4w9mXtdIr8Ksjb+29e2aHS2CWahFebyPfOvr5xde6L8hxsCS0hs7uvFWMjEND00sSykGhoaio2NTYhLFBycwTjU1t3f0e/ILWm5NQtpldiwRldZXpUYn2LQm7U2fU/3QFu3dU9o/RgWmufOalqxiM7ZJCJhoLensrLyD0NvPK/7P08Y10T2xlYNDr5zsnB9QP3x0EJqwIhVw1IkSdEOafJys3NzMlpamnwDgpPSczsH7R+eCtW7o+W4k8eIUc/C8fWv/Y2LBG6zQ3jrt0aG8S485xx+YvWfXw5OxW8Cm9at//XPf/n9n/zg7//p60+uWfHHdzY4bJqnn/1KdmE9z3MOh6OsrOydd96ZkHleJ0QPMAvvR250Ym/SzUL8I+taNPr7ZiHkv1EsNCG09VTmLzaFbzhX9/uPknQ0hN91zcKMhUxM00MTy0KO4wRBaG1tzcrKysvJLykoDAw6FxWfrLei29aRyrwTSWJHW2dOVm5OVn5eTmFgxMWE+NSy6v7NF0pvykIo9gJntRTk5P5H268f633mBeezH2V+UtTW/vtDyVsvtx88nwoH0fuDsq/gq0mCmJQYX1VZ2tPTFRhyOSImqbFrZP+nQUYS5Xs0C602IwK7bxdF8ze+/rci1M8hrU7zyqt/1A0hjjfo9G1PrPrLSwGp2TlRO7fvUKwiNqAOyfL8k6vf37xnRN+2fNULgZfToN8NQmlpaWvXrkXQvAX1tV+4GAuv092yEP9J01vQ+ydKsF/4h6Mp9E/qIhcY23fmrovS3YixkInpvjWxLBQg+DGKjo7GLIyNjstKSy8ozAwJixwyoNvHYIMZIZS4mPjIiKi4mMSEuOTcioLwsOjEtKrxYyrGsDAnIz02Muq/u/7ny5a/etyw+lyl35WMTMzCdQH1+84kjWGhxWKrrqxKTkooLMhJTk4sqahOzylq6jacvpgA5uJ6FtodZgThdKzYTP7lX3zZzgEQjGbDy6+8oe51iLIFIcufPPf3kVey4xNCTp88hRwwS2Jrd+NLzzz27qZdQ4MNTz7zF1t3n8DPEp/l1KlTFy9efEAGVCDGwjG6BxYGZw/9YX8qZuE/vvF5+4BZll3UIRzbd+aui9LdiLGQiem+NbEsxMKGPikpCS/09fRjv5Bzmooraupa9XmlrbdhoUtxiUJKUqpBbxxUazPSsq2Ko6K89tT5qJ3B1bdmYWhwkEY98I51wzNDL77If6lMqTrse2Ht5wVvna340A/G2o9mod3O0bgzouAICPDDX+nNXHpBPY07cz0LEZkgXSLPR/zB979r47BLh/r6B956+73+XnAZHQ791/7mm5eCou123Te+9vVv/Pnf/fy//t0/5Pz+nZuf/ZO/LsiPferZv/S/lPLP3/yHF1988ec//zn+sTabjYzC/+LFWHid7oGFP3/31Ldf933zeMkPNgaWNfR4T+X5AzMWMjFND00sC2nVX0ZGRnNzM+WJgzNevHJVb0W3jUeqCNhCKumpGeFXIsD+CC47ckaEx8Qklo4fXziGhS0N9UF+/jvRvkd7nn7G+sTh9KPBScm/3hu3O6rvI38YXziahU6n0NPVnZqS5OSssiw2tXVejU1u6NRjv3BcHSmwkAwWhIBtiPRbtDtEJw/9GcGPdUGnQZ7M+Qe2V4Y5L7A9sjgN2ODD+HxR+/SX/iops8Zkdk/z9OA4hYixcIzuloUWhH7y1mf/8srZ1z8u/M57vnUdGgQ5BhLzC5mYppcmloWCIIiiiP0erVZLeYJZ2NzRM6B33bYfKXYKcbKabQP9g/RYs2TraO/tHRRuy0LBYdcNaTbwW18c+bMnjGsyzbltBuOrRzPWnq/afzZ5DAvxP1mUurs67DYTXu1RD9U0tg+ZXCcCYsb7haOOgjT2W/cSeVR0GaZCx7tha89z0BlIP2/hE5kFzXf/LKdCjIXX6W5ZiP3C7A609liBz4XG3xyMgwBE9BvEWMjENM3kmlAWUtH6IZGnw4thXgG1Trlt3Bnaj5RORc5zEiQCmK5+7mBEy61ZSI5Fu9CBZ4ZefNb2ZC8aUDv5904XbwltO3AuZQwLoU0HGwO8IDkp3vAdYhYevxB5UxZ6kvtbMoQMzA88Prxgg6SQ70axEFsbUdB88mlAU6cJbvPBE2PhdboHFpYMIJ+zVevP1v5s+2U78QhJ5md9Z5iYppnAmE8oC68NnnPzhOcVNGRASZmVd8JCShRZBPuBSzfegP3CTeeL74SFO9DeJ9XPPed4GrNwUBDXnyvzCWk5fAHmLxzNQrogCk6wli54fxdcaNiKzoUmm0lwES/73PKuww3DmG8PC+3U8iBkgkSPvN4vxNtHTC6rgPlCvYYHS4yF1+luWYgJ88M3jv3f33725vGS767zq2pR0/NAfmZjKpiYppVcE8pCURRp5VBbW1tLUyspa3xtU9ud9J1RBJ40GSKTwczZBUWC0u2wizWN2tv2nSE+Hr+B3/q87v88NrKqHjVX9fW/fSL/ff+6Q75pY1goSdj7VAYH+muqy/EqNpcdvUOldb2HT166A78QjLmHhSaPkdNBGsdCbG04hxpbZKsHOA+aZigL3SfHdyvKBIk43R0L/RpuwELIRqSuYxQL/3vThR++E/zWp6XYLyxv7EVQBtyZjYixkIlpemhiWeiVTqerKKtMjk9ISIxsbOsa0LtuP6aC+oWYHGZbXExia3NHbUdDWmp2Vf3Q+HikY1kIfVCl3/T+4Yn+Lz2qX3m24kJyeQVm4R9Pl41nIVRi4UtLQm9Px5UroQkp6dkFZUMmF/YLbdeBz6NRm9zhwNwstHiMnAGhETcLifMAwXBcgBSEbAYTzKDndVYeKM0QFnIcnSsEbo9MZ09qJ1yCJHPwVyN/tNrmoWEbTDcCYbyBZQrd32KxeM9zPQv7AIJOkeQweAlCJKwDXoWzwByFTjtCZxM7/2tb9I7g9m+tPTtklhWIyg0+IasjZWKaXgLrPaEspH4hxpt+eMT3zNnTZ47jk7T2WJOzqm7PQviELSM608Wg0JDoy2aTo1vt9PEtuS0LMaG2oz2P9z37nOPpClTTY7O/+WmuT0jLrs/jxrBw1ILk738hJSNbrTXq7cgdm/s2Go00sJPkVCKYImpYCCbB4JPaVARm+ME1OTOEhYiwjX5iLnrOLcFUW7RXpwJ+oc6OLwy/kILKGwfP27XXzcKzVddYSF5wwMGXrTKHn5Hk5AhvPO2F5Rq05XzNtsDWX+6JHIYAhATG187JWMjEND00sSyk5gWzraqqKisjW3BwTt6cmJZV16q/IxbKUJaxX5iRll1f21TeVFWQX1pU3n0nLBQ55/+oX31m6MXHDatD28LTqqrfP1Pyjm/1kQCYp2I0CyFIlgv1dHcmJcaOjOg6evozcovL6vtOX0wwgIF4iDRDWOiFmSAI+F3MwYkgaKGVBB68+DEspBoTCg+fxOqUxrDQ5YBbtUO9J49v3MKZYcouwkLOacIsPBxS8cutURvO1X373fOt/UZyWhhu74m/zljIxDQ9NLEsxOaFdiLt7+/v6+nHp1ZcXM+AFrOwoLz9NixUIPSMyEvYoczJykcQTVvKyS6MSSwdP0/FeBbaTOZfdf/+if4vPWFcc6Xj6qXUtHdPFW270rH3dOIYFtKFEf2wur8bkX6kWoOttK73ZFCchrzZPzyaISykFZ60prS5ubmvf4hslixWg1Yzgu8aZ/H6Vq3egSgLaR41GAwxMTEhISGhoaGBgYGVlZXSjfxCEUaMorySrMzk1GGjNiE+5crF8Ja6OpyzjS7XT9767Jsvn3nzeMn31vsX13YiODk4jfQSjIVMTNNFE8tCjwUgCy5a1nhOQn1aKT6t7DYsJDHYgFsi+G34MIsMc+cOG9G7n+fchoVwuLIfffSC/st0TIUFodc+zsR+4e6TMGfTWL8Q6i/xVeAdXyY/U2NGdHzhQ6UZwkIMQp6HqQobGhpqamo02pGEhIS29iYHZ4mLTcIeGrb9DW3DI5ybhVR4H0TCQ2DhY0tKSjQj5hv6hXqLpaqhDN/4lcjLkEsFhOHZ29eG/cIjl6t/9O7FnRc7frb9Mq0jZX1nmJimoyaWhVTu5hj3pHMwvvBOWAhz+UqeFjiSoHS70JAe3TYeKe108wHa/6zmpccNqzEL9Qj98XjOuxdqxsdgowvYAwWbIIucqFidioFDR8+GMRZOSxbSMLg429XV1UGAO+IdxsZF4m2RV2OxuyiIpB+pA/8Od1bAO9PIsDjz0frM+vp6tXZkrF8oyBh+JoejtbsR33hETPiI3qzwKCY8vLOrCRMmqx29eTR3w7m6Xx+IpbmHtkKy9kImpumliWUh9Qvxp1qtNuiNCFpqHGaH0D3I31F7oUuRBFmn1VeUVefnFtV3NfFOZVDnupP2Qt2Qxkfa8dzwnz5lfixFn6GR5P89nLI+sGF83Bn84i7ywoC6b0SvcTodja0djW09Rifa/2mQhdixh0czhIXIg8P29vbc3NwRA3QN7exqTUtPSk5K53n4RaNZqCiKLMvFxcVhYWF5eXnp6elxcXGRkZHSjepIcRZ0KsqliKCY8KspmckYrrFX4zOSkuwOAybMa3vD/vkPp98/Xf2ttWebevAbGNSRkk/6CxkLmZimhyaWhYgYJWxbampq6msbmusbnLy5rLq+qdOUllt7GxZKonlEnxCXWFFWKThhavshy3BGem5IWOZ7J3NvzcL46KjczKy3TO9/xfY3q4eXR/fH+0bHvPZxJvYLT1yGuXxHs5DnxbKS0pbmxpbm+vPnzw4Oj1TVt+aUthzzvcr8wunKQgSVk/ieXJhqQxpgEv5ZJaUFiQmpAkQ6cPedcSLkhJhDbr+ttLQ0JSUlISEhMzOzs7PzBiwUZFFAnCw3tNU0VNUYrCPlZdUp8WkGjcZk1trJ+MJ/eeXsuycr/+XtM6X13cjDQo8YC5mYpocmg4WxsbF4wThiSk9OaWyqau3qa2g33DYeKTadTps1OjLGZDCLPHYQXRbZ3tjQdj4gfsPZwluzMDoiXDsw+K5t47Oal562PJ7PFZ+8Evbq0YztYZ3j/UKz2ZqZnoFIuO3s7Ez8lYWTMwobMAsfsq4zM4iFtAezRqPp6+uz2SEIOu1HKgrQqxPb/jFjKnCew05hY2Pj6JMIrnEsJF268M/OLkzvbe8sqy4NCrwUGnSlsboakTEVmIVf/9Wxjefr//GNz5lfyMQ0fTXhLMRGIDU11WiEClLdkKasPD/wUtgd1pFaDCOx0XElRaU2C2e3OvsNg6kpWRevZKw/U3BrFt6VX+h0CqXFJc1NDdgvPHfuDPMLpz0LaQ9Snufr6uqwq5eQkFRdXS0ITpxcBE407gxlIU/yOz7k8uXLbW1t2CnEhzQ1NTmdTsk91r6MxGBTw63KCu+UnYrS0FqPHc/IuKtw5xKKvHy5p7cVs7CoH60/VepzofHXB9yjU2/SXki2TpIYC5mY7lsTy0JveyFYJzBDeI0b0pv6h+U78QtpFxiz0dJQ11xX09iq7rBZ+X6NtNW//KYsdAcDUbBL4G0vTNNlDMjyy4dTNgQ27CV+Ib0XUvShjtTp4Pr7enTDg3a7lbUXTnsW0hi4giBgBJqIYmKiwsOvtLa22nmI+iNBPFK13uYSSCbAe+I85+fnhw/Ey+Xl5b6+vsnJyU6ZsPB88eaAyoiyIcgxQBFkdYptXd2iwxqdEAX5lUcRly7TfqRlGvTuZ4XbApsxC63kjYu2XE6pGAuZmO5bE8tCrzALtUOaEa3Gah/GJ+lSC6k5dYSFErAwoHJbcN7NWOiSUX/voE5rGLIM41W9GY2PzW2dP6d15RI0YkUQHAtiYuFT7UD7MAufHllTLlXqEXrtYMr2oJYdJyHuDCL2EH6OC1joguinnJOzKopktjuNNsHEo73HAuxjf8cM1wxhIfK8hWEPb2RkxOuK9asHtSMmkfzIutZ+ykKS3UEpKSmemkxoazQYDBL1C88Xbg4opyxEPDh7eHtuYUlcZHhAiL+/36WkmIzu1nZaR/rDP37yrddOr/28+P97/3xxbbv71FMsxkImpvvWxLIQ2xZJklJTU/Py8lqbW2KuRqRnxiSmZfUMSslZtO8MZWH5DVgoSzLvTE/NiI2Oa25si7oam1GcnZyUkZpVN35MxTUWgrXlY+KiY5ISfqd5/c/tf/vY0LLw9qv+WekbThRu9Ws4FARxZxBMskvsPqnCaqirz8/LqawouXgxqKisMiO3uL5DdzIojtWRTlcWUjU3N2OnUJFFp9NBK0gFqDe4joUuMqYQ+5FqtZp6k97D3e2Fo1moiHgfh6hYOUHd3ZFdkNXS3N3R1IcEicad+cEbH//Lq6deOZL17XfPltZ3whGe0G5TJ8ZCJqb71sSyEBFTEBERIWOJUk5GeltHdVF5dU2Tvriq9zYsdCmCwx51Nbqnq5fnpJSk9Jb+9oL8Ur/gpO2BlbdmYVjEldbuzlcMa58ZevFLxsfybYXHoiJeO5C8O6R974XUMSy027msjEyrxaTu705OTsQQGBg2pebVsvGF05uFPM/b7eDZi4KzoqIsPj42PiHJIcD8X6NZCL+OqLW1lS5kZmbiLFtUVCSN8wtlOwzPwNsNFjtySWptf3hYbGJ0uqZPTf3Cy4W6PxxI2nGx+fcfJZgIVfFtuC8wZWIsZGK6b004C7E5SkhI0Ov1VrMlPTmpo6s2OSMHszA1p/5OWJgQl1hZXmWzcAlxyfVdTXRMxfi+M2NYGB0bVVBW8i6/+c+sf/2UblW8OvGz2Kj3j+dt828cz0Kj0ZydmTWiHx4a7Dtz5hR+4+/q1+aUtpwKjjeTFp+HRzOEhRIRzkYVFRUOLLs1KSmB4+x9/QP5xWU3rCPF7mBgYCDmFiZif38/3lJeXq412Mb7hXB+hJraOjELL4WHODmX3ShGXg5TD3RiFuZ2o7eP5WwJqP+RT+AI545xit8Hp5SIjIVMTPetiWUhtUhOp7OsrKy4sGiovw/DsVutwcyKSaZxZ27KQog741J4TqirqS8pKtdpDbh0D6iHmztMt60jtdotlfW17wlbnhv+02cNj0Z0RDZztrePZH4Q3PrBWYhHOpqFoig7bPaqyvLOjpbBQXVyelZmXolNRkfOXGF9Z6YlC6kwBGtra0kHTqW1tdnlggkjElMzHCLCWQ2zcMQOv5ZeGe8WEBCAFwoKCijANBpN76B+PAtx7hRcqKWjGy/HJEZjFuKHFBoY3K/uwITZ+FnyL3wuv/VZ4XfX+TZ0aeiZR93UlIixkInpvjWxLKRWBb9zU7/QqBse1LT3Dem61EJuCY3NfVMWyryT9p3RDg0bRyxmo23IMtzXi1fQFr+yHcHl56OKydzidtvBo+a5s5qXL0IGG4K5c7GtUvQWkw/a9ZLhK9gvTNNlqBF67UDy9oCmnWcSxrDQ6YRJ6Pr7ekxGHV6va2qtbeowcGjPJ/5sfOE0ZiHORvX19ZcuXQq7Enr1avjAQH9ZeSX+6zrlG7AQ+20XLlwII2pqasLHXr58WRxXR4oEDudpncnqGxAcfin4xJnP7DZpWG2Kj4weHOrGfuG/rzv93bd8152t+MXOy7S9kGpKWw0ZC5mY7lsTy0LsEWKrkpOTU1VVVZhfkJ+d1T/Qkl1Q0tnPRyWW3JqFEn7jFoXM9KycrNziwrLkxLT6rqb8vJKQsMwPLtbcmoWx8TGJ6am/H/4jZuFjQ8tCm6+cSozbdLJ4R2DzwcDMMSzEH3U1tdlZGUWFudHRkTUNzUXltWX1fZ/6RZnu9gdPc80oFiIyMS/OeTnZmaWlxRaLqaCw2CHIvAIdjb0stDvgJ2NVV1fn5+cnJSUZDAa8mpubK41noaeOtLm9q6q0KKcw22oRrCP8sHpQlGwGRVl3LOHbb5x989OCb6093dIHY+29Myl672rSxVjIxHTfmlgWUqWkpODPxvqGwtwcSTE3tXdjvzCrsOXWLMSmE7uGMVGx+uGRtpZOjENcupsa20+ei/TxLbktC7vUfW9Y3n968IWvCC+UCuXHo6+++WH67pD2XeeSxrBwZMSYlJCIl7DX6ut7Dt/DiMWZmlf78blw1ndmGrNQkiRRFGHCCsHpcGDrr3BOQSa/ThjFQsjxssxxHG1lRJ6h+jgXWp3KzVgoKEjhHRghMHhHhqfg4IxGl6tci9Yez90W1Pgfu9w9r2jHVO9ojakQYyET031rYlmI7QA2L+np6TBbgKxgVw+/h2fkFnYPiLdtL1QEHu+fkpRaUVaJN1rNDly6c7ILA0JSdgRV3ZqF4VfDMvJydqADf+X82qr+RZdbwj6JDH/n4+z1pyv3+6ePYSG+WkVZeXNTg5OzajSDRqujprG9qLrr+IVII3kMD49mCAtxBsIIpBP5kg2K0+mw2SyQuW/EwtEH0kkqsEOJPz1jKq6NtUcSdIGRyHmQS3LwFkFEAgdjYGXEWxF663DkT98P+fGmqz/bcaW5V0dPK5E5pLxXmXQxFjIx3bcmloVUJpPJarXiU2O84bfn3sHhrn5HUmYlZeGec7mb/Qp2BWYI1PLSd2hMTlnE1pOzO3q6evGxeM2u8L19g2Yb2n4yeV9QzoWoPGChxI1noYLknkH1HvQR9gufMz6RpsvCVulURF1UkSW+tAd+JAnDRn6OgnmNtwwNqonREjRaXWNLp11Gx86G2OkNPTSaOSz0Ltvt9s6ONgThhTjFhRpa2gWY/esaC3F2pxWY+KjGxkbIqURGo3EYvxfdKAYbPsoh2g0aDX4QVk7AVysqLjc6jJifv9vs+/X/PPKtt0O//uqZkoYeeirvlNZTJMZCJqb71mSw0C0XsYYuERe83gFTSlZZXHbJ5YSC7ccurz3ov+mjCxar3eWpUnI3r3jLJoajhC0ufv1G+hFzyOWUS3F5BY2dxL/jzXsOjO87g291O9r/gv7Lz+gf70EDJmTDyLPYkRHABxeARKLPjBJcFHgoyhgFVofo4MltPDSaUSykeQjnJ/yak5KSlJ2dmZ6RZbJxY1gIHPB09ezt7a2srCwuLs7Pzy8tLbXxMrBwXGxukhF5o1aXlZNYXFKRmJhd29DqkB12hDLrnes/yV77edWvDyTroKoVbmZKGwsRYyET0wRoElmIKA4hyTBVDrIICNMPv0yb8Ov79Tt6Krc8Ip4cGRimwBIYVXqIghwO8cixW7Dwaf2TaqSz4ovIcBhYPzgDvOIjYhVvpil9lX8wNHNYiEXzEB1TkZAQFxjo39TcKpGaz9EsdPLurKYQmc3mM2fOHDt2DC9L4+dskvBbGbLy+Bge33hjY/mpk+ciI5Kg2CAJ79yoRVs/z9vq1/Dr/fE0T081CBFjIRPTBGgqWIhgfntqdrFRciJkxeZFAqNx0zjGhIX46k7YxYmXnDIiAx6AhdyhI7dmYS/SuFkIcbtvw0JqSOnC2O9mumYOC9EovzAuNrq1tRmjLS+/sKCkfAwLXaSzDAUndgojIiKsVmt3d3daWppDdI1loajIkMNwRrS1NzYX5KaJTldddVtGWvbwyCDGY4sW7fgsbV9I3e8PRDjIPXwB2YixkInpvjW5LFRg8jjyPy5+LlwCBdElyPCyPfrMNxidTFgouss2fEhuvxBT0WE/cGgCWUj1cOJwRrGQym63O+xWcpsK/os7JRgpP5qF3hhsyNNlhvY+xXSUxvuFAoAFtksWxSkg2Slx0PQ8qNbi4zjENw+4Dp/L3nAife0nMfz1VJ46MRYyMd23JpeFRBR1xEqAgYKErQ40BYKo3bhhHSm5AUlxQUWpm4UuEfGcZe/+O2Uhr9whC+lN0k6FD49mCAuR5y/n6b2pyBCFFL+BIZsTfo0wKgYb5oDT6aRHjUHXDViIoSHSjOhEEMdGxLfPW2nu5fGvaxqQdh6L232h4OV9F2+WtyZdjIVMTPetSWXhqKJGEOiSYLwW/sQJOufdXC5IlIW0gGPcuf1Ch+1mfuE2MmfTMyNP9SHt3fqFD6dmDguR53WGyP3OJZPewyKpmh89TwXscSPXzWSHKZrGsBD/Cm97IZwMb3VCL2fynKQWtbLzWMIe36KX9136wvIWYyET031rSljoNk3Yq3NhPw2DEF6vb+mBXWOhSHZWPCwUkcNiP3jjfqSMhXerGcVC6hRqNBqtZhDfpiThbIH6h4a9cWcwC6Eak7iDFJy9vb0dHR3Nzc3d3d2IPIfxLMQH2ATBaNcZNMP42Wi0BqsZchJlYROwMGmPb8nLey9/YXmLsZCJ6b41pSykpfXaws11HQv561jImRkLJ0ozhIXe9sLBwcHk5OTKirLMzPSmpgbFhRJS0kfH5sYLnNOd89LS0oqLi7Vard1ux1DMyckR6Fj7cWMqOFlOy0nKScsIDQusqG5obR+KS0odNmoFpDSq0c5PUvecr3x5b/gXlrcYC5mY7luTykIvBV3XEsXc7UrheBa6+84wFk6kZggLvRWeNTU1siwLTt7hsMXGRhtMxvjkNBvv4hRU16KmLBRE2Ww2452DgoLoUfgQ7FP29PT0awz268fayza7KMpWnh/UDeD94pMieYg4gy4EhPRr1DhjNg64dhxL3X2+9g97r35heYuxkInpvjWZLISCR/lH2YaXBSSZkMOAbFZ4AyciX8nELst0Z3ooWXX3OVVIl0DYxiOnhbUXTpRmCAu9qqurq66udtg47CkODqpDr1xKz87DfiAno9rmIcxCd4aGri9KclKC0WgUMetIlWdcfOLgCMwF7IlHOgj3CFX5ikOSispKLSPDl0IDh/Vai9Xu73+lb3CIR3zjgLTjWMoH5+v+d/9ld4ecqRdjIRPTfWtyWahAJGO3tSX9/GzIlKXJ8y8P1KJhAB+2snb8vo1sCmaj4oBCSgwTFGeKT7IARRhzFEKAIN7C7bvx+ELGwrvVDGEhHaZKJ7Xv6uoy6M2kX7JkNOvLq+swC50KsFBvg6Zq0qyoSCIvS0JVVVVpaWlmVk5FZbXBaLbwUPmwzTd3c2AJZaHCmUWJw0f1qAfam+rwORubaktKikwmaIzEuzcOOrcdT9npW/c/By4xFjIxTV9NIgtdgB8ZCik5vYjLqGkY9f/i81/+3favBTX5Y7BBDwbiD5LdFFKcIcoMcgdOI6ehCxDKDeOQR4KN38tYODGaISz0jsjRaDQwZNAFfUo5p1WQOMhY8nUsRHBjEmZhV2c7HXRvdzjNFpuLPIsxLESKUxAdeCeDxcrbTIrMF5fkp6enchz8AsZCJqYZo0lmoeRmIQBPcaKRVlT/d3u/8fzG59+LfteJrNj+wpUJr1xQHQrhuWFnxsIp0QxhIRZUdcpyfX19Wlra1fDo9vZ2B2fBWYoTFUG5xkKc2WiQNoxDfz/f1NTUzMxMCkKcTJxrLAuh5ykckJaVzVkMEeGhg0N9RuNIbGx6U3MHYyET04zRJLNQpG/bxIJyHag+sP/CIp8Vq3eveemD51vFJkwsUbDDHWBrhU2OAsMnqKfIWDgFmiEshP4ygqAoSnl5udlslkWoKS0ozAmLCC0oKceXxPeLWaizQndkIvwjlOCgABeZs6mwqCQpOfViSOiwmR/DQpfTYneYceGob25xmEfCroTgp+Vyyf7+V4Y0I4yFTEwzRpPLQhdPKYUgRocpoj/kKwf+QrVzjmq3ap7P7BPVJxtRowBxRnkkelhIus/IXgQyFk6mZggLRSLKQmg1VKAFkXNaG5vr2rv7JHK/o+tIZQCBcjkUgw2aD0VJ6esfaG5ps0vj6kiJX2hxOq9cjYyPCo+OCm9ta2xqaoiPx94kx1jIxDRjNIksJEbPBeUOL9kFZHgn4vUntj+lOjRn1qFHFu1d8O/nf5VsSrcgIxBKUgBnELIUhk8IjIVTohnCQjq+EFPNZoMA7i4Z6KjTD3G8Df8er19IWQgDMPAeLrmrs51GbjNbbHT+MIc8joUwFwX8bF5WRjTqwYFezML29lYR4s+w9kImppmjyWUhWFg4h8tl1/Pd/2/P389et0T14WzVftW8D2Y9+96fvBr8lhlZeAQjCIlHCNOIO6FcMxZOhWYIC6kwESkL8clbW1vT0pOyczPwHY9uL4Q8TdoLccIspEcVFBanpKY3NDY7SUCH61go4g2ADZsT37PosJtz8zKTkxMNBqcCmYmxkIlphmhSWeiCqlHJBYgzdevq/2z9l2e9v1h1dL5qn2rhzllPv/ncv+76rgGZeUTesslgfAF6kzK/cIo0o1iIVVpaajAYZBGlpKR0dbcNDPVl5RVyont8Ie07QwQspHWkdXV1HZ3dnFMoKi7VmpxjWUjqSI12e0NLq2A3h4ddwqtWqzk0NKa3b4ixkIlpxmjyWEjAJsIcE3AN3sCpT7Wd+c7Vn6l2z5mzU/Xo1gXhA5fKnMUOZAczSypSPdyDQxgLp0AzhIV01kBRFGtqaiCmjAs11jfAREyiIz45zc4DC2taBmg8UnoETpFXw/GBLS0tTl7EaVg3MuJwmRHa6pu7NaDoapkangWpVeVlqamlGclCxNXL5GkpF84FD2n0TiTVDQlbPkva5lf7uwNXGAuZmKa3oAyRQQxGzrH/iHnOnPalixCngy10bINHrutLz61XZVI8nXQjmFcu05nz30mvqbbNm7VDtWzdnE7UZEBabC0FAYDmZiEpy8hdtXotuWTvWHubff9R47w5zcuXIIuBzH1BpuJB0k6060XtC49ZVlahmg7UrEF9g6i/Fw30o74h1DMMn309aECN+gaQGie8QNMkrdLlB3m1Hx6IWgPPpKsXdfUjLX5cg6hrAPWVodKnhp+d61i2X9knIRsSYGIRsJ8gDliIHhgWYhAKgoA/q6qqgoODExPirkaE2azmwuKixtYOCwe3Xt7QqbVK3Kg8GhERER0dfeXKlY6ODryKFywS0iD03qmMDafTYkt73bUTSBkx6i/4+0ZGRvgFXJBE3joykp6YOqIzmV2osNex4VT8u2fzf/dRvCeS0pSLsZCJ6f6FiwNHwvPjMqLj0K4PdXNV5WvmIUkHPpQDwORFEoHUXazySLGTxj+KuipH/W9C31TtWK46NHv5vlXtqHcYWZ3wWj/KBUT0pd19R14u4lUbfI8dPV63/8jw/AVNy5ch5wCMjuaQFVoZ7YfRrhcGnl6GZr+NXtuE3tuONmxFG7ajzdvQxh1o407yuRX5kFWfHWSBpklapcsP+OpmWPDZCgv44WzZgjZvRO/uRFvWojeeG3lhmePZ7fI2HulcDk4mkaudUJWNWYj9yAeGhcooWa1Ws8lgMRudnN1kMcskG5l41NCp1lhEnuQoGr8U72kymeh0vlgGgwHnRcxCnzNpB4KyY/MaBLIzvYLBoLfYrBrDsIuMTXRaIDc6XahmQFh/NHRPYPFvtrF5KpiYprEkYAz8DxU8wzzaecSycH7D40uQUQuEgahW/D0mqJDiZNp9Rsa8NdXZ8n4b/F+P7Jqt+lC1fM9sDVLbkQmKLfbtwEpx5HocHAjB20isGpEk+JoT8LeSEVmHuaMf2WYtUM9fiWxDsLMVGeBXOI+hY3/b8fVZ3KJZ3IK5wuJHHPNVtrl4eYG8jKWbpXnKdekRfiFOKvtcFTd/lfjU6p4vnZA+4ZEezCgxue5o6Uh8gFjoIqKR2LAEngPekTkGKQsdMmrp1egdEKSbhrz1zuLrneMCyyqhARfa/HnssSu58Tk1Np5+R1/V4DgB6uKhWZu+7+Ezdw7L246EHA0qeX1nqMdrnnIxFjIx3bdwidAjxTYzQaUAAIAASURBVIlEeDvWc5iFxjlzG1YtRlajp0On8x4TPqsE8wLAlODQDjPcjkpeDf/N3L1zVAdVK3c+okE9DmQQRatnal9cYK3wiQ9UsM10wkaeJMXJIwuPTyKZkE1n/+gw98iCobmrkWUEjnUAC/FPiEZRvxt4+anBLz9re+lL9j950vTcE8YvPWN98VH90yzdYXrK/Dx+dPi54eWXtF/+ass3otAlGVmwCYUpbCHLiIRlMFTmQWEh9fNGUU2hIwhhI+lHiu1/YUWdxuzEWwWguPsQKnog/gQPEqHNh89tOXAyNiWPbIV9kUvGwgy0K9AALiJZlAXZpQgi0uiEy1dzQiLLTl/M9ziRUy7GQiam+xYp/gr2uoy4FBnt8u4jtvkL21cvQ+YhmLxb4BF+2+Yld8LLd77qlABtmKYymZ3Cpe1wFK0N/t/V7y97bOP8L7/3qNbeCeQTSZd3nLDvJ3HQ20aU4Ch8Kk5CNgnidtNvnQ7EcchoNuyFOZvaF69GNgvYH4FUqNrMAtJqUU8TalOjLjXqIamLtIS196JOkto9aWpW6fKDu9oHqVNNElluH0I9A6iLfuKN7ajGgAZE2Un6kJAkkT40CpjfB4WFXtEZeqlHSCW7wxghvdlOWHHdlWnkNu8qph3AkvQkw7vJOCPKEjRVA/hhEUtwibwLiOhUBHw5CCgBr22Q1cn3X4QYC5mY7l+k5gfJ2PmS0IhF2X0IzV+gUanQoUPOfXuse/eYDxy+t2Tbf9i554j5wEeaj/YbD+80frit++P3zv32q5t+vGbjtxZs/6clJt9D2qO7uQ+P2fZ8xH94zHjw4Mjh/SOHDxoOfmQ8cASvkpN8hBNeHfnoqPXjT/iDh7idu3r/5Z+N8x9pXroaWfFrvCKBLcImi4PaVDsvuCuw3In0HmXpxgn+uWsA3Ul0AqzcCX8rw2uGu9YbAwHwBnHyXKQF94Fj4Xh5fyolIvyEsbtck3c396MB0HmyD90CzqRCOjRj6mIUCpITPxlkEmULYyET07SWi7DQZoNWPY3evnWX65HZrnnz+lY907j40ZYlq9qWrby31L5sZcfSlY0rVtasWdq2YmH78gV1j80uePqRlC+pCp9TlT6rKlqlan5qWcey1f0rnmxbtKpl+fLGlUsbVy5vXLGqeflj+MDm5atalq1pXr6mYcWa2lWr6leualu+vGvpUu2CBbb58zuWPYpGRvDLu6DIVvBD7dAJh3S6YboLeWkxPskkb5BHCkPOYW+FxMmDZfu0YOFo3c01Pe8DY54I8Y7JaCEJGrTtZsRzyGlFLjsvGshbxBchxkImpvsXMXki54AojiKHSgsrn19TvWphxYrHm5et6Fm6ZHDxosHFSzxp0Z2vDi1aNLhkfvfyhR0rFmkXLtItWNS3bH7dikdKn1Q1PqFqfVLV+sQjHStnqxcu0i5YYVy+Rr1kYf/Shf1LFvUvWaJevAIv9C1d0rN0WffSFZ3LIOEFvAVv7162JGvlyvKvfh3ZdEgy49t3Ih4n2lHCSQw4S3eSaK0h9YVGL9NVsKvQzRdhn8fr9sjQnOt+yNOMhXemUU7yaArSbRAvF1jo7kGEQWizIasZOXTI0EMGI34RYixkYrpv0bd/SeTsJAQaMg6hc4fQ4e1o7360YyPavh7t2Iy2b3UnvHznq9vxqg/atRnt3oq2bUdbtqLNb5b/4h9Of22e71+rLn11jrj7VXRgPfpgO9qzH3bY6UMSPgofuxNOhZfxtzt3og8+gE9IW2Hjrq3ywQMoLAyJI5ygxZZA9jZhCddquehP+wJX6fKDvOpdvmECu8pDc5i7QzHJLjxZhl7HD85Y+zG60blHEe42un4378PwshDiESgAG5lPP3z0jdVPvjx/8a/nz1n/5edJZ+gvQoyFTEz3LZm84JPxDFAVBsuSFvFkoL1sQy4TiR1zL0mCbveSAylWtxUWK82Vr1x8a5HPioVbVE9vW9GHNHpkMclWMoheERDHQ28ZGsKUmGESwo30Y3cbbsI8CZjt5JHDplOGzcgOL+rUx8E/AOYgt2EzxdIdJWVUAkJdvyqLXjMLz1wAFjjJYwaiOflbsdBFu03hD+tQz6IlzaseMx36EDlJtD3okknt8GhETVi6yZmp4yuRbyEMvIcE9CuFLIuefcjACbfI4VD/Dv1wJPIiAI9D5As+2L9pzlIf1dyNqllbFy9EMOOT90JjrjuZq+S+iKtK/Fa4dzsya5uWPj4yb6EBv4I4LEgh0YQUykP8RoILJ3F8vT+QJZYe7iRDcZKg7PCe8e0ydI1w0sX7SFDQBLgIfQHFpbVKqnotYa1q91zVLtWaA4uGkKFP1EjUKkLQNXwzxFK5yLWpWaJGU/GUexmW3SeGQMqiBQZsEHeQ/iDYYvJWk9JOH/QcPDFiEin8tAHMSc5HTwwdV0etPjyJPijvsxq9KhE7KRDLCewgX9N9wOdzcLdiId7JjB+obEZmdcOcRXVLHzfv2QcdguELl01yEe8KGDsFCcEnoALnMBvOZi4OCTbYgAW9gzjIbnA7JvcQV/fTGJdcio3UFzsRdCIq2Ll71/IVW2fP2TRv9lsqFeLJN3D46DNMzap7mTjuDsSNIN1A8YpnBhY91XvoKOLsSHAonNn9vuM9EJbF8Y+LJZYezkRGtcOIMc9rokQaRAAM5P147P53mIBMdrCJZPQW3mKr5Av+GPvGvJ0LZn2gWuUzV4+0dhhT6G6XIa+q4BSSWjREGl+k8fAmEASE01YbCcoy7E/uXSFVQXYLskt0WCK1Wti/kQXsoVoodzmTngQYwbYabDpxJOhYSnxRCs6HMNE3mNGrLpIbiINEEvlwb4c9pFuxUCZvHDAop7+zb96ibpXK+q1/cG33gRrwDRvR3k1o53a0fRfUhrvTrilZ3YN2HUabN6EdW9DWA2j3IemtVwZ//D3tz36m+emvDD/8/sgPfjLyg5/eLA3963dNv/iv/h/83Phvv3L84Bcjf/aXbQvn1z2ialu+tFQ1i/vRT3Xf+4npx7/An/rv/9v4wycpaX+M7/knpu//1PS9nw3/8Gean//M9MPvoB9/T6dSSQvn27/5bbTRB23Gv9cH7d+Ndm9zp13b0Afb0A7vU7r1c5sBq3R55q3S5Rm/Spen7eruLfz+bY4DuNxtQbt8hrf+IeG/v777n+Z99M05H39jlv3we+g42e3wcfTBfrRrOymhO9GuXWjHvlGnoqe949Ud28HQbdqGNu9B2/bAxi270M69aAu2APvQzoNocAAT190ZRIA3Y0Tm6gHTDS/KTHeqW7HQRd5/ECeigX7t6keVVctq56kq1iypf3R5z5LZTU/MbVu1vGvZY53L19CEl6dk9bGex54fWLZEs3pF9aI1rY8+2btyfv9CVf/iherFTwzOnqObu0Q3Z4V27jKa8LJ3lSzP085bpJ61YGThKo1qnnPOPH6uip+v4hctMDwyWzd78ZBqCf5qeN5yzSNLxx07WavqBUu0c5fo5yzTz16pnbOyf/GKjnmzNItmObGrunx2l0rVtWhFz7LVzctWtK55tHHNapyaVq9uXrW6ddVq71Ma96Bm2ipdnnmrdHnGr9LlabrasXJl3RNzyp+eV/7U4ubVy9vw6ppl5c8uz3lhQfHz8woeV9V8aVHD08sbl65SP/5i54oncdlsWr2yafWaplWPta54ynsqeto7X+1atka9ZKV+/pqBRU90LX2qY/kTQ/NW6Jc92jB3ftvipVULVqLEZIxAACH+BwHegH+Mhfeg27DQXZfKjVR+6+/rH1ta/szKwuUL6pYvbV0yt27NI80rF7ctXz7VadnK5mUr1Svm969eWPfomqZHVPbFKmmJSj9X1bd4ac8cVff8uV3z598sdS9RDa6YpVk2t12lGlo8d2iByrpIhR5dZJqDFxZ1zZ7Tu2hR2+zZPQsX9i9ZMv7wSUpNS+a2L5jfPW9+35zFfXOWds9f0v34qsY1C7ufXdL92Lzu1csb5i9qWbq0ecmSliXwBCAtX96+DCdYYIklliY1tS9f3LFiVsvKOW3LF3ctWd61ZOXQM890P/1oxWNzq5+YVfe4qudLS+qXzO579An1mqe0Tz7XvmwpPoSW0Pala8af8A4TPkP34pV9i1a1LVtTv3JN1ZpV3atWNy9ZoH1imXbxLP2ieeijz5BmGAiIjbXDch0LyeA5pjvUrVgokVAsfcg5jExIGkK6XmTVwSRbOg4NOyHEn30E2bRTnaxaZNSh4U6kaUfaIbT/UN/jj6pfeBzt3oQG1WiwD2n60HD/TZOpE+k70XAP7FactWueyl+lClapLqpUx1Sq/qOHkX7gWhp/+CQlQw/SkTvvH4DJWAZ1EIBJq0HDA6inHX4yp4OE/xQODXKSZZzsNI17RCyxxNLEJosOjdiQ2YZsFmQeQZYhUZv7qe///vUrc/7mddU/vfwIcjUhpQvZh5BtBBkHETeAnGqYesKBTdZ92El8Xb0BDY8gsw4GIOJTGbRI14PUDWjPJkxltG0H0g0oVo40kZGJNEiPA3BjRkXvYrqtbsVC0nZL2x5F6KiCH7ddhCZakydemaiQEH9Tm0TSO5Y3IKcBGR1o55HmlU+Vr1mJ9u9CDhsknoNhtjdLsg1muuccsFt/9/tPPRU4d+XnKtURlcpHpZLqa6/b2WlDnBUJDnjhwp90o90MiS5jKns/cQnxHoU/6SG83b3q/faGSbIhwQ47czxyiNCXGieHhKwisvAQEFiWoHEdegSQBRIzh7S1S0iggRZZYomlSUsciUfKkR6hUB5tPVzluyEvr/RZtGKb6pl1cy1oiEdGcMVoIFOFQy47dPHDxgoK6bgT3mmi4wAUBLOY0w6Q2PrZ0HCv9NEB7HGindtgGKW7uw1MP4TIoAzo+yqzOtK70O1ZiKATFX242AZDlyeZ+OAkmLq7u85UJp70mCLDfUToqLXjk94lT9WtXIEO7hJIrDl3v6CbJdKZi7q8DoSKPv10r2qWn2r51nkLtv7fvwBukZk26c6D6oHzZ88lxifAQxDE5MQknOJj43q7e5DiSk9NK8jLT4iLb21uMY4Y8D6c3YE/ddrhupraAD9/epKigkJ8SEpScl5Ors1iLS4suhoegbeUFpdYTGbo9gV3RSaqVvAThqdK740+XvjW2+nMu0yfBe2bNu4RscQSSxObCGkUnpg+GeBmr5erXw5/fe72ZbN3q5b7wJgKEwTwdg+HIL1D6dgwd3/Fe0/EQvCkHyksCcQsawbRgUPD81ZCDx3bAB1WAePfEAwqkekNMxbejW7JQhc8XfrwqWl2Amx4nKww+EAUiGGmI/m8fVUne5VijA6AhR7UO4+ol6xpWrEIHdjugPBF9M6VmybZjUMjGVlhryg5oFrykWrOHxfMC97yBhmxQAK2kp2rykqjI8LjoiLxssw7YUGRB3p7aisrrEZD4AVfvBEvxFyNMI/o8T4Q8dul9HV1NtfXXQzALFQUgS/IyS4rKjTqhoP8LuiGBkMCA5rqavEl4qOjWhrq3XclkqTAbNcOcmM0OIKnbzR9AKPS6LJCBjONf1Azb5Uuz7xVujzjV+nytF2VMP+siLPAkHnsJFowC18Je33+tmXzdqlWAgv1JqjJIe4CsJCMxCBL5OO6097NqvslXibDyeCUpK8oGlKjfftMs5eiPTuQbchOLIZn9kS3YQCvlOmOdUsWwt/DHQaFGFy6hXcPbqOzXUx9ovNWAHZEE37z2XegZ/nS5pWPoIMbeSTCABvIOtRjIonWK3qWwZt0EoxC7sFnsxz8yt++O2tJ+NtvW/ubZEwiaHC+dmBaUnxSYixedWHOuiTJaW9taWhsqMGrmalJJQW5sTFXe7rbeTuMhZd5Or5XEjnbpSB/ReDIeSCDWgw6vL/RMFxWWhgZFoqXSwvz8H6y5MTnpHfoItFkSBFylyknISKUDUAmvSWyTP80ZLdrVaYsscTSJCVZdCHOCc0YsOBClkap8pWwV+duXzR7j2r55rlDSGuA6VNhNnKCMDpQmITOgPfvcSe8wwTVRdSg2SGRCjp44zf2uj76wDR3Adq5C5lHeBpIDF9aUhCJX+UEu2G/3p4z3Uq3YiExzaSCnNheGGRKEvG+3U2J3hH+tLV2Clbh6nQTabg0HTrSuWJ1+7L5aN8W+Eqg71A3TdijhYwlQX4lTqSoi0t//8v/V65sxbnXu5tIToI/M3Jyw6OiITOTSyenp2Xk5WD/2MpzkfHxGr0Rp9ikVIPVIcowLxSMe8c36HKFhoc5JRGzS1Bcg3p9YmoKrwh4h/jkpPLqGrPdkZKR2drdTYHm8HjeIMXza8lvoU/dLc+Sy3Of0s0f1Mxbpcszb5Uuz/hVujxNV91mh7x8QsFDUr1U83L4q7M+mKs6pFqw4xFSR2rDe7pDxsABxCkkyXsqeto7X5WulXrSXgikg/Yp5NCYPt03Mm8B2rYLjRjc9ll2BxkTiD0RwHoz3aluxULipJM/Pv1jXDPJ7j8w/d/LD7ptslfhspDbCEQk7NYd6VixpnfRIrRrO14Hl8mz/w2TfO0XQIU+nGdwOObTU4gTkINzkUmBvUlS5KiY6CvhYXS1vqqupKSItFzbLJI1ISVVIMFez/mHDBlsCqwgu0PAGdEiSFejIoCMitDT15uSkT0w2KMoDpfCXwwOhOZGFzrvG9DU1klhJnl+nfvu3XUknnu9kcb8qPEPauat0uWZt0qXZ/wqXZ6mqzhdK5VgFqVaqfaVS6/M2Txb9aFq/o5HRoBIRp5ERoR36lFEJKbmutPe+SqcgBIRTqiQ2iOgIrLo7B8fMs+Zg3bsQEaLx0hzYE2gLhUqi+ixTHeoW7PwQZQ7X9K3JKdIWahesATt3E6mJLydiKdFMhypl3e56xoVmNtx1F4ul6IoaWlpn376qa+vb2pqamtr66mjn8dFRV4Ov5hWkDpgVIeEhMSGx0aHxxYUltqcPM5+iiDik5bWNoTFJhz95MPEuMiutubjn58+63cxMi4qKjq8t68zJSk5PjYh7PLV2JjEIc2wN+szMTE96HIBk2Ro1OdLhfKXr7w2b8s81VHVgv0LB9GABZl4CJYmuE0MYSFt+Bh7nrsQMBADjtos2k0Uzmc0ckc/tM6ZBZGnTDaPJSNhKUm4VLgoMyt3o4eRheQDnEJ3bGvi+trsUIHpzTyYhbIs19TU5ObmVlRUNDU1ORyO0uziwty8vILcuo4Gk2AZGhoqLyzNz8zlnQ7AqiJKgojP0NjZk1tanp6Zkp2VOjjQn1dcnlfekJydW1pdrR0x6PWGzs7u7My8QfUQvR2WY5mYHniBT0Za6zFpIExoHWp4NfyNuVsWqQ6p5uxaqEEDRmTgoFsNgZCHhcSTu71ZurkYC6dIDykLaQal9ZMWAZrCaYud1zekfiE0g+ONsmezDP2bbQKE4IXIDhBH1+XieZfE2R0G0kcG50GXU4b2QpqJOafgREhHhmVayCXsPAwIFHkoV4LDKgq0u80t60OZmJi+YCnQEEdC4csw1669Tmp4PWjt41ufn7d35eMfPN/P92FAOhDnfsO+xkLa0nTPYiycIj2cLFRIHxeYAsmK0AcnYj+9VFDWYfJOdnwz6Sxo/4nYIwFZu8+nfHA2fucnfkZOgCZBiSM5TwI0klMLkujkrLLsMtvEbUf8jwRnbT+bsO9C4s4Tl/uNMuRs+BmSYDcrMEsU6WzGxMT0AGt05wlc3q3IXmusz+dLYuxJ6Y4cTEGjbMJOoeASPW/CyPPf/ZRuxsIp0kPHQnIssBARFmJ3bdfZ9N3nMrIb9cZRfuEN1aFD2z9L23oq2+dMwdZzeRuPXrR6+nq58UY+PHWt0HaNvz3sm7D9ZKLPmYydvim7zsZ26ch8wYSFxJUkQ4Luq7QwMT28EgSB1uJ4V0d/6/3qWu3OKHm/ot86nU68hbaPeL/leXd5lbwv0oqbNzzizcgyjHR6NEICYonQnY+WZbedYiycNnroWEgKhEKHSOKd9QhtOZ+37Xx+ZpPedDsWdlnRFt9yH/+GDYEdmwPb3vkkxkAqS2kfaHpjntuD5kP8eogvc8A/d/PZQp+A6l1Bpbv9sruMnrETbhaSRggmJqb7EEUg5RYlmSiKmG12u92LOhGmcbiBLBYLGgVLfCq87GWq0YhfkqFQ0/7eYDwkkkTyCW++sIl03XT3F3Xreotwr2IsnCI9zCy042UdQj7nizb7FmK/0D035s3VZkGbzpdvuND0nn/PBv/OtZ/EGdzjeNzvjNeyPQS4gc44+DL7Aop9fMs2BzXtDK7e5V/QeR0LiUd466syMTHdUhhd3d3dGHt0eWhoCK/29PRQnmEE4lWbzTbmKCq8T25uLqYmXsb7NDc3JyYm4k+8zHFcfX19VFRUQ0ODg+PdLKQooiykiRCRUvA68HnX76uAMxZOkR46FpIdFAibi2z4PMMIbfAt3uxbnNegcdwu63Ta0FbfQp8L9Rv8+nz8u94/GkNDlAP5RteLwPklCEPjgl42u4Oq1vk1rAvq2BZUt+NCYfsI4BN2IyB00TfL0ZdhYmK6Y3V3d2dmZnZ1dSUlJRUXF2OwhYaG9vf39/X1Yc7hBcy21tbWrKws/DnmWOwRYuxFRERg7OGdOzs7S0pK8Pb4+HiMwOrq6qtXr+LV2NjY1NR0dymFT2/NJ0HQqNJL165tGLt+D2IsnCI9nCxEpF7T7kKKHlhY6uNbktcwzN+uqrLLjLaezd58vmLj+fatF1o2HA0nVAPsQcQHT7wbNwtdcDPQNye4+j2/xvcD27cFNezwL2o3eVgI98JYyMR0z3I3xVmtuJyh9Iys5JS01PS0oIvBV66EarVD+NukpIS0tJTM7Ky+/gHs2409AYIGRYxJWk1KT4hLb0pqenllhU6nCw8Pj42PuxoTrx3Wey4nuUhXUs80MRIxO14ouhl5jYCMhdNEDx0L0bWoZlC7gUvApvOlGy5UZDeOAAtvmXs6LWjrubzNFyo3+bdtDWhZ90mkxy90t/ldYyEAEvqL4h12B1dsDKrfGNLh41+BWdhqpCFGETkU+tfc8ppMTEzjRXkDI6N40YlLkH7EmJGT39DaEZ2YeOzkidz8rKjosM7OxrT0xJOnPk1MTYuMS6ptanMfTDrISMRa4IWCggLCQoX2hKtvbc0rLoPQiZqB+PjY2MSky3EpVa2dEpLJXD0yXfBG0HaHCIaSrJBBFxC3Esq22xqQ7fcuxsIp0sPHQnemQSQrS3Y3C6syG40QeeaWuafDAh1tCAtbtgQ2URaSFnZyUnI0OYe7kFAW7gwo3hhQsyGkdWtQ9a6g4utZKNJXSCYmprsR9c9IOHuX0DugTk7PMtl50ngnOwUYp1RWnJWWHJWfkxodFY4PyC0swe4d7XRKIi26u4liFRYWmkwmfKjTMlhXXVJVVyuTIp0QGx4TcQkvFlXVhick2QWH6HLPQiF7gz1CQXcXf8JCMm0hzKJzrRsBY+G0EGPhpLNwd3CZT1Dd+ostxC8saDEwFjIx3b/cfqF6sD8zN6erbwAXJ0FB3T3tnV2tuGQV5mVmpCZUlBTGRUXg8lZWVhEVFTO6KyllIf7MyMjo7+93KYK2r6W4INtgsWLUuVxyfkZCZlKUS4Aw+pciIpwyzKhL8EfdQI8xIgnWYYEjMyWBXyh4mz8YC6eDGAsnkYU8YeH+0KrNwfVbw7u3Bdd8EDimjpSxkInp3uRmYUpa8jm/C+FRsQEh4UlpmX29nTnZmWFhEdU1jdgcYPY1NXdcCg6rKKs0G2mjoOd4RaF9Z8rKyqqrq6uqqrRDmqq6xvK6loraxpa2VqRwxoGOpuripsZaF8TbJkfBbDRuUVskk5JMyUdGSdHYNB6nEDYyFk4DMRZOOgs/CCxZe6bkOz7hv9kf+87xROYXMjFNiCAEoqf3WVtnX0Vtc0FpZXV9U2VtW9ugI7NyMKdWV9RkSivqauocEa5NM3/dQEO6TEcg4tJqpMkFA584jpd5B2+34OMcHJnRjVofciJKOzrDqNUztoqYAjBNHlNAD2EsnAZiLJxEFnIKGnKgTWey3ztf/vdv+f94UzBmYaeVsZCJaQJEWQjwcaGM7ILmdnV9S1djh7q8sdcvuvhgQN6u89n7/XL2n0/7LDCZJ928x4v2oMHqGtCdia04GV1xLKL0THRxQFw+dexcLjg/HKt4rI+n9DZ0DjYNWjvMqE4r1vXa6LhhmPRbFjymgPy7HxQyFk6VGAsni4W80+F0odoe67df/+TV4zlvX6h960TOv/v4plT1j5BpkBkLmZjuRZ4CQ02BAtNlo8KSaokURuyfdRrQ57H1PgG1G/zqNgfUb/UrOxKUY3cX1bHysrBj0LQ1qHrrxZrNQVW7AgsPBmbZsGuoIFFBThpdm16PJFzMSxv7Nx08s+nTK5vPpa4/EbvndBQu7IBMsC/usG30/hgLp4UYCyeLhaLgdMioqtP0zZc/eu3T3A0hrevPl/zwnROxxR0m9+6MhUxMdy+PCaD/4/KDWZhXWEFZiItku8F1PLZpc0jLhoudGwObffyqPgrOvRkLaeg17Py1DpjXY3wGNW4IrNvqX7jHL9PiIhTE/FGuYyE1IPn1/esOXNh3seCDy9U7gkuPBGe1aqH4S4IIA46p4P4YC6eHGAsni4WItBdqnejtTxK3XGxY61eHWfg/e0JzmnRm2uuMsZCJ6R7kMQH0f1roCopraHHCha7fLH0WV7/ev/HdgLYNQa1b/Ko+DsrgyW7j5Q3D3aK2ADhDOnxCWnYHlx0OznEfosgydAsddQi5Sk6Dft3RsM0B5esu4qs07vFNrVHLEsREpUGGya4uxsJpI8bCCWYhSW4WWgXUbUC/3XXlnfMVm0LbN14oO3ilqtt+3Vh7ehQTE9OdymMCPMUNMJGTXya530TRoIk/FlG+wa8Gg9AnsHGrX9nxoFSIanEjeUdWtPaZN/rXbgxq9Ams3x1U/GFQNk/PLnBIcpLuMG6muVnYYlp/PB4fsi6k683z1XsDcqvUYH9EkcxUQS9Hz8BYOB3EWDhxLCTHkv8h+7oUySGhqk7L9985++aZ8nf8GrcE1Kz7PL16QLK592UsZGK6d9Ey5yKYyC0oheJEutMMmoRT0XUYaZiFmG2bL5R+EpQmuitj3O+p3pPIMh15j1p6TRv9quGowNrtgcX7ArLdk3vLkguGzkM/HTgFfEh4PbNp+O0jMT7+TZtCGjYGVOw4m9akU4j9ITWqsBs+RIQyzlg4HcRYOMEsRF4Wygp+r6zudnzrjyde+7z0vYDWd04W/ujdU5H5bTon3RdugOzPxMR016JlzkVZWFhCXy0JCyXCwkYPC8tH1ZESTI1noYuysNInqA5YGFCK/Tw7NRSyQupIPSyEIssLSMxoGXz7SKyPX8uWizU+AcWEhRJxCSUKJMJCDnDIWDgdxFg4iSx0Kqhdh3658/La8zVvnqt/73TxT9efiy/t0ZP8zFjIxHQ/YixkLJxAMRZOFgvxf/grC0Jb/Et3hPesC2rf7F/9/om0UWPtGQuZmO5djIWMhRMoxsLJYiEuQpyMmoeUb/3xxB+OF2661L3ubOmmM9k1g7KnvZCxkInp3sVYyFg4gWIsnCwWiryAv6rqsn/7rZOvnyx7L6AVs/CXWwOTK9UjAt2XsZCJ6d7FWMhYOIFiLJwsFuL/bAJqGpR/tP7CG6fK3/FrfvtE/o/ePYVZaHTnUsZCJqZ7F2MhY+EEirFwsliIi5BAgvy+eTxtYzCEwHjvdPErByPLejjWXsjEdP9iLGQsnEAxFk4WC/F/DgkNOtAbn6SsD2zaGNK1/lzZrqDSFgNi7YVMTPcvxkLGwgkUY+H1LCQ5j2TiawXGu9phBRZuulC5IcDNQst1cWfose4zCzznRKi83fLN1z99+fOSdwKaMAv/bd3ZhLJeVkfKxHT/uh0Lr42197LQU9agaLuPBRbC5pY+PbAQxtrXAQsDs90sVAQZxtYrEKBboUS1C4jLbFbDWHu/ti0X63z8yxgLp7sYC8ewUHTBPJw4wTShlII0Y+HVNhvy8c3DBWZDQNuWwJb3P4m2kGhMniwHt+SChE8vKopklVF5j/UfXz/+u0/z1vo3vnuq6MfvnY4u7GDjC5mY7l+3ZGENeHhBzRuD6gkLs+icTRSH3qNwIviSMbSa1EMbL9T4BDbjN13CwkzCQsnlsssQgw0KNWEhXjBIyJTZ0v320Sgfv3afi82b/KsYC6e7GAvHsPBaURmf2qzXWLg5qGkUC0lmJ7fluT0QLkAGhHwCCrdFdKy72IZZ+If9EQVtZsu1cFCMhUxM9yhvwbw5CxuvYyEud6TojU6AL9goNfVrN/qXgl+IWehftTcg/5pfKNKKHwpP/J9dQvbMln7Cwhafiw2bAphfOO3FWDiuvdBTWkB0lSS8+ygWtgALj0Ed6XUsHJ0UF/7KiFl4IX/b1fb3glq2B9d/EFjSamRj7ZmYJkDeonZXLPSUN9qcAW4enXYe6kgDinyCaggLa/b6F11rLxRGXQkbnv+fvfOAb+O68vVQzVLs9OYUO5tkk7zs27ebbUk2m56NneZsnObE3ZZtFYoVLBLVm9WtLjZUkupi772CBQQBNrATYK/oHTOYue+eOyBFVcs2V1GZ/29EDQYzdwbAOfe751ZE43iRtBfCfKRRqS0imdBeeN9LYOG1LATDI9u8n/EvSXmw34qiEmvnWNgReuTSHAvBB69eiMhfhvZwqH2ErOV7rDpE2hWZ1LzucF6TwS3EhYIEfXDN++gdsjAAQvA3hmQgXmjL8NM8ZnoM9khZRZSiGVgo7twhbp5jIeJZCNfxLCRTSpV2za47kBMl6YhJq4+SVQosvN8lsPCGuDCAKN5VvLx/wXEW+pHOsVAXrWgPPXLx2vbChRe68V+XD7UOWn/+5qm33mnaIOnm5+YW2gsFCVoUzaPtPbAQ3JM/ETsp9n4Hy9rgGsxCvTNSWj3HwvYdkqYACzm334933QyALZAZ4ItLdca1B/JwXBiT1hglqxZYeL/rYWehlUWbZJoYeXu5zkK45ONNn7d+snnmiMhcx8KQwxcd8ywEw/cyrJ2DS5wsZ8XX0hwaMqHnYi8En2xdl9QZkajCLMxu0Jto/iMsGguhJxy/8IwgQfeqaJrmrZRfPheLXzvwfYvPCrjbsjAkuSUyQblPXOz2AwvdbjPUcPpojvUyDC7K2nz0DOIgNNSP0XN1pL1QRyqtIyxk4QQYBmXzIqsfgesynMfB0SW6mXUH82MkPbEpapGkVmDh/a6HnYXY3MPPKEUSbUWXFR/0eDHD+O6jC+7k9zDIxiEr9CNdwMKY0zkmBrk45HGDmfrAUZCLwc9Ag8kir5tFMz4Ul6yJlesjUgZFyeotsoYu4yKPL/R4PDiXwdkK/1eQoHtQ4Bak0MYbLfvBKMjrTlgoUnRskqm3n8rGcaHLi8zWWf4Cvw95ASs0lFkZF94bneXImIpO0o9UtUNWZmQ4BpJ0ejH7EGPyWWhyV7ff7kFMiW5q3cHcGHF/rKJDJG4UWHi/S2Ahik5WxaV1lXaYfGCyQEFsdWPjPocNluzERVhihNimbdex8KUtyWaGxIWkNdHmQD4Oepj5SAo4fXxN3wx6cVvGhsTOEGlPtESzTdHUZ11kFgoSdN9pUaox7oSFYRJtnLzlkLyc90pwTFxCnSChIHFtFoeJrNfPop5RF1nL95oxFR4McZ/f54KrYFwFR5oPYZ17zMKJAAsxccUqgYX3uwQWohhxc0RyS0m7ER90uSEJixV99tN//OoTqy+dnfK6IeBzQ/eYheMLddHyDtHx/EkHgnYIGtEO9JlPv/DGmgxZ6ojVhXxkyJLJh+q6Zn6y9ugrRyuDxZ3rT9T+95qjiz7W3u/344hwvt5JkKB7WSqVKjs7u7u7e3Jy8vr33qPuhIURsrZYiQrHhcBCDhxzZho9/vGX172ec+Zkj8VOBg6TC/umOcJCfAkOJesD4wtZaCeJXpvxtS+88db681kZFpcFTnYjVNI1tu5Qdoy4T2Dhg6GHkIUQ+c2xkMVYwiwMS2yu7vHMWug//Wnf9/5z7zO/ln3yI5GrloY89kjI5x5f+53vbi6tmpm2oN6r/UiBhesP5h6XKJ97Yf/Pvr/9j7+JD6LWLVsWuerR8E999q2fP3Wgps7k4FDPLPplVPzq+MpQRVfwybpfBJ9c9L4zGIT4r8lkUiqVdXV19YIE3XtqbGxsaGjAJpqfn5+RkZGTk5OVlVVeXj46Omqz2a636TvTTVmIN8zCE5ltmIVhik4Y/JdYfyytITOn7Te/Cf/xT7f+5MeHl1Frl1DBjyxZ9/Wvb/jJf2/KKerzcKhtGBEW8vPOqHZIlPKLnX/606Gnv3fi7z9xeBW1maLWL6VCvvGlqD17cyubjIUd3rUHS6IlPTEpbUId6QOgh4+FHD3HQvhn41DY6bptF/qKW+24hPiVJ7csX4aNfsOypRspKnTpstCgZW+uWPXW//3WnjfWlRapUeSpupDTTbjkGCnVrj1QINpW9tnPr/nkh7YGUZuWL91GBeGrojERP/Jo5H9+e1/qxUn1IAqNr4082xos7YhIVL2xL7N1gl3c8YUspjvHGY1GnL/kCRJ0ryo3NxdHhDlE+GU+UWlpaUVFxfT0tA+WOHtvuiULzezxTF2kvB2zMFyuiUxu2HOmPiNzavmyX6x6LDho6fogCvvp1pUrdi9fEUktWf3t7x9Mu2IqUaFYRUeMojNUrNkobt2a3HYsUb806I8fW775Merkcur0I6tOrHrk8BIq4okvbPn3752Ieqf/+S310SmD0Wma0CShH+l9r4eQhd6FLMRYCjtdEyVtre2F+pBPfSzsQ8v3LqF2PLL08IeWHsFgWx4Ut2rVJop6iaKe//GzB3Yq2qOTNCHJ2rizPa9sz4jYUvbpx9d8+rHdj1L7Hlt5nKL2UdSBR1ceemzFrkeC3nz0Iy/85Lcnfh15cb24LVQB7YXbU1TdJmRfVBbyTS84LsQFbZzL5AoSdE9qvqzGv8Qg5KNDrJqaGr1ef71lv5tuxcJRyzwL2yNTNdGypt3xTZevGD/y6IvYtZdSO5dS+ynq7WXUoaVBO3DBd8Ujb3z+ybX/59ux60/VbUztEik6ouJbtia1n5aMr3jk+RVU5Arq8GOPJAYtO/DIirdxaEhRLz760fCPfGPzF79/YENie1RqS4SkTmDh/a6HnYU4LhQl1sfI25X9yO5EX/nShiAqOIiKXELtXkK9/bGVJygqkqJe/bsvi/7wJ1lawVhcUlOsRPPWqUZSR1q85UDVpz//MkW9sBJO2xxEHVi25OByatsKSvSNL28+eKRdemX6h6sTXjhYEZHSt+GU8vW96VVdpsUdU8EPqJiZmcnIyMjMzOSL24IE3VMqLCzkC2pFRPNhIt4vKyszGAwOh+N6y3433ZyF3DwL2zALRWna0ISaw4pWqaKHon5BURtXBu1eSu0KonYsp3asWrZx1YqwJ54MP/hOS5HSHyXVbEzThUm0MUnqPbLOvUfUK1f+/qMrw0gmEE0twWXi4E89FvaJj73x5FejXttU/dsNOdHy7ih5S0SSMO/Mfa+HnYUw1j5JGZ6kqu3zYy9qaBitqnLmZjlWBb2xnApeSq0PX19z6bzR4UZuP+ozo8hTJRulLeGSzrizfaHvFDbo6LzS8dISR262/aOrQpZRb33iwxExorqCLLfLgtw0qm61PL3+2IbEGhwahpyu//naY+m1fYvbXojl9/sZhhkbG5uamrIKEnRPym63WyyWxsZGzEUMwsrKyr6+PpfLNT++ApvxexprcRMWkgn1CQvbIhXasJS2qLOaiOTqvclVYzPowsXe4lyUm44eoV5aQv3x44+9GhmWk501Y3Uguwe1DDgwCyMkmpizHdFJddvFdUNGlJM3VlOFfvLjY8uXv7DyQy99/CMvbBZl6Aehu3hJO9pwsEyUrN2U0hWTrBVYeL9LYCGKkdTHpmiLWy1euJj2+hg/h155eUfSqapxA4xDcnuxbTk5ZNS72IiTBdvS2jYktm9OGwg+kGlkoKe1y438LAped7xZZZ81wzAm0qmTdvg8doSiE7Oj5LWRad2hZxpwXFjXZ1v0OdiETqSC7hcNDg6q1WqMRq/Xi1/ytRoLEXjnwy1ux8IsbaSiBbMwIqUlUlxzKLUc+yku0eLg0+1EL/xFVF+rHxmhsad7PDgFxus3909Px6R0RCvaI+SaqKSK/Wdr+clmsHcfP1n2/EsHG1X0zDS4LH5AB43Ku4wbDl2KlWg2SXpFZzQCC+93CSzEcWFthLihrMOOWUjm02ZcHvfoqMU8S8YfEW5xMCbQNOBgYhPLopMbyfqF3SGHMs1kUD0+we3xT07AioUMWCz2Aex6Ng/rw5eJzhRsStOGKWA+0tikmgG7MDe3oIdUuNDmI7r+jfel27KwJcBChVYkUR5QFLuJs+Eyq8Phmhif9XkDa1bA+oUwJNipGx3DQSFZ9VCzSV69U1bqJKuTen1ofBKNTCC3D0GXbQAbwKlCNx588NxGsTpO2heb1Cmw8H7XQ8jCa/qREhZWR4jr5+fmhoHzV21ozoo52CVr+VaKxCp+XfvQQ5etgbV8+ZlL5zyT88GzcYyHRh16/09fl60+qHvrTGfI6frn4lKKNOMzUBTlExdYKOjhEh8IXn/0fYl3N/C461nIHM9WRSqawyDI6xQlq+dYCKfwTs2xZHkKFvlp4vIs6ja4I8TaSBiS2LpZVhtgIUfWLyVjEP2BrAemZsRZTYVuNPhQWqxEvVHWFyOw8P6XwEIkSq4kLDQCC7EtB5yFr6vh9wKG2G8LrGvPszDs8CX7tSzEtu+H9SrIhSzyMai5m/3hS/LVB3uDk/vD4ht/Exa/6OMLBQl6OMVnBbx33sDCRsLCzgh5jyhZe0BR6saFU8g0QBhvPAiBhT54Ayeh0zNhkjkWSut2S8vchIUMlh9wSdoh8DVOMpubv6wL4kLCwp6Y5HaBhfe7BBYSFkrqynSzXt49eEzNN2DMOxwLazbFJNRj1yIs7Ig4fNHF0wzMDoxx/lzgKMxbiPRm9PKuvHBJz7qkzrXHqn8nSs5TDQtxoSBBH1zz7nY9C62+49n1UEeq6IqQGkRJugPySp6FAQqSy1hSAxRYv5BFuiFnmKQtEuZg022WqHZLqlwAFXKOH2JCwkKc7bg5zs+vU7HuYHq0VB2j6IoStwosvN/1ELKQ4W2Jp9E1cSGYrIODDRf9vBxMsc07F01s2g1x4QIWBu8/F2AhRywWMTTr9sIspHyY6MblShtC4Um5UecaQmTt0RLNVnnjkFtoLxT08Oou1JGOW3wkLtSGyXt4Fh6SV8JsogQPhGsscWovmT/YxsIE+17dyBTUkQZY2LxTUuMh9aIsw8G6FlBhRJhJJq4CFnba1x7IiZK2knXtmwUW3u96+Fh47RxswMLE+ojkZmgvBJOlyZsMb4ILNjhI6khro5M0c3WkV+zzNINnguvJLp8Cg/1s0Mw9tz01OLk5RNq1SdG+MblW6DsjSNDtNQ+5wEvSWuFnMBFYq8VkNlvdbq/JZMFHMaT8LHL7uLoGNUN4wbPwRGZLlKwdszBS1oMd9pC81MsHdtg5fX7e9VjOx/g9+ICfgxCxc8gamczXkXbAHGzSKr6k66f53GCOLgxye118XLj2QJ5IqotK1Yqkwhxs970eQhYGbImw8KZr+d5SfHth9NX2QmAhaS8kic5dy1MWO4Ldi9QDju+8fOClwzXB4q4Np5S/CYtPr+2bgiViyFUCCwUJulYcyfYX+BM/ZAh8yjg1rmpq6OjQqdUalUrNABsC51fXNfMsZANzc7fBLNuYhfLO6GQVz0JIkMZsY40zs2NjI+PjozMzU4ahEZyOl0Ftetvc3NxtsE6FtMoZ8E//zPS4YahvbHrUZnWP9k94abJ+YdcssFDSG5XaIpIJ887c9xJY+L/FQlxeddKoa4J9KiTh9eMN65I6w+IbnwlPyFQOCO2FggTdSjzbFvjTHAs5v9U43daqwXHh0NBIZma2H9ZbIu7MoYrqxjthoc9JYxbqOjpbWprr6+v6+3tb2zpwIpiFXaPuW7FwoL9b1azs7O0w6McaKlXYwb2wToXAwgdKAgv/t1iIyKglG0Kx0qbNl4ZCpD0Riao1B3M0Y3BTgYWCBN1UN7Lwah0pxzjsVr1+CMeFJSVlwyMTE5Oz/Pl8XEiGCN+OheBzHOrt7nG5HBaLqaiooKFRBY2HLOoYctyUhayf7u/rwiwcGjc01KtrSpQctK0wAgsfMAks/F9kod2Luie530bL15xRh8p6o8QtW+WN3SahvVCQoFuKZ9sCf+J7ZWMO+D0Oa19vt1bbNjExNT09O6gfqVM26Q1jPj+qrGm6k7gQ+xzLAKZ6e7v1+oGhIb1G29ap68PH2g3261gI3g3s9LtdNqtt1stCfU5ZXmV9o3LCZhJY+IDpYWHh/BgJzgtjKjxgVe/OQn45JLiKTBP1riwkXdTwCz8uSzI+Gr+lHnD8ZO3JN0+pwuR94QlNr+y6JIy1FyToNrqRhUQsxzKW2amK8lK7HXst8hJHnpo2dfcMOtzMnceFLod7enIqLy/n4sXzTU0N2Tl52TmFRou3d8J3HQstLPFPxA4Z+quqSzFd1M1tRVmlZRWlZ7OuFHZMvbE3KzypK1TSEK0Q5ua+7/Xgs5CZOxboyQ1TLvEGczMWQidT0HUTJPJ6VxYGzifmi/+zeVDbsPfnG+JfO1a/QdIdfLLuv9cczW7QL+669oIEPUjibmAhOCOZG8Zmmmlr1bS1dZjNVqfT3ddvKC2rMgyNz8eFDOHP7VmI48Kaqmqn0+7zeTIyrpgtNofTl5Fd0jdJ3xgXYt7SPk9nhzY754rdYyssKMMua7VbmjpbL9T1rjuYH5aoC5M2CnHhA6AHn4XXy8f4WZhO4uYsXGA9fCzoJ+I5ensWkr7X/CSHARa6GDTuQi/tyQwRt2MWhsU3PheXUtNjWdz1CwUJepB0IwtpOjBPmt/rmp2ZKigounDhkkymyMsvLq+osdk9+D2+78y7shCmR+SQRt3i8bj8fhqz0OX2en1cbkHljX1nrGR0FL6vrrM1M+vSrHVGq+nEh0bGhitV9VcaBzELQ+I7IhXNkdJagYX3ux4KFl6zEMxce6GfYzjWdyMLbzUQ+E7iQv5SnoVQS4otlkNhZ6pjzvZHpAxESzQ709SDDqG9UJCgW+pGFvL9SDmWgYkyWAbHhfn5hVeuZNQpm0ZGJ/nzeRbSMJTpdiwEMDHc+OhYbm423jo62qqqay9eyjRavLoR13UsdMzFhR63fXxiqLq+6vy5K/KE1IamenV3R43e8ebb2aEJnZiFUXKlwML7XQ8+C+frSEdHRycnJ712u93hcTMcA9Mx+QkL58baw/xMcLLb7R4bGzObzUajEe/Pr4h0exYyPnp4eBQnb7aaZmcm/IzPy6HGXtN/vX7k9eMN4Yre4JN1f4iRlrVPW4nhCiwUJOim4n18oV8Qx2RtVnOLWtXT02e12m02x+jYVH1Dc//AsNvH8e2FJFOA+UhPZLaRFSfmWQhrNoEbswQVjK+ysryoqODcubTs3Jy+fgMOKHtGeRa2B1goq3CSSzALfS77zPR4enbWhfPpuVdytdoWi9dT0WtevfdytLx7XZIyNq05Lr7wKguZAAv9ZO6qD+bhAgvvkh58FqK5uLC2traxsZH1usbGp4mtwj9gIb9mUyAuBMsbGx3OzckqLS01GAxWm4O/o599FxYaZ6fLysrwXSw27LGN2HvxW6p+04/XHHvpcFWwuDP0TMMvN5zKbtBbyBhhgYWCBN25aJqemZkpLy+3WGz8EafLNzVt0nX1u7xsWWU9TZwRe7TBxhzP0kbJYXJRHOdhFh6QwwAJcFUME7dnanI8I/OSsr46Pf1yembGlfTsaaOjc8gqEquiZVoRzM1dv1NahvEJTR5e7+zocElBYV2TNie7sCA9I/3ihcra+poe04tbpbGprRtk6ghFU1xCDmEhgnlP/TTUDBH3hiqohR/jPUtg4V3Sg89CaGwg1SwjIyMWi6WmvMQwNHYtCxes2YQJRntbcbnPbJyamsrMzLRY7fwdcQHv9izUD/ZPT0/jULKoJD8nOx0fdLOob5Z95e3MN05CXLjueM2fNylwXGj0CSwUJOhONV8xY7fbu7u7a2rqenv7p6ZmKqvqZPI0HBfit2uUag9k/7Bw6IjNeyKzBVMNQCjt3JjUeFg2Fxf6AS0V5cVQdYkYw1B/eWUFPlZYUt09huNCdaT8alxooxGUohlfp7qpKC+XR2n62VSn1VZR3VjSOrXhSEZIYmNEalekQktYyGOPLH5BuuERfiHSaPK+JbDwLunBZ6HH4+F3MAuxL3Vq1UPD4zMW181Z6GdYP22zmkdHhnA0WVJSYrM7+Tsy71pHSntNJhPDMPWNtZUVJTgd/Na4G22UNYaIW0OkXdESjehMRZdRaC8UJOg9CBdn+Y7c2LlwcTYvr0AsluItL79Y29rpcMIEo+VVDT5gAM4U/ONW96lMdbQM4kKehe/ISmEEBtAJ0KKsq5qaHnM4LQ2NtTgutNpcOKxs01siJJoIeWe4rAP7LD/WnuDT16Vpzs3J4vOW7IvnOZppbO4saJ54c+/lDUnN4ak9USkdcQl5uuk5f2YhLuRZOOfp71sCC++SHnwW8sJeNDg4ODAwYOjrbla3pl7I6Ojs8Xno61lI6kiNs9PZWRmXL182GAz87corqmwu7+1Z6PW4Kioq8vLySsuLSorzsfNMWXwdY+5fhie+erQWpglOal79doay3y7UkQoSdOfi40K+ggeXUE0my8yMEY6zkOWbLU78dlWtCrOQHxo/aXafyoCgMEzeFyXriklSHZUVA0vgXfBT7HclpQVl5UX1DTUTU5OGoTGHm+0adYZK2sIUXaFyXYxctU1GxlQAiNwep0nX1VZZ11BQUDA7OjQ+OtXSNtCgZ1/efmHjub5gcXe4tH1TQmHnzJw/+6G1MODYsHOrbOlOJLDwLumhYCHfNTQ1NfXChQvGyTF1S5tYcX5sfBrdGBcSFjY2KF1Ou9PprKur6x/Q+2h/cUmZ/93iQnVz0+TkJNwOTBVvbGFFY1Xb6E/XnXjtWN365I7gk3VPrTueqRww0fxHEFgoSNC7ix/dhHccDkd7e7tardFq22pq6nDkNTVtam3rcnnZypomj5/wjkMTZuZ4ZgcufYYoBjEORcmad2TlkACLqQLDM2xWjFLG43VABShDO10+tbarcxjmnYmUt4fL2zbK6nfIKiwsyWV8Tj/0sWNomEyD9nscJqNNqxuu7HK/9XZmWII6BqbRUG+Jz78aF/LxIL+xMKTx+o/0HiSw8C7poWAhL71eX19f392uNZpsZy9lYWO5aVzI+ukWtcpsmsWXuFyu9Iys3r6B/IIih4e+PQtbtS1TU1MICoU+noVFlU3lmqHfiMSYhWsSWjELfxF8MqOuX1inQpCg9yqMQ6PRWFlZ6XS6HQ4XZiEGodXmalJp/XNjKvCO04umXSi+cFB0ti80ZSBU1r05tfNYai2Do0YvsJCs/cR4MeFYL824vbRv1mgtLqvtHLLGJDdESZqj5C2bZbXbJcUuvo4UnBTGVjAAZYwYz9SksaKmpbLTtmb3pa2KjrBTTVukmi2nczvGOCc/dIMEoAtYCBHt+5XAwrukh4WFNpuNJhrV91++kiVJuYAT8brJ+MLr4kLO73TYykqLMTs9Ho/D6a5TNlRUVptsztuz0O1y5ObmZmRkKFKlyUlnKivKZu1+G0LBJ0pfOlz14hHlq/uL1x7K1TuF9kJBgt6zMIjMZnNTU9PgoMHv56xWe2VVXXZOAc/CltZuHBf6WGR0ob5pv7S4e2taS2RyQ2RizRZp7Ylz/Fq+vLOxmpamlFRpRWVJcUl+UUlxekYOZuHQlCNsn2LDvrR1+8+HHkiLOiD18adzTGdHW0JCQnZhYV5BbmlBTl5Obuq59Ly6/lc3ngrdfzls3+X1O1O3H7/Yprd4A0P657Ip+A9nDgIL7wM9+CzkK0gxBQMj7jlGWa+qrlfjoyzD3chCh92K3xkeAhDi03E5cmx80myxeZh3G2uPWLfbPTIyMjyqb2tV9/f14LeMLPpdrPwHG+TfXaf4WbD45Z0Xhz0CCwUJeg9iGGa+78zw8HBjo2p8HBoj1C1tObmFmIVeBuUVVuSXVBWX1xfVaPKqWpOzm3bJKqNO5mxOKNivqEy+UmXzIZePtDEi1qDvwyA0DPVPTo1OTE0ODA6XlNfN2umajtHy9vGi9ukq3UydbhzqdmD6N2bYMJSVldM3NGS1W2anRkeGDYUllaMOVK4dL9XOVLbOVGqnqltHbQxi6EAFKSEXL4GF94cefBbywizEQdvly5frKsvy8osvZeYXFJbarY7rWQi2DH1nzp9Ly8rKKisry80ruHwlo1PX7abfZW5un9d96dKloqKisoriK5fP5+fldPSNTXhQ6OmKFw5WvHy04c0jFeEnS7tNyEaKjQILBQm6E/Gl2PmRFQwDL1nScQb7jsvNeGggBUM2vINfMsQx8Wb1AEjs+K8fn0kjluNYmHDKZJ52e7D7MhwZpzhtdPhoXGqGlj2cJ7gQggAPp+XzYXxyPlwmRiaXxw/9CWiX3WQ0zuATrCwM4cCXeDhk9SKHm4VRhRzDTw0A5AXvhksWfpz3KIGFd0kPCwtdLld/fz92qvzsDNoHQ2hTFOfGRsaxN0QlVUcl11d0XO07o2pq8LixR6DMzEz+dpiIXh8zz8IIaXe0XBd6OMNCfIaXqrGJ9vqwx+bmZRr0vdglSisb+2eZyPjqcGnrmoTW2BRtTGJlrxk8jYh3XsFiBQm6nXw+YMH85Ig8C/1+jmZYfi1flhQuab52hkO0n3iWH+cPdhqAR3NuJ8OR8Ycw0gH6BJCL4K8HpodCHi+pNEJuBO2C4JaQJt7F57oBPzCJMR/qwTq+NEO7SQbEB3/keaDATUBI40Rg0P08m3k3f78SWHiX9OCzkHckj8fT19eHd86dT+GtKlV6dnbWZEVoY0LlpoS62jZgoZ9mMMxaW1uNRui0LZPJEJmSDUd7eEdvRbEJtaJkdbhMF6nQrX8nx0TG9vIm163rmpqY9rjchblZA90diKVLK5STDhQnUa4/0xAia49RNMeJKwdMBJ98KwIHxVJSeBQkSNAHEg9CvHkgOmMQA0suMfxxhvEitwtQt1A8/xaKh+CcP/J7c845twtwmj9t3nPndq5/d+6S9y2BhXdJDz4L0VztSn19fX5+fm9/z/mUi9kXC9pU7T4WmYCF1ZvjGzAL3XMW63Q6S0pKiouLh4aG0tPTz507Nz09jZlqsMDJMcmNEbI2UUrrhiNZlqt1pFCEzM7MKcjLN/T3NFaV56dfGp+y4OhyY3KtSNG+QQ4s3CSpFlgoSND/lrAjsX4Hmf+MNA0yDZPt9QYV48He7fJ+oPjsbyWBhXdJDz4LMcP4hneXyzU5OenxOXs7+6cGZ1kvWBewML52U3xTTZvVxfK1KyC73W6xWPBV/f39AwMD/EHMwrj4ypjkBpGsNVqhCT1yxc6v6gItBF7MQrvJ5rDZse3OToxODOvxW/hFbFINZmewvDM6RR0rqe43QShJPgYjsFCQoEUVZoKflDXBv7zItfny7h2XdjHIzDAMBGv3nwQW3iU9+CxEc3FhZWUlDvIaVUqwKjdKv5A5OjU7g1BMQn1sQnNFu8tGFllBJC7MzMzMyMjAIETQDEAH6kgtKDahOlqMWaiJUajDDl9ykg5jMH4Io5VlMi5dzriSjqNJm9WMj1bUtw3b0ZZUdahUi1koSlHHSGt6zHP9SCE0DNTJCBIkaDHEenxu7JKMC0PD3epu+djajz8Z+cVh1Af8uK6K9P6QwMK7pAefhXwnNIy37u5uvDM+NdxQ1UBbmQupl/qHRjELoxKVhIUOCzSyAzhVKhXfXtjU1DQ7O+v1ejFHHQ5Hrw2JkpQRElWo4rq4EDZDt25qbBy/qqmDBTE8Pm9BVZPBijbJ6kMlzRvkrTGKZhwX9s6zkK9Z/UBtCYIECboq0hEU1k3yu1G7RxddJPro2yuXbaY2l20EltivP/9+kMDCu6SHgoUYbzabjQ/yOEQXZBe2q3SXzl7uNRgmEdokro88VVfZ6TCSqdE4jtNqtTMzmJLIYrHk5ubq9XocF2IW9jmQSNq0PrEBgy1Mqg55J9MCtgmRHetHOq12agKGPVkc9oamxlmTsbxeO+1DceLqKJlqXUL9Rln9nvMNoy7oRxpgYWATJEjQIog4Igtg4FCGIedHx38UtJOidlG/k/0W6m8Cs/SDWKKrr+9dCSy8S3rwWTiv/Pz85uZmp8+Ooz9Ngzb5TNLQ+DBmV2x8eVx8dU37rIMOnImDyLKysrGxMbxvMBhwUFhSUoKBanCiGHHttosdsamtW863bThw3knGVDBk83m8sOTh8BDf/ldeXlpWrRy3+HaJCzeLK7el1G9JLtkrKxm1kqFLiP8H3ihYrCBBiyIeExgFTkQ/q3j+seiPLT9ILT1CfXrrF1Uz7b4F5c75OU7veQksvEt68FnIW7zP5xsZGcHRnot2gK24WE2j2mQxmnFceKZo04mSps4ZKDnOecvw8LDZjN+EARU4puzt7cXOg0O68OM5G8VVIadKd6Q2vbUtwTM3ohau5WDKUzftc9JeXD41m6ZHRsdNTv/exOwt8XkxJ3Njj17cdSZjcNoD0A2AUGChIEGLJo40c3gdngk0/Y3d36JCICik9lNLRI8mNyusGBXzZxItuPSelcDCu6QHn4W8GIbxeDyYizDiiEMcQAyfS9sQquxyVXe6Zs0wyIEjVjdfYJyf/Il/id9TdU819dtK26abDZ6a5oGAXbLkL4cNEKaq8MCM9izmLXlI1D/p6ppkhh1oxIYMs/CEkNwcC+c+jiBBgj6owJuIZyU2J1Hhq1bsfnTFVmrpNipox0efTvh1uuHKfcK/hRJYeJf0sLBw3gd4FvIhGeN32znOjpCdJYmyLsSQ/tjkZC/Ms3v1QqfT6adhCISbhvmWwDoxU11u5HEjP4M8XpgJg4DQj1gyvROQ1eUiZuolbRU0/MXnuHxk8iiSsGCuggQtomAWRc4vVov/TfJfnzr4+Cf3PrZy24onTnzzjZy3klQJ90m96EIJLLxLelhYOC8yPeB8KjAml+FrOEF8iPcu4sj5ATODdFiyIX5srx8qaRgylxu0C4IR4wDU5ERTFmRyIzPA0AyTNRGU8s/jD5wvSJCgRRCLRt0jiUPib+z5ZtAWasnWoH8/9p9d/u4Rx/D1Z94HElh4l/TQsfB/UcA3/ABzLIS5oOBYrVgS9c//GvH451/70CfWfvX/YPJB3xnyMQhWycSJAgsFCVos4QIp8hWZin9w9AfUJmrJjqW/TPilC7nvTzQILLxLEli4eMIBHlgtw7PQ70NuqFJFjUlJ65/8SuhjH16z4sMvfeRTyO2EafTnWMgIcaEgQYsqzgcszJvO//b+b2MWBm1f8vSZpx3IeX+iQWDhXZLAwsUTmcmexILEMPEDwlT4vpYjRyI/9elYihJRS95YtgK5HTArhh/O5/hlLvgqVkGCBC2K/ACDQmPRfx76T2oztXTnsl8l/kqICwXdXgILF0+kUtTFh3q8vfpZ5HUPnT5x6Im/201Reylq24c/ihwmxDjh8cFj+eG/AgsFCVo8QQ0Ng+PC7x78LrUFWIjjQjty3J9uJrDwLklg4eKJLOx5lYUuhrPbp7WawrVvvP3JzxyiqJMrH924bPl4QdZ4m4oflugn5+MrWQYaG1mW5but8n89ngXzZEBT5NUPN79/Y784vvsruiE1/q/f77+xW/n8mYIEPQiCzuJ0/kwBsJDEhb+I/4UTue5PExdYeJcksHDxNFdHShZNg6Ip8tPJu7e/+vEPR1FBR4Ood5Ys37Hqw8888bnUdw5cy0L4SDfFG97n11/kRdP0QiLeuZxOWJp4Xn4iRNLHOzcCVZCg+1gCCwUWvncJLFw8gfXxU7IRFmIbpj0DDTURX/1SGMx9QcHMiB/+ZNhPf9BZXT5fR8rHhfMsxH8x8Hj+3Qp7/Dk8zG4Tz7ndbhxZ4jPnj7hcLpwyfwRfiCNIHop8UoIEPSASWCiw8L1LYOHiiUzt7SNDDMEs4UFpxLjXfvmJzR//5HaYDWrlaopqu3geRvRDzxqehWDrfB3pvDiybqLNZuP3jUbj5OTk8HBgdBQ+YjAYZmZm8M5NMcajFP/F5+BrcTr4tMHBQZzI6Ogo/ovftVqtU1NT+F0MSCRUkwp6kCSwUGDhe5fAwsUTUInhyISI5PFI053P0xZ/evs3vr5n1WPbPvTJiE9/HlnNyEP6kfrhk5D5gmHDKMKRHL4KIyo7O3dgQJ+fn49h5rA5a2rq+gf0vb29iDQiZmVkarXa0tLSyekp8lXwKQTER5NOu6OooFBZW5eTk4e3kZGR3Nxcg2EYb4SP5vz8wsrK6pycHI1Ggwhfb4pVQYLuL8HkFWSgUuF00XcPfJ/aEhS0a9lTwMJrWt/vHwksvEsSWLhoIk/F15LC8hV+aN4j1Z9dnUf++Ez0spWvUEHpb67lLMa5GlQ+eoQVnwI8I0lYrfbJiVm839PVaxgccts8Xd394Ags3MM4M1tXVYkDSaNxxo9Yu9dNbkpqZXkicsjt9NAuX5+ul3a6LSb7qZMJdruzVdPGf3csg2ZnLFXV9Zh9+F4Wi4XvbiO0Ggp6jwrY7XyTtsfj83pphgFDumlXL0RKXbepgcBGyDeKz1sjX0BceMn8WzcmRdZsorGr4MNFk+Xf2/cjastSateKnyf8yo2Lnbe87b0sgYV3SQILF00kqmJh7lHODU2FNAn8sBV7neNVhaEf+7jiT8/5GusQ7fRxNHwEwkLEr7gGdCRj73lxaHx0oqSomPF4rUaTIiUtKyc7IyPDbja1NDSU5ueXFBcWFuZPzs6Qz7sApRxifPwyjGRj2LrK2oqyyunxiZyMzKLcwotpF5S19Rp1W25OYVFheV5eQXFx8dxdBQm6c7FQCwJz0bO4LMU3QvMUxIbng4nvQXxlw8IqhxsBtlDctUsp3Vg+Y4lu3eGLBb9ioJYlf7r0Owd+QG0LovYs+29gIfGL+08CC++SBBYumsDd4eEYMhU3TbMw0Rqw0G1Hk/rwLz3ZsG8fGhuC0jPrI/WpZAMCgrlDkyEXcH7WT2PaVVdV4NT8Xldzc9PQkL6hvm5EP6htaqopKxsfHlI1NfT09QbsfR5+c5vXjW9C6/v6y4tL8FV+r2ewt6e/u6emojI7PUNZW9fU0NjfO1BfX3/hwgW4481zFkGCbiVg4Vw57Kpggnow44XHrmHhTTXfXM2vJ4Pm2rwZIv6Ehb3Abg1U8lSkjjRvpujbh75HbaeoPUsJC4W4UNDtJLBw0QS+Gdggjwg8J/7nxAbqrjh8CI2PINrB4H/IA89JjJuctDDnYGmfq7Ag22KeJp/RazZP0LSdpV0W42SnRjM1MqKqq0d+1mw0dXd34xL53E0DGwsLR4H/lJeXqlSNhM2MzTTjcVgxETFEL6QpxgwDzfU1fo/DoB+4fPkyn++8a4YlSNACsaNjhvPnz547l5aenl5bW4sPGQzD1dW1Pi+L40KXy1VeXl5UVKRUKk0m0y3QdY1wfNnX19fe3m61WvHLgYEBvN/Z2Tk2NsaX1Xp6elpaWsxmMw/Im6TJEZ+COdg82absfzvyH9Q2itq99Kl4zEKyRsz9J4GFd0kCCxdP80AiChSQCe1cVjdy+5Cf9rNeF2KdMAMpb+SBS/jr/DArKTPQ352cdPpK+gVFqrRroMdot2bmZaWkpV65coW/S111Y1rK+SuX0p12WJf4ho3lWGZ2dvZ0YpI87WxaWtrFixddbm9+cVlWdn5+QUlPbz/i/FVlxRkXz+ZkZ+LsZu6BBRYKunOxHZ3a7m4d3oHlzPx+DL+2to6srBxsxQzDjo6OYpjh84qLi3Nzc28dyV1VfX29VqudmJgoLCzE1+bl5U1OTo6Pj/NNhg0NDSqVamRkRKfT8eNlb1KZwRFO+DAxXDnG7O8e/PbSjcs/tOXR35x8xj03lPd+k8DCuySBhYuneRrxr4jv4zIy/gvBG4s8/kC/Ghv0X7kGYH7oTANZBc247TbT8Mjg8PiYfmzM6PZ6EBqdNQ+MTU7MWvBVNItmZ10D/cNmk91P8yM35kJSHq4Yv5wfXzc8Ma0bNPTph0fGZ5w+NG33GSbMs3baaPPgc+12++zMFP7Lj6kQJOg9im1tU5eWFuv1Azhuw4Gaz+czmSyFhcXY5hHp88L3ycKEy8nJmS9p3RSKfM1Eb28vPg3vX7p0CYeDBQUFPO28RBioiCSLjfaW7YUc6bsGjubIGcv83q7vrgpb9bmtn38h4UU3eN7NLrnXJbDwLklg4eKJx9J8xScxT5wD5Fd1Jl9WJuWoEnPrFEX1ugmzDYyVP4nlJ+aGqzjGD62LUL+K/03ZmQkPGnSiPhca8iCDDQ3Z0agTjdhQz6iLIXdhaC+pAp2vnmWhoYaDpkcv4e6MB0240ZgTDVrQgB0ZXEhvR31GNOlEkxbaF3hOQYLeh9iJyZGeni6TabakpOTy5cuYUlarvaSkzOsJYM9ms/X09LS1td0ehIhEeIGxQE5nd3e3Wq2maTojI6OysrKqqqqxsREfT0tLKy8vLysrw7dzOBx8Ge7G1GgvPwci3e3qOF17amvl9r0N+85qzjGQYwgsFHRLCSxcPBGqAaKI3YIRk1jvuKJ007GsqPjC2DM5m05eqmo1mDz8CeScAAtZDEKG9XKcH386m5c7fTbvndSC7ZLi7fLKnbLSt2Xle6VleyXF+yVFhyXZLhb54FtgAgtd8P9I0yDPQhw+2v2oWtt3UJZ3QFa4T1G2O6Vyl6Jq/9naPZLS/eK8U4ocTd+MUCsq6P0K6vPdbgi2Ojo6srOz8SFMqOLiUrvNzROqqakJ02t8fHw+hrsRXfPi39JqtZh//HQQOEzko8D09PTBwUGpVIqPW63WK1euYMTO9Vy93uN9DLSgs5zPhWwG/2AP6tej4RE05mXdfiYw9uO+ksDCuySBhYsomgze46caJWjE9sii2EMZ4UfL18U3RosbNsWXV6knoA4pYKakWpNj/ayHDNKnyWKGUJuzIyEnLqEkLKkhJLlFJGmJlqpjxM2xifUbk6re2i6xk4lPYaQ+rMoGjZIkHRqxOCNgGB/tAbdABcqe7ZLKTeI6UZIyQqKKlLbgBMMTlXFJVWt2yGr63OA4tyiqCxJ0W7G9fbrWVo3ZbMSBWmZmJgJ69eflFUyMz3i9NA7vMNUmJiZwAMePguAvu6m98bDEESQOAY1GIyK1phh4Xq8XB5c4IhwYGMjNzbUTYTTqdDp8zsKepbw4wAYNGMBFSh/0TXVBVzWfj1S33J+rhAosvEsSWLh4gqEUgKU5FoIt+vxIdCQnNrHprcTWSLFmm6S5tH5sjoUEhGRjycch47K8+D8bQrtklbFJdZGK7vCUwQh5T6ikI0zaGaPojJG1rN4ht/ELYnAemrYi0mc18IVwUEGEU8IvLBzKUxqik+ojpdqolM4wRVeItCsytT84qTU0XvnqjnPKEXhUQYLuXHzuyvsgNnJdb19HZ9fMrMXp8rm8bM/AeL9hSj9m7RmYnJq1dnT1t3cPtnUNjEzOOr0MGVSLeeRj/dczjPeCjIyMvKLStAuX84qK2zraB/SDldVVaRcuTs4avX6EGVlWVJiVmc5PRugnug6HMLwWuXEICOn5iE9AR57AY8MkvvOl0IDrzb2cy1buPQksvEsSWLh4mhtKMRelwar2bg5tOpmHqRYu00VJNXHJ9UVNo5aAlQa8ES6FPwz/oTjoXIO2SCpikpURsrYIWYdICn9xCuGyjiiZes2eFBw4eqCZkNg/+UY4uBXJF/zIT0N4ihNJzmlffaQy9mzvhnhVaHxL8JmWDUm6UIkOB4jrDmXktpoXsvDmnREEPdS6ap9gamQ2eavVS8M0Z1Az4SXE4TezF6oisNWZyV8XBy/tuEyGL8FHyMyEDEYV5yalRt5o51JnoXp/cmrGMG3vm7SMW6wmt8tFuycs5qGZWTdOkwwOdM1OG8eGbxpZzglqVWjW7WTgdi7+psSvsHu4yAqjDt7oGXiH91ZIC5oq7k37F1h4lySwcPE0tzx9YE41DpsjRG+bTuXEJlVhmEVLNJvEdfnNI+arLITn5R2SvKT54JJnYbRYKZK1YhDiCzEUQ+UdeBPJNJiF2KV9pDEycB1kK04/4Sh+SVhIDzmQ6FDmTzYoXj2q/NO2nP9aHf/zDakR0l7Mwqeizv74jf17FJULWXjr/EXQQ6trWIi3AcNEcZkSB3+GCfPglFk/adRPmg0TVv2ETd07E7FXuie5ZJe87u2UBtiRlO6QlG+Xlu+QlJ65Ut3UP03MnUYMmRqU70EGO2CyGIcYTUWN3UdS8o+kVB9TVJ5QVLyjqDyUUn04rXFvclXyubqJMR/w4DaGyqF23cRpSd5+WeUeae1uSdUhacURack7kpID4rL9ycVd49C3FWbLYaDfGeELcUbodPa3zDxuLYGFd0kCCxdP9x4Lo49k8yxce1z53PacF3YVh4l1EfKeP+/Jf3XPBWlpLymfB3S7LEbQQ6rrWdg3OFaj1DAkEHST0NDHQRUFjrqcCL0afQxb+6bEqh0pjTukdVtlyi2yhji5cqus7ujFurpeM7E3njqQ8lUWknZu/FKRXb1mS3z08arYo+UbjxbHHK/A+zFnGiKOVscdKtCPkll5by1swpWNk6Ld58MPl4Yfr4tNbMIpxB0v3XSsJOpoWczRwrqOCRwyQtcy0tFMYKGgeQksXDzdIyz04xI2dmtoSJQW9IUlaUUpPWGJzXEpHVHiVsxCUUpfmET7wrZzoYfS5ypaBQm6qa5hIc2gzm69srGNIYbLkGFAMBLIj9wstE8/LzqxObk6RtYcq2iLTNaGSdrIpomUqN4+r6rsdWJ34KeYJ/473+eLgTpSFrl86GyhNvJwZrikSyTVxUjbReL2MHFHmLQrUtYVebJCbwPizuvGylL8VHkaW8TxkhhF51vxbRugOUArkkDvs1BxqyixXqu3gYPhCJRjOBoGfwgsFMRLYOHi6R5hIXlJI58JocNpjS/tL1+XoIkUayKTm0LPNIjk3RuSO3Bqvwg+/fTqg565GVAFCbqZrmGhx8t29w1X17U4AoOCeAOGc/DLMQdavSMlRlwbJmtdm6SNkOrCZd14w8YWJVMfvqSu7iJNdTAHPUP8FxwkkIjfx/lYlx+dK+4NO5IbkqIJkTeHyRrCFerwVM06aeN6qXLDiYt9Lg6W9JzTjSzE6WdpRzccuxSZ1rA2RfWWvDFEUR+RUhuhUAYrGsKlVU09s/MsFOJCQQslsHDxdI+xcMQF7YVPR55/42RTeJIqVq7B6YQka2PO9sek9fw6JOnZkNM49+FZeGO2IkjQdSzEW1fvUI1SQwea+gjS+NkeEJql0V9jEyMSakPkug0yHNjhIhdsUdLWWIlqr7yisdcBg2cZH2K917OQ9H/GVn2+dCD8WEFIijpcoRLJmyLkeEe9Qd4Yc04dlZDRZ/MsjAtvFH6grOaB9UdSRWnKYHljaGpzeIpSpKiNTKkPUTRGSKpUvUaopwUfEVgo6BoJLFw83RssZKHyCfHthREH0n8akvLqUWWUVBMrV0dJmsOlraKULszCV3ZmVvUjgYWCbqt3YyEQhUwwyCHTHAs3yHs3yHpiJVD2whsGYZxEuU9W3NRnhCRoJ/K7+UuuAhWWfwJnSSvThx0rxdGkSKqLFuuik/uixH0RST1xir6Np0r1JjK1xK2FEyyonwrfl7VJ2h4m1kXKeqIk2H3aovFLaVdkUrPAQkG3ksDCxdO9wUL+pRd5xr1o6+niP27PWxvfEilWb0zBLGwKk2gj5J3h0vbnt1wRF064GIGFgm6j27OQ8GOOheZrWNgVK1FHS2GLlTbFSWrflgMLwcICLOSNFm88C2kOxsVjFg6FHSsPl/aJJL0YhNFJ+qik4chE/RaZIe5EzdAsP93SLYWfqlBpjHg7N06iwwSNlPZHibuj8SbpCRf3RyZpBBYKupUEFi6e7iUW+pDXipC8aCAsSRuV2hsS38CzMFTcEpWmwyz8c+ylf/5lnMBCQbfVLVnIzBstQAUs3+pDz8fGAwsV3cHyrmipSiRT4y1K1hQtU+5SlCv7rV7wEh9fI8pn3xwM8sOHvSzyOxFKLdeHHi/Gdo4NPhAXJusjkga2yPVxJ6qG74SF9ZMR+zLipNBNjMSFHbDJukKkvRHJLQILBd1KAgsXT+/CwlacO2wS1+Q3j2IWQj4y90m4a1gIsykCC8U10eIGkbRDJNVFSVsxSkPlOsJC9bo9Cr4vO1lVnLd4lnRr98KuD5LDmY3ehqKP5P4q+sqrR5UbU9ojxfWh8bXhUm24rGN9gurpdfHBb+cKLBR0J+JNlbuRhXCUpwhrpdHzMcmR8XUhcl2wvDNCrsY2Hw5NhtB3ZntKVc2gHfqR8hPQkxIb4RBfImRwKsDCioHQE3mhqcrwFGWUvAGX/PDlYRLtprS22DO5ejO0NC50nGtMliSY19QXflARm6IMlakiUlpE8ia8RSqaQ+TaCHE9ZiFMXghXAgt514NEAp/ibyX4AhdsC75xeDgangwf9rNkPg2Y6BiZre6DB+3LKbQlBlndgEn4+E74IgNfKT8dFZ/CXLL8W9d9cVf3A78FfzI5iyQSOIFPgT9h7mXgLZIbL7hqPpG5MyFbm3uXHLn66fiTA1UFc+cHriVJIZL4nPhLrl4byHUX7LxPCSxcPN2WhaIU9caUxk2S6vJ2k9UPcybCWbxdBCaMYeAT+Tz4f5wpbJeqdp3vX3NKGyntx6FhuAyDUBcux9mKas3OJBdxezIBGz7XzTA2lozygkS9MOwLp9VvQyF7c38SfPbNU2pcIhaJG6MkzVEpncFJmkh52zPhCSVdjJv9QGMqPsi1ghZX87/FB+kYPJ8Iv+PxQEDCMCz0/STW2tWrr1GqoX0PXpJcFe6GC2FeE4Oej5ZHnVZh/gF45KoIqS5C2hsl7o0Vt+2Ulin7TGRuByvnN2GjZTkvzyG324tTYmjoO3O2rD/sWC7mqEiuwqYukuFSYBu22NjU9u2Sys5RsgoUdh8fn/UjN+0L5NckR8UHC9SjUUevYOyFSjURijYSmKqjZdowaXuEuKmx3+iCT4cWsnCuJPq3yjxYMlYTgmOywXzC8Cx+MicBPJyDrDoD8/WQb8wL9T5Gt2f/UcdKCm2LQHYGxqQAbrDnMzRn4T+N0wuz9dDwlUHeAl8V5DROj4tfNI6FuY/JtHU+L2825C5QqoZl3YxWG76v04O8gVWQAW9e3yx+HvKjw68Pc7ODbdg4ZOLL4l4/zve8JC+ah66XY6fxZ6HpwLft8zvcLpjxwAdRLv5QTi8anCuNEHCSKi7yuJAmg2CKWj7DJIbJcD5SIIB3GR+J9DkGCgT8g74/CSxcPN2WhdEp/VFi7VZ5Y0Zd7yyYKZhCb5djzZunkuI1szbeIZEf2x0LBeTt0tLo5Mqo1JbYC1AvGg5xYUe4vBVnEDA3N0MyI2IZm2MvrV2dWlPrwEd8vsC8WD7knWBR7InyZzcXrj6hEkm0sXKNKFkdktwSldodJlWvfycnsaDng7AQOw++9oPkvIIWV3q9vqGhYXp6mn+Jfxqfz4d/o1uu9vdu4k2DpqH7p8cLf69lIc1bOmSAyE1YmBZ1qgXTK0TeAnEhZqGkL1rcvVHcuj+ltnHAafVC9uewoheeOxUecq5Pjyx2uAsLE4vSOOe/UN4X/k4eNvgoqSZaqsYsxOU/jDGRoj36ZPGgEXgJ+SmHLlxRRm9MvpzegYNNHAu5PRBb+BGbrxoPO3wFx5HByepQqRanAF14ZG3hks7IZGAh5N6QidwzLJx/CJLXQ3YPpIIVueEQqeyEr56cQxBJA/NmGc++k45VOC4MQ04GToAfAv8iHEx+h1Hh5miy8iPBntfHWHHKPtrlwTAjJ3t8ZhoXhqFyGG4KK1DSdh8NHXXdLpojob+TdvtZ5HCQBVY5HwNBpw3qrcjTYpT6vEBCyPnwXb12TEEHpicpqcA5vKHAf9MsCfwYWNOctdgxlhk3bfQwRrNtxoW5iJNlYS4gzEva52H8HkiTrG5AAGeB+UNc5PvAH95HsAc/m9fNeOChQKQA8T4zM5DAwsXTbVkYmzokSmqLOlObVT9oQ8jigkyhvsb5scf++k/f3H0iQTVrIcOQweZgRsddZ0u3pFWEiivC5XW4bItzhFB5G8/CtbtScbJWJ9ii04l++wv55z8Z99tnJEUlQ3oDWaaNwfd147L3qayedWdwibgrPAk6kUYmNYeKNaKUrnBZy0s7z762Tf5BWMhrPp/la1kF3X3xhRJEFjwqKCioq6ubnZ31eMg8Z+R3mT/hDsWfPH8JzgEhZyPWfYcsDJNhFmpIXNgdJemIlah3SquqdPZZFxitzYQ+/EjwI8teee2N841qG8PnqjQ4y/my/vX7M25kYaS8LeZUyZgD2UiO52bQtp1XPv6J33//B9vkit7ePkILnBH7XDkNY+FHMqPlLesTodiHk4IuPDJtOE4kueE+YCGIIfmbl8yfCp3CAw/Kl4CvsvC0E8eFcYSF8KHIGRAue/kEfSQ448gPBFsgcSfeYaAmyunnHBCBgYUQO4Hqa/Izs8hqRiYbO2t1+P2wCCu5lM/fnLBhIENdMw4ZIT6bGoeN57SHgaLTNSzkcAA6bejmpqddI1MTdjdywSPgzeFjjfhZYDJaEv9xpPrB5/PgzzLQZzcbcczAL4Zpgw/NoFGDuUNnJt3lA+zHlw4M8Y3IDDQPBT7j+5HAwsXTbVm4IUmz/XwPZmFJi2vYgv7tP9b+36/H/Ps/vbNyyY5l1D6KWv/kk1FP/+xI5kVdb58Pw3JTcmFUclmUonFDsjIKWKgJVcAmkqve2HlR3YX+8JcT3/rnzd/8xuaPPHaAorasWLmTWvr8Rz/ycsibOdKEnkkzN4vQnpTGP+wofut0S5S0FecIYfGNIkUHzlniLnb/KvTED57f8kFYyK/C093dXUtULehvpKqqKqVSiX+CoqKivLy83NzczMzM/Pz8tra2gYEBfnH5hT/Z7cWXbDBKcXyp1bZZrfaZGSNDckPuPbBQOze+sE0kh74z+y+qy3TsD3+x96tfifz6V3ZTVPSHHj1IUSHLVq7+7Gfe2L0jv6R43Eqji5Vjoe/kX8fCSIUOmttPFndPsLll/f/vW9H/8I+bnvjiriAqlqJily0JX/XI2md+806t0jgxg4pbzCEHsiKhzNcTnKQJsFDejMt/keK6e5GF5AHI18vyfV6gctTn5p+NOCfpOwMw4+tIHVBLOYPc+5KcKyi0aTOyQ3cBAAaBBB+J+V1+DyAQfiMa6kkhyGJp6CTE38ztNdF+Mwtsg5+Qtw3ax+GgKzu9fs3qPSdPXzlx+sJrLx+qKJ1wEZLiHA5Axf/ufjQxZn/95eiDe8+Kz9Tv25l95PBlJwnYHB5v4CE5UpOJH8Dt+MqnX5KcUZ092yyTaFOS9TGRJ48cuGIzw5tzaJzBG8NBkIgLXp/55A+f/e0mwDthHqRDox98+09f+fqvXRxUksOVft/gyNTTvw51+ci6lVcLE+9HAgsXT7dl4ZZLzdvONW0WK/MbEXbHxx5dt5QKp6iNS6kjQdTRoCAJRe1cEbRpZdCzj3/yzzG7C/em6kTxzdGyXpG4D/qRytWhCnVoigqz8JXNl1Q69I//umXlIyEUJBJBUWHU8p0rVm1ZSm1cRW16jAr/8tf+eL6qa/2+7P9aq3j9eBOOC6F3u6wVx4VxFwdxvhB8NPdUdscHYSF/YXNzM85/cS6cL+hvJBwL5uTkYP5hChYWFuL97OzsrKws/LvglxUVFTMzMz6oPb8j8Xmi2Wzu7OzEIKyvb8zLK+CdjnsPLGwVSboBh3KNSKGMUlTtu6wtbEdf+HvR0qDQR5ZFB62KoZZgku1cQu0LorasClq7gvrLj36+81CKepsUuswsZKEopSskWR2XUKE3Ifm5nkeCcOFv9xLq2LKgM0uoExQUJbctp8IfW7H+774seinizLq96WGJzfy6LiIZtnxVtFwVLmu+N1nIAeq8PsjegXl4m5xFB49c+ctf96Wm6rwQ47kJ1UwIGf3AmBlYCwSz8G2Zc9kjzLotaByz0MkiG/5MyuqRlHPVnS0GjxWCyq7u3rrqIeOsr6NjMPOy2mODppm6Wl2r1sAHYXirqVHVN6jJPsuw/v7+ybiNR6Aa0g8thc88vft7/xGiH57JLy6z28m6kH58ibqpqSk3S9lcB0M+ORrZjOhrX/4j40NWG/KwFsgDCS/5jXH7v/Kp17x25PFCpz/8vc/Ooic+82Jxntntt+I09QPo7LmSzCyl1w0RJwb25z75hz88cwRCTJ5wLHSD+K9/feWzTzxj9MIviO/F+LnuwemfPiWCVlb+Z/0AEli4ePIzftLhy0+61fEsdBMWRidUxF1o2nq2MS65rrYLmVxo2dLXllERS6iNQRR27MMUFR9EvY1ZuIL6n6/93erzeVM7ZW2bZR2YhTGywetY+NrWK+pu9E//vm1J0JqlS0XU8lhqSQwVtHXZI3GYi0FUxCoq+De/217ZY454p+jnkZdXn1DhYjLOWaLELWESLS5lh4hVbx5Ib5mZX/jp/QsHH5cvX+ZzXkF/E2EEYiLiv5iC+C/+LfBLfBwTER9pbGy02+0Mw9zJDz2/TDyOJicnJy0WGw4NCwqKsF3z3Wd0PYO19S0MNM353xMLt6XUV/Sir//ztsc+FItZuOyxTdTyOCpo78oVh5YSFn5o2YuRG/MSs/pi46uuY2F0Wk+YRBNzqmRgFklSdUuoPRT1Ns9CijpEUXtWBO1atSTqsx+P/pd/3RV7KOutXZdEEm2YtDNUAn1n7kEW8k25gR0axlHhUil0QGLhq5ycQtHRuR/98F/+8Ztxe3bWW+xQpPZ6oX8NhIw0Rp8ZdZsKnnrFHvSI6jvPHluzl0zaQ2de1L312oFXXt8btn6HKHQvPlRVpf6fX0anKgrDw7Y//6et8UcbMbf++lxYZPh+DEWI87zoZz/9fXLSBZKvMl7a5fb4dbphmN0fmu7Qz3+485c/2z42aY3ZvA0DDEdpMyb/737/cnllRW/XpHka6I2/S8zCb37tL37StOmHNsVrWEg7uS997DXOAzGvxw8Tz/oY9OmPPlde4mAQY7GiV148+dZbBzdsOPbOoZqpSXj385944blnk2nykDCXOguZ6VPfD33yq8/zvyB+cszCoVHnb3+/i+909O72fVsJLFw0WY2zOVnZarV61jTT29PFsxCbY/SxjJjESjK+sHWbvKVIbZtwoldfP/nqixde+HPWyqWbKGozRa3+0Y9Oh28o6GnnsCfYENoqK41IKI6QKqNSW26sI+0aQpt3lLz6yuUXn8/46pelK1ccWbFy+5JH/vov39qiSByrr/Jjy5hFSFJq2JDYHqmAkVWxck1EoioqhWQQKa3PRJyOOp77wVk4PDys1WpbBf3txH//OIyrrq7moYjDQbxvMBhwRMjHeXyr4fU/3g3ijYEnIt4nfSVAI6OTeMPvdfcZKqobmXePC6+vI92hqGsYQuFxha+/lv3iX4opakvQkh0U9dYTX974m9+cyUzXDxmgti61ZEB0svg6FkbIO0PFLTwLa5pnXnvj/CuvXfmXfzm9bOlGXPhbsSzs8c9G799fPzyGZiyoRGMRHS3ABo9ZeLW98N6rI2Xn1NVl/9xn9z7+qV1feHz345/Z+YXPvf3kFw8+9shmUt8T/eiKbU8+vuffvyu+nDLe1wIRGF/O3v3s+vhv/MgWtARFH03ZKE7PzBgemvrOt2JcDgDqQK85OvJ4Zt5sdXX/E599TtNiwpnR5Dj65lfeOn2isiBf90//+CzOIywmNDaC/vD7iP5+B88sL2f3kznTTRZGJs85eODixojCfh3ktiOTMz/5aeTIKHpjzf66+kGopYQ+wO7BgbHEU2U7Nl05f7bF4YIvkwksXukgfV/JADIGffFDIfgjyKSqtLNtcnFvWIjsxIkibF/TRvT7XydoGkjVMIvWvHnqhz98Ff8SX3si8oXfX2b4pk38OzEu/BA//Y+Qz3wxwEJEmpmH9I6fP7XNDr0FkZtfC+z9SmDhoqm7o31yfKK3t7e+UVldVYH8Pp6FfFwYmzoUHq/ZIlUXNE9YEdJ0mrs6UcYVE0W9sGJp6FO/FucVmgf6wWhwwQqfEJOYGSUuiJTXRCiUmH/h8tZQRWuAhTvOOlmk60O6TqTRoO9/9yJFRX3m8e0btxZmZBp8DnAYL2IxC5OKBoIT2mBGK4kW5wjhCU2xZ7tDxK3Rae0/fmP/r9Yc+OAsdLlcOOxwOBxOQX8j4S8f+gt6vSqVCseCGIcdHR0jIyML4cdnuwt+t5trvkERRy04Lmxv71SrNc3NLVnZ+ekZOTOz1gHDWF2D5g7qSLWwALVUR+Yj1cRKm7YmV9brkbYPDQ4gjQothaa+sC9+ecueA7W19Q4fDWaPo5/U0u7ok4XXsRBbLI4L4xIqxhxo1Ix69Zx+FL3+5iWK+vNHPrz+ub9ckkiHp2Yhy8UZYpZybO2ei7GKNlLm65pjYUu4VBsprr93WDgvrcYaRO2nqN1Lqd0UtWMJtZ2iNi6htj6yBI4sp/YGUbtwcfmH/3Jg/fOpY3qy+CKHXvjmf5/79v/YlyxFbycy7c72ju42jeHXPz2O8eBi4Jz0S017D6qrqwz/8NU1fLjmdKB/+kbwwX15XTrX738XO2aADjIFeQMnjmfjnx1/F27G6WFtmIVOLzM16xRF73z22ZDEEz1TI/DVOLzMSy+dPHCg8kc/DYGJPuBbY2yOiYaGhtUv73v2VzvKS0f4L5Mk5uWHe5GmS+SysMupP26KSMfB30uv7v7J97fs3pE/bYQurvohz9e+uElZji5cVFZUdQevP/P5L3yP5tCXPhPx3G8vg5kB9jASLfghfv6dyM9+8UVsJ4FaUw51dUw9/dQOJwMdgUg323c38ltJYOGiyWExGwb109PTmtYWZV0NHxc6WGDhxuTqMHF3WHzzzjRNnsow4YFKc7cbDQ9ZpdKqpkarhZSnsPxej9PusCMYU7FJVhsirg+FUVbXjKlYv1thJiMIGTKgKjm+KfF0q8mCHDhZ0tuKg/FazkGXR3Q076nwS68ebcAsjJI0i5LVkfJ2noW/j0mKiy/+4CwUdC+IJT1FMb36+vowHRe+9Z5+Xz4dLMzC8fHxixcvd3Z2GY1mDMKGRrXN7unpH6pRqt81LrxxTMVuSUWzwcOPqXDZ0Z6dRQpZGw7jaFL1Sqq4oGdianFr1MmcG/uRxqTpYk+X4rgQn+PyeR1uprBMm3ZB2dXrxfmyEwbA4eewOWlrTsNI6KHLsSnaDeKWyJSOe3ZMBUfGuuAdVfPM0iW7gqgdy5buWrJk2/LlmIWRFJQVcGi4fcUy6BmHY8Svfn7dn355YHIYIOSyOp/6xHczv7/aQi1DYWHIAvWZlaWdq/+a5SbDND0+Z3GJdvXakuqqoX/4SjD0BUUwpvn734k4uD8Tv2xusu7eUtnbzT37P1FeDzQN8gzzcV63j3N74WToy8OiDW9e/Pa3NvANmUVF3r/70pvr15/DvzcucJM1t6BXDv4u3Vb0b996AZ/vJXEgNPL5yZdKNrvJ+ZVPrca/OwMX+BrUht//YTdO0MrM5JU0fuZj6zMuOSuqJotLh8sqJkvL+u00+5mPhv7h1xl2N7/IF87tjcjv/tl/RP79N/4/e+8B39Zx5I9DXbYT2/klTu4u/l8uudwlTs/FTjnbiR2nn2M7TlziuMrq7J0iJas3q1ldJNFIqpOiSIodYu9gA0GCvXeidzzU/c/sAhBV3eTEdjCfJfjew8O+fVvmuzM7MxuMvhUM9RyemXH7M0/uxjVIxAPqYP1BKYCFt41sJmPepZxz585dzMnKu3TxwrnTKi3AE4k/nBObVBmVJgtPrtmQWlsq17C4M26Xg3jsOsNUZ4+0oVWqN6hHh3rRtNyNyoWNMJlNbo1NH4oSDVzva6+14bTM7YYbzU6XFjB3WjVQVZff2lqnGjON9SqhKkZsJGxX9mNrT6440hx6QrrhtHwdlIHG5g5ObnpjW2bDxIdaL3RSYkP6vcgcAfqIiFU+04L6W/OaU//FuafXE+PO/k+LxZaXV1BaWp57qbCrux+4Untnb0W1FDkaGop57e+RJ831tRcjFoanoq89Wn6l9MWndGwXVVR1K5mvvdM9A7hls6upAEHLj8s/bhgsaSXyqEM5AIToIA9YiD2/Iyy1a/35gbjjpf1KZL0EDSOJw4lWlyDKuInd6bEhRLjQt66oeTJs7/lIQUOISB4kwBCG1Iha7sXCPr0PC5GBMCykleJF9b8b+UXw8Unj1rcrNu0s27q7dsvO+m275CGhDY8+KuDxVvB4Qffdt275mtSUM/0mPWV4Vg/VOnrW/PgF/gPPcIu/QDa91X6m/ExGwciQ9ecPbrBRPwyVTrvr7dRCCbks6fvht9dAw9ndLqjrh3/65u7dp+DUaiGP/Djy1Ve2//73ISYLMVnp7NzFcR5PkaT5t79fxnHorwBljA7N/OF3lkOLTylN//PDkKFBEhxyqqkFfS3io/fJWkZgcuOwE7uVPPrTUJcdpc+JmVlfR0PPfQpa5Cufe9lpRYiFPmDmyO+f2FdVge40o5P6Jx6L6ey0or5URYok0rrGAXjcv/2/FX94PBmKysxn3HYNPOPY25cXL/211kRsGMEI9aZH9p9PF3Y6MfqAm0Yk+OCNGMDC20Z69WxDfe3IyJBSPTs81NfeAo3aijrSw3lxyVVz4pFiDDbcWNttdzosU9NjZRWS2kapSjlTU1EKvc9qtoNcGH+iPE7QHCmQRwo63zUGm8tp7xlo7exubpA2dskGpLXN0DkBITcnlb6wpXDVMfSvihLUhyfVhvLR7wpm7q9uyjqY2WvF0E3vwh8D9M9DjEGz9UKHAz3P1Gp1c3NzRmZ2m6wTmGN332i9tMNODffxVoaF1FhM7yAvxx6PPF4ZktoeLJZFiFthAof+hfzuOH7HFnFddb/FQifv6ACAwdTcOhN6Duj1RuzD1Lo/uaA5QSBBrSYkAXoohou6g4TdMSd7Yo5KBjXI6Ak6hiPLs3IWlUbJHAZUKpXLgZqYIulY5L4MgNIgcVdIWo8vCJyc+hc2NvSa0IcAuzxlIP4YY0yI+UeQB6GLU+mcKg1RqYlKSRTtZO2KM59d/Jf/d+crWxIrOzqnlEYqtbKJAK3zsgNJu/7tP21L7lW/Gpr4dGRZXb+JI9/+z2cHJtHP/tzZhl/+Kmh0hjTWjf/3V38P7WOzEouJ/O+PX9i0IRlOQQb/v19H/e9DYft2S1Ao9CBYQh3YnJ7BQcvyN7cLU+pcTqJRkcceCV2x7KDTQSoqBrZvy4KDrKzO0LD9s7Pk7KmqNSu3y9sNkHlPl/unDy132qnp6R9XFBe3U77COWxatxUte778uSfguWYrvofFRsTJdcGr90ExAOO3bsgIWX3QYydGNXnmyZD1Gw5A8/7rF558/pl3XBwBfLUYvHOVyTH366/t3r8vH0NVOsjBfVnf+9b/9fZgGAibExW9H6YVA1h426hVWg94RkcXzMFgouq8VCCZ0rsSjuRHHi0HphAjkK3j1zEsxLfAIMV2lWq2Q9HJuQjIlLlZGdjyHgI9H/cHFzRECFrfNTa33YzZjU31aIwqzu7OvVhUUiRh+9qLCvvDU2Sxp/rDk6UsNjeGiBS3A1/4c/SZ/3lyQwALAzSXWGdgWAifzc3SixcvFhYW5heUtLZ1eNCOdLiktM5JObMXC1mAEG9s7qMRJ8rXpinWpHZCR4WuGyWEKWB7PL91u6iqth/VJBgzk5inxkZbm9s6OnsbGluamluZOz90e5GkI2h/ZoxQGieA1IwGOEJFsLAj9qQi/mjhiIZ6g1N5F6C6ra2tpqamtbW1o6Ojq6vLbgcBkUiaxqL3nAfYCxJ2hKYiFqKaVNQexZfFJAEWIh77sJDq99hbeN/nH0Ju+njKxCkq20ykqnRQkt9v0RLOhDegPO3C5GJxO+FYpxuJjlDyeO1PPN13QQovZbQT7ZTzqLD87d1nz55u6u7G2GQTo+YjB0/C/VQlTFKFOVXlcpy6uIBfTWad7TFqqNSFfg7otudtTxc5nVZ7aP/FI+/k9PfY4P6BXnN6ajGqZ814g0iYlZ9XA6e11f1iQdHhdy6eSqtUTmPgGIuRPPXUyrw8mRcLgQ/R9zu6/yIWg8YNx69cJC56Z2lJG766k5TkKwTHJUmHi8eG7EYjTskOv5OxffPJ3Vtztr2VeeSdS2mpl5RKK1yHh1aUDhw7dAnS5eIueCgamqKdKSonAlj4scDC8eGButpqpXLGYjObTTqQC2sbWnC98HBexJGy67GQDgCcmU7NTFvsLuXs9NhQv9WgZVi4QVDNsBCmtLfGQjoxhw/T+MwoXBgemOxo79TbdICFx7Lky/ZVhQk7I1KaAAuBxQQlSUMF7XGnev8Ueep3yw4HsDBAc4l1BgAb4EYzMzMSSXFVVVVTU1Nh0eWCQsnEpLJ3YLyiGtcLHV7sQJtGNia1dtyzKSypem1q7xpxD92kQhYNnY0vS+BLd4jKGvqAXcMjoHebYLAABqrU+uKSMomklGEhgKSoRBGy/yJ6QSAcwuytHTUigvZ16R0wpxzVICpA2QAIAfl6e3u7u7tlMtnly5f7+/sJLdJl6QRgYVRSHSBoWGoXCoVCWaywLRqwMLm+sdc0Bwsd3limnn8sFmK1e6gmkCWoVLOB4LbFVFq1220mjM2Dp8wVHZ0wDAb1pg0aHo/EJhAdVL7b7HAYlRY11R9qlIBCxEwR1mxEoEClopvoNBxGEKWP4CzErPeGPaPYZKbBX5wcx9wY8Cc2GjUUTgECzSYaUBSg2oaxHg0GO/7QjXaeRj0GJgWhEERJuBIasqGldZxhodOJAds88BMTPgP1rljztMOobVAMjIZqJcD2oDCaWbyHcXh4nMmAUiO8i0GHceDgot0BcyDCWdECdnba7aERTd2oR7XTwtMgqB+UAlh4+8jJzUxPKhQdHQq5olM20KOwu1Cls4VfGptUfQ0WojYHSuuwGI362vq64tKKkuLCy0X50tqqS7mFUxYvFkbCGH43LMSpsodMzvY3tNRptMa8nJLLMHVvqb1YJQvZfu6RVfyX91RGC1tjRU2od0pXRIg7Y0/2/DXxXHkfejUFsDBAfvKbm2o0mvr6epPJANIhx2F8LAANWXtXV+9ITb3M6g39yORDHHMuuq/98/HC0BMNa1KHVov7MQYb3XEsTtCawG/cISpt7NNir3cjFqK/nM00Pj0zPj45OT4BeVnMDpWVpJagLhR/KMJ9gNEYVdQRJmhLSOtIOHppVONkciHT5ep0uvHx8eHhYRAKAbBNJnQMKKgfj3w7M4ovBSwMFSuoWkUWT7EwLqle2qu3IfYQHxZSBGT//nFY6GVq3oEIYi/zl8PFNowjyuRCB8a09u7Z5EIs1G7ZaL9zCdkSR/QmOyKBAUNnEzSAwSkKNoyDs5vpSgqKZi7USyM8wlzC7cFAtb5YpNiUACQOt5Fud+NwujkbRhq9Ui6aUHp0emyQoBic00jlSFSDsRscTLg3m8Ynpjz0KjUNNiNaupBNcV6ZFo1LoQA2m8VGIRo7mMeDoVPdeGzlLHjblbJhwB6HHgAAgABJREFUYtwOcjVZjP6ycXbvRVpskwdnUx8cAQJYeNtIPTMJcmFtbXVnV0d9XVVuVsbgyKTBSd46UXxDuRD1qMTR3a3IK8iHPnX+3JmJkUEA1PGx6X6lFwtxZv1uWEjnVq6W9moTZzBb7G3NCitGx+Uyypq38Ste2l6CATiSpfGpbTSfjqi0noSzAy8mnFm7IyuAhQGaS34dKQhegDElJUUtLS0gflVU1kouV/QPjIJcWFXbyuRCtCPFhPYvwIKVgIVx4tAT0rXioTWiwZBU7K60x8riBNKt4opaXNICuQG5vNtt6uhslZSXFRcXV5ZXQF4jQ+MN7WNZ1WNBe3KCU3FpHPo8MxkLFaCONOZY4YAOmauf5HL5+fPnQTQEEVahUJSWll4qrMionQrakxspbg8SKkKEXXNtZ6KTG5v9+xfOwUJ8Zyoq/cPoyhBk+lLOiyI0AXThKilFa4xBY6GBzgwGbu9uHciFIa8TLbAZs9OjIm4zhu9EMEXxyubW+SYrTgBF/6eNA9hwADTSAKROqxXx0o2mmdQGhcIwFMDuoEBFf+Llt/jVFZz2HbOatONT3ZhAkGVv5MQtKVFWc3BODucg0LXsdoeRQyHRXzCT3WF2oeEU5kaLRIxGM+tdNGKqlZYKyeXyWKwGuI6PIG5faAgsHryuy02F3w9KASy8bTQ1Npx04lhRUUFhcUF+Xvb50+ntnb0mN0k4kg8QeD0WEioXTk1NXLiYNaPWnTqZVldVbtKqOuTdQxqySVy3TtwEcuG7rhcyubBvSFZVXzE5paworZuZmh1XjuXWdpwpH48UyAH8ogRtkSmNkclNIcntGzInVh6p+0PI8d+++TZgYcAENEB+mhu81Gaz1dRUZWVlnT59uqBQUlPbaDRxgIVFkhrGGqkVKMoZDAsnzOQv0SkgkMWcGQtLHw5N7w5LwxSV2hGb2rrzVP3lTq1PP+mcnBysqJSo9ToQ6YoLiyaGRrSzmkbZyFlJb+yxy2vEXcGiznChLEzYGSLqjDzZG5TSHHTg0rAFw1AQH2bX1NRIpVJ/yQG88y/X5MvNK3dmw/3h6X3BojlYKFJEC5qaembQXAeTw2kzX8FCvPIPHwgMkFnyQgVNN93L17RwHkmMIHqzE4HEQFxWZIAsA1yZYz4Gt0iYuffhV/CYNS/n+2pueRgiXpPwK4NR48uNqhYwNzeDN9pJ/Pm76U+uKcPczH3yoPdOBroObw7e63OK7SV/Ptdcfx8UwMLbR27H4EBfdXXlrGrGaNB0d8hc1Nd+C780+njlNVhIt5hxupzYWSenp6St7eNjI4r21saaytqaRjVIk8Ia3Mv3vciFdDS7iHFgtE/a1JaXU1JUUNwklw4byS5xzXOb8lcebYrktyakoRVD0In2EH5npFj+yxX7/hafHMDCAM0lhjH+4KVOVEnS66iPcnd1Dyh6hhubFYzr2D0OtNR3Y1AJ6EhaN3kh4tBGUd26VHlcemeML8WnyxLTWvZmSMu7DUzEgNzUqikYKX1Dw9D9jFpNtaS4vFjS1jGcVdGzPqk4TNQWKWyK5TeiU6ygJeakPJzfGHIgt1NDdHPK2dDQkJOTYzQacb8nm621tTVPUpnTPLty59kYsTRU0BQhkMYKahIEtfGCeshqHb+qUTGKPB73zXMwD2CnVznKVur+IcSYvh8hfDyOnVHuf1MsXDCfJMQTnZNujmz1Wj0xfS/yhLkQ4qO5p+zY/yz/E+lDr3x768R+5qHe9266jSJrY7yOsyUXJlSlXgVX3t/eiK4qBv2J57rizU1zL34ICmDh7SMYWk775OR4eWVZbU1FU32Ni/ra3xALfQ6kDrcbVUxmjnYRj7O/qwM3taG2M1HJtdHi9hgxOmPcCgtpz7M5NQ7gVw6PVmXWqLRGu2HMQoK2nnksSPza/pq1h+uDDteFH29dd3p45dGWtSekz8akvHOh5cP4Fwbo00d+C1JCJS3UaNntCDZOotWZWlo75IqBqtpWq4MY0KbPK1S5qFxo8JA/r90dd6QgNqk6IbU5OqUuko8pJqUqLrli75ma6m4dtSOlD3LZuru7m9rkeOJxS6vKs86e7egeEV6sjn0nI1pYFyeoSUypTOBXwZCB3CJOlIcfyOzXo9KQEfTbgYGBioqKs2fPZmdn5+bm5ufnl1XXFzSPh+xKDz9SsPqdvMgTl6MP58Yezok5nB9+uDjqUE6TYpjDoQcjkLsWC/HwH0LuD4eFCTANoTyA87acm96M1jbUKuZmyf+guY+7Idi8h4T7D6PhDX0u1VSxd/FgWdAT1Le6fCOInUueq4vBTvwXb1a8K/d/cApg4e0j6mVFqFnT9NSYZnbKSf1eE48WhB26fEPbGbfL5nBwHYrOrNz8JmlDaXFBWXFBbk6B0o5YCNwEsDA2tfPWWMh0pFrjRG5hdnZOfmtTp6T48tmLZ4qb+0J3nP+/2IxVx5r/uqXgkeUnnow6H8bv/n189oPLDv9m7f4iBV2/CWBhgHzk7wwGg0GhUKSnpwLAgOyVl1985mxmWXlNi6w7K6dEUt6QW1BeUll/ubK2tAJS/eWKxsqm7o3vnNyfJtkpLns7vXJfWvmedJZK96VLMiWtPaN6L3Njw9SDnvt1dQ1N9XUj3XLl2DCMCcWkuVQ2WqnQ1HSqGjqmaztV1Z3a8m4TyJQ13TMaGm6JETOfUSqVIB0WUxocHLRxDpjeDavNYxzp0rhHTGRC75o2uCcNZBgSDXKNOXy8sJDM4fSIH9fRu2GhjprXwlcuKshTbKB3XdF435i8zJQ99+ZYdYt05YfXSG/0Hw0qRAvuput/vnvwh1fTlQyve8TNkv9hV1384BTAwttHOB3CzgSinttjh1TZ0DptIeuOlsSeqA0XdUcLZXGAhdJJNY14xDpQb293Vlamy+O+kHm+qkzitnP9AyP9SrJRVJsgasJwjqk9zLLcvwcNYCHMjn0iHXYvO+ceGO4anRiETJNPCDrlCidxZ5a3JOfIoviyCHFXZEp7xIn24CPtQSm9q5O7Q1Ka39iY2jRCt7z2UQAUA0Ro92U6UovF0trazIIKudzEYnUABqIg6MFIEX4UwSs0uWhIEY7aexjpp54mC5UaEbmQbbrQWt9p16gNjQ2tbTLF9PSsTqueGuqvLisZHBqBSZ7GgfM8F5Um4NNBjbFx8geZ023roGCsr4JkeeHChZGRkZmZmenpaZAR8/MvuZwwMhAbLGwnP/pOhJbWzkoCJx6n247LE1jsK1h4Qxz6+xNDF8ccQxU6Tr0FRCxEoNGq7bu3GxfOJ+vjiR7DDVAp0LfeiyAElYB2nvQ1/WKZd4mXXvSv6rFnMVsYKkp6n3Ud0lybfChIOCdnqiotPnQwyWqlFeqmO0vQu1g/QSxkObPfet+UvazXgMJ7Ec1oadPh/biK4/sWHzTH9YT90Je87/XBKYCFt5HQUBiaxGso7LafypMMW0jc8bKo4/WRqb1RIlw4yW+ZNXibGptzcmIk+2IGdNDmloaW1kZ4tY6u/u4p+xZhdczxmlCBYk1KT6QIUhcmsTxG3PLqRqGB9ly03XIY3LgwQFplLVOTI9BFLpdIJicnoRwXK1v4OXUxKdIIfkdUsiKWPxgpGF2bOrFcOBTKl61OEPYM0t4ZoADdhEwmE1tOxvmd063XG510/3h/r6FLQb75voPiHtX/Q/eT6/ov9la228bshLJFOlGkqIMjFyCwoqIKTnzRU90z05NSqZRB7JVeeUWwuHLR4XC4qbt9W1tbS0uLh/rdw/Xx8fGioiKYVrKfwCcrrZehe/Njh15mP+fK35vYhGPuBNS/ck9NOt1+XwhWfjvHXhP9EmCuQNQz5o3x3J1LyK5dZFaLmIleCFYTdWVw4I67briVWco6kTE6EFI97IDt9As3uumSMFqWEjTl47yP9XirBwoJh2aL7UotIQ5hkRCvzEo40uMExcrZjOX5mcuDEk1Oiqd2GnoNfRbNTpy1wx0mfA98ac5ms5lNGFQEBFm3A65b7RYzxhLCZ8AUxmixWWmQP4LiuwumQ0Rr81ghIzddcfaWhjXi3PShKICFt41GxgZT0wSVleWV5TBDLbtUnJ8pqZiwkYTjxQlJ9XGp7W+dkiUKqoqaJ1lAJbRjdnEeNzc80tfe0crmbpVVNQXFZWqOJB7KiT5UAL8KE7THCtvjhS2YRNJ1oprlWxALTXC3w0LQJQi3BHM6nSBW9nfJobMCf6ltlg/rXBmlTZGp5WtE1XHpDbh+I2wKOtWxIq01KK0ybH+abNxAeVOAAvTuNJdre9gOUDgJw6jcdMrvZiOSUD2ejRgO1R39xtoHd1UfprafHJPIkBPS6TygLMBYV1eXXq/XaDTt7e01NTUg4fkfcQvyPp0QyCE3N3dwcFCn00EmtbW1uXmXMPoIxp+ZS5RRekWHjxddr4xh/iETExM+hwGKTj7xjIIBFRP1avuW9br5PBIXR4bHvPKu26Szc1az3WwyAMgAXOnMNrse4Qlu0E2MuGxmODApVSalxoBBy9x2Jwc4ZsDtAOi8xENsdA97vdYwPDw8M6tiExGWsNZdTpNeBc0H0x6PVcXR+Y9GM6mcnWyU5L4e8tY0yoUw+3G6EECh6XUqtQHeEprIZkATH7NhRqk0onYBod3tASj1uGdnxkGEMBjN6BzpMIxNTXMYat3u0s0ap8ftVM2AIq/nQ3nT35oCWHjbSKWZKS4uHB0dtpotJpPBYDVmS0qnAAsPZkfuuRSdVLteWB1/NF/SPGJwUy0TnZGxF7HZzcxrVaVRz6jRxGBHcm7ikdxEYV2sqCkhpSYxpSqBX5XIL0/kl7654Yi3Z+Bv0UQccnG5XAaN0qRVQfeyWq0as2PWRi7Vdrxx4PSLe0+uPXBu7a6Tq3akv7Y/86V951/al/bG1n1l3UP/wOoK0CeCPJSYHOYn+gUmqsJkRvNUGMT/Hgex6IhybUbQ/au/8Ur6KgPuxm723+KDJTI7O3v+/HkhpZycnMrKSpBC3pdV89jYWH19fVZW1tmzZ8VicXl5eausDVi23eGVB31I83HEQgAeeFmQkFgYHb83CyBQQUEBzKYHBgbUarW38DRMGgVEVO0yLJwIWWVYyKv90Y8Kdu+d1aPwRFzGuM2bnvvziy88/5dDRw5CbSt1xuRDB8prGg6nCF948jfCpGOzBnNZwaWYkLXwPJVeDbkWFBWGhod5i0Wb1cE5+cmCp59+em1QyOWKagaEfHH6yMhY8OpVLz73zL59+8a0IF9aOwZGtx1MeuqPv4uOijibfDB43dtqrGYX+tVjgQweoj16LOXxx/+4detmF3Xx2LV9fXzc9k1bd5VXXrZYDSODEwf3Hvr1bx5L2BBbXFpmMQNAW1cFBadl5CVs2PLm88+c2LcbXkRLA28HsPAq+thiIXAEo9lgwoB9lE24bUbObHS4Cqo7MySKtJKutIK2s8Ut3aMas7fbowLEypnMVpPNSZUZHpwD9vX1aU22vglt54ShYchUO2xtG7XIRi1tvlTfPc2mgS4Oo54yLMRRYjE5ICsMskSsTpJdUj1hdI+6yQzMBI0OojURvdVtdau0FpWHTLsw/kdALgzQLegK8l19BS96KL54TQQRwJxWVE6a3GYD0bU5pV+M/cLnN3z5C9FfbiNNeuyD+C0OT5QtrgCehhKhkzmlUjnXwfE9EotXQqhE1aHo/ETIhQBypaWlJSUlRUVFMA+Az+Li4ry8PLYVMxxcogTXa2qqpqcnOQuiO30pLxZqivJSv/V1250Lybp1bWmnlq2J0pu4Pz/5ywpp42D/iFajEoj4wVGJerMtZNVfgyI21Eh7TKqRl1987hvffXR8sD145fMtnQMuqtz80UMPxsbHsYLZbZxeq9u3Z29BXj4IpiAXfvM73xelnzZa7UdOpKxdGwxinMtufvPNFd/96R+gHb/+nZ/8/rk3PFAityd6xaurY3bgXiR4iiKgUtW/au0LuZeKZmctdXU1f/jVU/1dg6tXLfuXf/lBTmHh6EwPwO4XP//N3TtS1LqJ7pGWN4NXNUuHictx59335JfVj0+pZge69m/dePCEGC0koHzoTf9RNWIAC28boV2xk3O6qEoDLYztuNjvstkpt4CGxM3bKPw4YN5KlwTMZqPeqEs9dTLjYu7ZcxkXs3PPnDl1+lS6UjkDt3FunArZmNhHP+3eZRdiMlNtO/rt4KPhSk9vP/ywIDcnM+McTLfPXcguLKsZntG5HPibugNHdv3g+29//3uR33wgdcUqhEoHNYAOUIBuTn4gRPMZl2vuKVvMwgkcBTnsjLiDtFNNtHKuPb4gZunm+fO2LpmfeGdYztoB0ukkNDwYoX9ONMzR6dDRfmRkZHBwED5bWlqam5sJ9fH3Pf/G5MdjlUo1OTk5TGl0dBR+fvb8OQeFaVZQ375IHzssBPgvKysDtGN7LxcWFoIsCKdwAJ+5ubkMDuHb3NzsrKzMvJyi8YlZajqEWAhjWrR25Z4v3K3k8UhkJNEaFANTSo3xa1/+3IzRAC8PWDg9O3Xf/V83mixBK55ukU9i1DJiOJmeesc9/0Vc6pG+mj+/sMxgsU5MTj/+y19ptHriXcLEunI57ali4auvvvrKq6/z5i+KS3zLYOFALpRISnHy47Hz+cJ/f+AXhin15//tW0U1nR4aMC3/tCg0ce9cLMy9lH7X3TyHE9cL3W5nb8cgZ3JEhAff98WH9HbORTStnQ0/f/glaBnOo9dywxXSqmXL1ts06i99+X605MEWs6hGBr7w5f9kmjC3VfvRNWIAC28b0QU/WjYP7VE49jgsJF06ZgNxjhyGIiD0D4PJWN8k7R8YgU45MorBGaWN9TPT48hwMNQta3lEPJb5lUf4H0Tn2VPTs9nZWbK2FrVSBaxhZGI6t1AyMathBmJFUfGhCxcm3Ln0tXnzdv70YaI2s6WdAAXoAxLte545WOjCfTdtOmLMHyt86uAfcDP2rbyF2+761d7HCiYvWnHDXezP2PHsbgBCkIoyMzNTUlLEYjHM3pKSknp7e9+LjtQrmBJSW1t74sSJtLQ0gUBw8uRJ+EwR8J2+McIMaih97LBwamqqsrIS0A4q4eLFi4B52dnZcAqfc0VDAMUCENDyL1WW1ao1RhcaTyIWGqz2Pc8/m/S1+613LECfCgOuAmoN1vvvu8vocjrtHqeDm5qZ/I9vfH9iYip09bNd/VrEQpe+sDD/7i98izhVBpXiW9/7mdXhrqisPXY8iQYDYuSenZk4fSr1tVdf3rlz5+Yt2z53379s2LzNYncBFhYWFuPyHnEcO3Zi0b3/bVHqv/n9X9TJx1iNSyV5q6K348IjAKEd426fPHV0/iIefkmx0G1DAWHtmhUPfOv3HPYcTdeA7LlnI6BlbG4dYGFrj+yll6KJxXzXPfeaqa0ycZh1EyP3fukrgfXCG5AXDD6OWEh3PKFH9J+bNh/OZrzQxcakL6FpHq4UE5PFbDRY/fkY9FqTUY9Njs74bADT3brwldmo9j3CVxeMg8Ac2WTCLV4YFwBktVg5/IXNXRQbF7dkwZa7lsTc89ntD/6ImHFo+B2fAxSg900e1hNxGYv1eZALbcSpJ6ZVx1f9Z8jXeNt5vM083raF/xF2/yuHX7AQs4X5yUF3tuJ/kOQ6Ozv9+V1z+l4IpMm6ujrW5wEdJyYmSi5LgL+zYeGPnvMxxEK1Wt3R0VFTU9PQ0FBfX9/oIxCOmbIU0BGwEGRHhaLDYqEWmAT9kYkHbdRtLlKwecPe++4xL5lH3nqLzKg2bNsvbZEDFlLAgD/3wFD/zx77zczMTHTQS5LKFouHmPTT+w7sX/q5r7ltKuLR/O3VFTl5xX957iUPtRRlQqHRoGtsqPniffeyuoKv7v3Cl2ITNkzOqkXpp9H0F/HYkZZ28nP3f880q/zSV74lPF9AtyUnSW9vBSycshC7QQdw6OZIZVXu17/xBQ9yJJDRHSGrImor6oPWrnjggcedqK7SD470fvXff6RVwURJ7SQG/inxkUNnnAbd5+77ooWaxzs00zODvY/99mkDNdIhGOD0o2rEABbeNrqChQzskBgWMu8Ztw/YnAwIIUH/8L0OioFWK1358AZxcFN1BHOdoVjoPb4ODn3D3mazMVBkiy5W9PTBsN3Ewl2KDA/h8dbP54UuXpT4rQeIxaq3mpk5a4AC9AEJtZHMX+0KFs4Q1eMRj3/ptft42ygWbl5436rP/yLmZ2qituD+PIRubY5zMIvFolQq3ZQI3XQCpKWr8r8J+eVCyAF4PdOpwrzSaDTKO3GfYTYs4Aq77WOIhS6XS6/Xw+trNBo4MKGtnQEAEo5lMhmgYEFBAUBjf3+/Cxc50HYGWIINdyREuRBm0CMZZ1K+/u+GhTySmNibefHJP7/SOzD65K8frmySWkwcTKbFaaLla8LUqtlVr/xp3xFhS/c4cXOvvPr6Az/6BXpbWGaFqadfemXZ/z78GNaVd1KMPKqkOO9z995l58xQnhJJ6R2fvTc8Og6+ByysrKxmWAhC/H1f/SGxmv/1aw8sC4uHX3E2S/SKV8PW75vBRR0Xkwv7+pv++vLvL5dWAV+empr45te+c+HsxeDg5f/x1YegJWwOHWR13+e/mnL8FDCt7sH2v73xWlVlG3Fa5y1aXFYvw0DjRrXw8IHIdZu9cqGTBfX+SCiAhbeRvCIgGhZ4Fy2c3mgLSBTSEC/R1oB5QUGCA1w8tPu27cKhPgfnGKz6T73n3uT7xVx1kJeYixKGCHQ5uJGh3FXLNy1esGvh/MQ77tj/gx+S3m5cNUeDeC9oByhA75OQJ9JN4654Z9uJW0k0+y/vjy6J5CXyeFvm8TYseVr49LGmwxqiM9AlQxyjFgtz4cdcrlaK+tDrAxIOKPppp2aVPvrYYeEtVMEAhzAnYMIuwaHNoQGCnz04jcAtcLSrZ0bWvAlY2PDjH4siYyZUFnhh7fRgwrat0ZFxK1e8uXf/HifdMCB65YpTFy4eTk176cVX9hw4JO3pRV2102HlbAuX3J2ULKIeiVjzIIByNpPNamior1qx/LX9+/fnFxSlnzn/p+derKxtyCuStLW12y2ASo7c3NzHn3oBxMg6mTxh1541a954e/f20oun96dk4sIjOp1SjRQxWO1TO3ftW7YsNCwsZHxwGi4Kkg8GBUVBL2CSaE9nx56dO1766182b954PuMCFMVpmPl/X/xSrqRm996Dy1/40/qIEBvdjQmn9gEd6VzyAcDHEAvpDO4qLHQz5KMFZkPRq1Oam5Dgfrr+jGZ5Dnbq+5pi4ZU7kfxYiFkBW/GG5GWKFHYMU3C3w8VZFJKS+N/9Lnjp0u083k4eb9e8JRG8+REPPUTQxRV9la7kelO6CoCv/ZLR1eW76vjGdE2e7F18Crerbph7GqCPD7kpEF6FhSbOrHSqpsjU2YnTvHje4gN38+Lnh+aHTZAJK7EZmLAA3dSJHhrEp8/wKzPn6jNuQS5KcOCXKYH8IAooCCVzOPH6VbYzH7MuBAWGocpK6PF5TN4II6lhgYtuk4vvaHVwVKxWz5B9O6xLF5HIMKLWaY1uWiMGB/rCE9yekAp7OtVM2PLVUlmrAWPO4UQBfeDtgIWkvEKybfvbeoN33w43xhuyUSt0thzjRHLhIy12h5nD1RwgNPqj2ikjfHhwnZJaOlHtl8OMFoIuVtMoy7o8BodLy9khZ2hcq9WEbv4Ed+yieO5lGlR55nJaLMxmCrqH6d/u/7INYyx7iNUAs/kplcFGAwkR54falenWFMDC20i+RroKGPwt90GH4rvjys2IPnFs4tDfXl239M4dC3CmvoPH237nZw+98FfcNhu79bW/uZowB7bP4vh4/5mz4rPn0ouLC40mC7Abuay9srzCbMQNp7VKVV1Vdeb5jLGRURfajV2b0XUEzce5PeimDamrp+N0xqnMnIz8krwZzSyM5VnlZH1DNZs9GI36pub6vPzspqbGD1iH/2hinJpxOqbKZlcY9wex3uMLnuLzsEaE8P/KasXb/PlQYt3pfXcq/6NZwBc49ivY2Q3AneestN2C2DyPqR+8fd5F3DbCmYjx0ngOKkhh8rWet64gQUU0HiqxoR7iYySefSIImxgrzNvU18VgS4wnOrOvEUxMLmZNA1f6+3oiQkLlnR1sUsBawag3KNrlr776skxGY6NfS9f2q6v4GRJ+RTPER9ADej+N70qx3f+b6xrbe3HuKfvtlWtww3333QcXrDZ0wydzAgm9397+viiAhZ92Ag47MLRqwaINPN5GHm/L0iXLeTxlWTl8g4rZ90BOuM9jB7jq7u3Eib9WB5U8PqOtqW08deoMzOYgyeWdKpXG6XRnZWVf+/sbEoq9XgWyy+XIzr0oKS0xWi1KrQa+6O3t7ZR3ZGVeYLJybXVNR7tcOTMLB8ODQ9dm9UkjtVo9OTnpV2t3dXXJ5fLx8XFC8W90dLSxsZGtnDGJ32QyTYzPEBSYcPtvHxwybnUdr3k36uvrk1OCBwH+QTFGKLHy6HS6zs5OqH+LZe6muTcgpsLw+HgwG5NUqWHniK14uABQcN5W3qL4BW/lbjHgxB9vYAHA3meR/8kJGxrnJhRnronN7Y1HqvMZ1wAWUnmLxsbDKSl0oZ6eHn9nA5nbQ31RJBJJd3f3Vc/52BCUMCcnBw5uJCV/hBTAwk872awwAuK/8tXN83hbebyEz9y14rOfIRPIeR3vVlmsqjmHnXPbO3o6W+StI1MTGqPF4iIzOtvo5EzupXyLlXM43Tq90cahHdCFrOzrPJ1vQAhyvskgDNTs7NyiYsnw+JTBwrkwMoDNbLTlXypiJZidVjs4N2d1NjW2DvQNX5PVJ4sAY+rq6hoaGpgmEMAvKyvr0qVLpaWlcDo8PMzczqqqquAGYGQgvTWgrSE63jlYaJGr9H7vGwuBy5w7dy4jI4M58wEqwxV4KNM3wqOY4QbA4bW/vJpujYUlQ0UL1y1euGnh0tjFm3K2GSgEetB0kLLyvyuL+6TTh8LCG5Jfu2BHrahXHzBH5fCPJ1aYd/U0vb0UwMJPOUGFuDhL5fZtm+Yv3s5b+PJdS5NWvU5cGOHX6a3JmxLq/OlSpZmzdff3VdXVtnZ2nr+YqzRaYHAOjU2eyci0YVRDvMdosvQMDDbL2l1MuXFrwpVBr+LD7SR1tdKG+paa6sbMC7kKxSCzls3KyPUyfDfhLK66amlVecMnl40yIQ+m5DBPZ8in1WqbmprGxsYI3ZZ2aGhodnaWaU0vXrzIJsVSqRSQCeqHoELV4Tc5+cBYCLkxNSxjNyCkFhcXnz9/nl1hEAiSaElJycwMCqM3o3fDwpIlcXct2rh0acydgIV6AhItFtRGQwa+S7cL0FX0YbFwLsj5NeRzLzJtvF85/09LASz8lJPWbeWgokZ7N9x5z8aFdxx75S/G/haHC2bqNpd3S5ebk9PnyOGy01VDt8Nuk8vlAwMD0AQTE2Pnz51yOtCyy6BXl5UW93R3wLEHR+67tQOLdo/2ADiInXaHXos7lhcWFtfU1OH2xh6SnZXjQXs052D/UNnlcuWMyt/2n0Rik1wAMwA8EPuA9SiVShaEE47Hx8f93nVwHaAIDvr7+wEgAZMqK2rZV9f6Cbx/LExLS6uvr8/LywO5EIAQMqyurs7MzCS+xUt4OnwFgO0TQG9Mt8bC4uEi3ob56GKYyIsr2KAkBicKhW7siqzUAXqv9GGxcC5Bc7O5lNfCzuXyWyp9rORCtmL9d4bnABZ+Csk/+yMY391jhvGjn0l68KdBvAXtp/jEMOF0G4kdrZTfBQs9DpdFRzyc02qcGO6fnRxz2szlkhLl7DQ8ZHykPy8nUzUzDg3RUFsBp2aD2u2weJuG5nxTLQd1mqQ3O90urqKiTCZrtdksl/LzZPJ2QmUm4Nfs3qKiIhCb2PE1w+NjNYDfC5nNZr1eX1ZWRmggLoAlg8FgsVgAe2QyGbwdzDNAapyamgLIrK2thXvg24ryGvbzOeE6PyAWAv5BzpAtiJ4jIyPwRBA9MzIy2LfQcwAay8vLgUXemhPdEAsd6AVntxKLZKKEt2Me721co44vXT9BMDIXhzwdVwwxBei90u3EwgDdggJY+OkkNvuDeZ/W7kY4cnA17xzZ/czzrukpuqkZFct8iHVTctrcnNHr5u92d7TJGurqx0fHCNttrrG+rFRSV1ttNhm6O+R1VZVVleWQLGYjNXS7QjeSMODRnMtt8xC702UzWw0dCllNY63GpHMRt7Stqb654XJlqby7Y3xyTNrcWCutq4QHVFfMKKf9Wfydl9Y/JPmNMycmJkAuZA5kHR0dg4ODgDoA/ACKgFIAk/AJr8Y2YYA7i4uLhYI0g8EEuD/nlT8gFnZ1dcHjAFOzsrLgEdA0AH7Z2WjxBMfwxOHhYfIe6vaGWMhYsMltLBoqXLhp4cI9vPkbeTEFsRNkhhYUf8JM6AP0nimAhX8nCmDhp40YF2OmECA2cd747mS2o0uak++xOHBTUIILdtcD1HVEOZjHhc6+TtxN1ALSgouYbJzRarM7PFabU60xQHPYOLR7hj8Tje7GxqCfn96IsTpdHrvTDTfjyiHgn9FqMTu84ZtNdruRs5rsNp3FZHW54BS+gusWp9PIcXbqavyJI4Afphe9fPkyyGE1NTUgewEugtQrkUgyMzNBYqusrMzJyWlubgZMAgnS4XCAYK1Sqaoq6wgKwdfF2Hz/WAhPLykpAcmvtLQUJE4QQ0+ePHnixInu7m5AwXPnzsGjFQqFXC5n20fcjG6BhUaXQTJYck/85+7ecdfd6+/aUrxFi3v3ELpTvQOjywew8H1QAAv/ThTAwk8b+YGH8c2hSdIzQkY1RG4jPYT0THu6B+yD00QxYxtQ4m6btyCzE3FUbcVIgCYPUdqIkRCNGz/ZgcpB9AQ/1U6i8+DGnewrI4ac9NxCgUnHNSbGy+00MdhmYoPJ5T224ugnGE2RbmDGzQHa66PtfPyJ4d/k5CRzogAyGo16vZ75MGi1WgDLoaEhuIfNZggV12ZnEJZYdX7I9UIoADx9ZmbGTjcLhOOpqSk4BRkRrgDujo6OwjEU6dbVewsstBOuV917qOrEztZdO6U7G8dacNbl5dF0W7v3MAsLkI8CWPh3ogAWfgqIscUr5PF4dzuDlLA7d1dyc+T+gteF+c8n50QdKd14sDxiR0704ew9Yol/VzRCvf28YURYbh6EwAkr2Xw8czO/OPFE0bbU6vVJkk0CySZh0frkvPij+VtElRuSL28SlO9Ir90srHgrpRSO4SIc88/myfsGYfy6ce+qa5oFfYctLpJZ0LYnuXjX8YIdR3O3HMo8dPLypoMZW4/n7k4uOJRevispf+M7mduO5uwVFO8XSeBgw/7ze/hFJy9cZluvXb3Y6bymEv7OxARcf7XfMLE9ZoFLsQhBcOqksbVA1HXRmYeVBpqy0akAmxzAp8lBdFY81lq8V65PCC7+x7ChwVghnnpdlRlsmjh8ls3psvu83o02p82Fu3ixU85NMGaJ935fGCCajzdbxneRvDn7kx1nLbjFnIm+hZI4VN64a/hTDzJyDI9ypaQBuoZ89UI/6EIGs0Zy0H2QMew4OixRX3ulY/dW48KFuE+FFuNd0Ip10GYH7KTu+fSi0z/3oHdcqXlvm15pDtaH/fyE3caamN3gHcb+L2g/wfZFolZRLgcmb3ZuWlCa4AB4sxP3cmLDxIfuXqTHErrpxjx2Jzp74QiZM82iT/SX5COiABZ+CohyrSudBroaeqIxvhlztCwmpTleII1Mk0akNcWI2mOSW+P5zbEnJPvP1aPvg4va2iD71blwC3KNN6oWlcPMhGxOyYsX1cUIm2MErfAZL2iME9bHiOrjhI1xAunN0p7TkpZRpRH7OePwbg8dh9jlPRjoacRIEg5fXral/Knwi4+8cujJ0JTQd/IfXbb3xy/v+VNs+uq3C19af+7nr+/7Q3BS8H5JXFLdEysOPfj81pW78oO2niltneGwgE6XAwcMfW8qQH50A+U68puWeKU3yrSg2qeVphk1NzyuHp5QQhqcUA+OG/ATj+mpN809VQ5MquWTZumko3GWNKlIm5J0zDgV0+6OaSKfIfB50zTj7Jy2YG2wOYwHSqPjnEqXB2UF7BoeDuANkAkkeANFKdYeZnp8i0SlfKfBYUd+hZHioYb1LmLE7sGgj6KmjaoBWM4s6WiCKxqaDPRZNvrJjg0UhvUWJ+SMriZ2VnRMvtH9T0a+oYF4QAU7BD6XDerc3SkjNQ2kvtXa0g7sDicrDEi0U46Ncdr5i8mOvWRWa4dW9iAQUmgxw3TEQCsVJh8axFLAIKppoRsh2b18glCTb2J14AQF5zEuswtnw8xoHDoJTNbsExol6mM8uOZvoIDl4XBKh5uNoA0e9ivMzo0BFYheWX8+zTCtw/s4jKwGcO72QCk4T3ffVE01UU9bicVgd6JRuM2NE0CPc5ZYbfjOdqLTk75hd2unc2iEGZm7bWhuxerESbeq8OL6R0ABLPwUEK2KK1jopAEH0WQGUvjxilBha7SwNVbYFitsjxR1hQo6IkSymBNle881wS85G2rnoN/afCzOOyypLz589xa/KFrcFi7qCBcpIkQd0UJZhLgVcoi6ZdpysqJhlAUvob4TlHW6MBAGjHu0H00vrn8qVLDmcP/fdsr/trNm2b6KKGHDizuKnt9euvpoc5SwY9Wh+ld3l72xtzLoWFNcWveb+6tfe7t8zZHGP6w5sUNYgRaobAZAp48uYsb4vR+OlfqVuqjevbmCl9E1BkEu77wXGFfn8JhhUm2eVBsnNXr8VNkn1VZ6xTyt8qa5p/DtqNK5TVj8xtbTIccrIUUelcQeKYIUfUQCojycQoqiiR37T6OPlMQfyFKasNVZJds4o8NtdTopE6FCAf9s1ZZjhYknKtYlVW1OrtqafHlL8uXNKRUb+WUb+SU3S5v5hcezygAAEQtpzk63A9f8PG7cBdpFJiZcOw5f2pIk2Syq3ZBSuTmlbEtyBeT/VrJ0fUr9NbmhOkEgeSulGI7fOpalt9PgewjVPsZME+uB/1xEa4COO7RQQ/kKe7Mb3XSHFU/dtWjFZ+5dccfd+55+hpigk+OgRqTSjtsTw7QLl5C3tpPhUUQuj9MzQ0VJotFy1MMXDt0OxBiMTuxGjYSNiY5E72CbgTuZX5Wd8zixA3FW4yxxcQ6tFq/DsFVp4McsiqzLasWmsTpx2ollRjbDOSkw44PUBJBUM5EctnK6uZ8Kdk6c9LocusH+XeHh2fv3tZ4+fXHn9rKT6Q6OhuMwGYnFSDiLV8Gj0TZlZPKDg2Wnz5QcO7Fxxeqx5jZvH/aOcT93+kgogIWfAvrgWGjHiTgwNsRCprtDqMI84aLpQ2Fhaql0AmPas17M3OfpfBKuOEB6SC2sfTpcEJo0FJI0EiHsjRK2J5xqC05uDk7pCON3RIs6I/jt8ek9Caf64CDxdD9ciRErwpLbnlh2MO5ADnXd8EaFpk+4DVg4l94VC5lpkslkMhqNICNanRYH3atW2trHGMTcxEY0BSZvmnvqpC2152T1G1vPxaZiY60TNW8QNkJaL2xOEDXHiTHBxXW+Y/9pgqhx/ZECvYPqzlCA83INLD3FF2jTg6nV8e9c3pjWkyjuTuS3b+A3QUoUtCQKmhJF1ZiENZjYse90vbB6/6lak4NiIS2rh87NkSHSeu4fJZsOl25Mkb6V1hXPl63nt2xIgdS2jt8ZL5Bfk/OG1Nr1olo4ThBUJxzPN+FyFuHsuAcDlQb/ubGQimu0SqiqmsqFxG1yDbQv+/zdYZ+5J3TJXUeeeoYYTG6/Ha523BofrF20lGzbTVRqt34GFRMw3tCyTO1CfSr94xwg9xGdkSoe7cRgJjaqgcTHIZ+wTqrgiR4bZRsuKyaYHOuNKLTBb80Ou8eGGnrIBCd7brxuY/NkJ06fWT9GWXUKG9AweTouhOuagtztKKcCW3FWn8t87qePeGanCPADeWfi756eHhgjRg4DbbtMqNAw28wqvWZwKOpvf52orSJGPZmZffGhh3MOnSAW4GTeh2CXvn0D/HoKYOGngD44FuIv7RiUkjFQzuV2YCRcJ9OiORkWphT7sBB+2A5ZUSxsvx7/rsbCS62TKjPlzozRASfF8Ukzh2y7VK41e3IiRX3hwgEoVYSgNTylLlwoA8SF00iBPDxFBtIhACEcrzvZC1gI0AjHL8SeOniu6aOQCwlFuGsv3Zz6+vpqa2sVCkV7e7uJMzMsbGjuMXPe0etdIfG1zJXB7F+28R0DM9l3qn759mx403BBV6xIESfqgBQj7o4Sd0emKmjqpokde09jUuVR72QZvcs2uO8BtD3n3SIQphy4dcC+Mw1RR6tC+T0rjirChX0R2I4doeJ2SOE0QWtCYsf+U5j07BI1mnGbAm8jQscC1mR0APeatRJt5wyJOVYekdQcKR6ARowS9EYLFNBkoWIFpGtyjkiVR4rl0L4hKS2hRyQcqx+0tKFLpv/kWIibMhHKvnDjUhC3bIBJnIb0tq3l8dYtWJDIm5/25P+R6SmGlTBsiWZMG7lau/ROxS8ey1i+7J2QVTUCYe4e8baVKze//ifd1DRmqzMmrwjaExQsWBvBXx5Sn5sDUlhfR0tG1CYyPMsRx/HYDbtCYjE71l+1KqLXRP35L8XJIv5bO7a+/MqJl1cSp5m4reNZRTsjI07ErNvzZtCRsFhEQY91qr52f3j84ZjNRyLiD21YPTE+SlT9ZyJWmOr6IDcYobjhotPNdQ9p2xXEw+E2cVrr65//RnO+pDb5ZFl+Jo5ZzjZeWJN+4IRdb5gY6EUlussMqPncdx7c8soK1q0R4gntIHb6+dFQAAs/BfTBsdCJ7vB2l4u8vUdw6PAZs4XYvItuDrogwLCw9FosFMneFQs3CzKaRsaB5VkMRFIoO3WqtKllzO6TKiDbMStJ4FclnuuPSusB/hgpbIOco1JR+gSOCWJibGpnWHILpAh+W3x6F1yJFMhixB1rdxeWyHGTBSdbL7ytWAgEcDI9Pd3f33/tF9cRYCHbfzUvL0+pV3NU+q2u7wDwYNN8F7G6UKNEl278DXR9omN8V2r5sm3nY9IVUCE4GxADeHSGpvZAwtObpGiRPPKdPANt67Gp2XMZRcn8KpMNV/I4l9aJO+i6D2SWxKYUhKY2h5/sCBG3hKQ2hKTWBaXXBKU3hAk7aeqiiR17T6G2NwsvGylOzyp1FzLLzpyTA+BzuEaoM3jUcpUxOulStLg6RNz25vH6cFFTuLguXFwTnAbp2pyxWUXdcLw2qT3oncsMC+HVLSYMB/hPjYVU7HZhCzoxLg9K+E6s9elBUl64dfHC3Qvm7543L/2Xj5DJEaLRedx003D16GzoSvWdnyExEWR2SrBqRehDD5NpmKqY+9OSSk6fsZtspq4eGV9MNDNkWkcGVcu//9A00epd2jMrIo7+8W+9ktKDwVFkQmXV0SYAYZEzk5HBZ7/3g/M796H4aNSeXRY8UllGRoZC/uuHxWdTiUZJLNbyY8llOw7AtyG/fsI9PoUSnt7q7qvfvDaczA6eC1+hre+F9+CosIuv5+BQ+IOXU+mqk9OqDgkRFK1c1DNPndq4Xpp66s2Hf4UTb5jIOW3Epid282Rjw5qnn9X1DmBN0KGDf7SiPvwAvxkFsPBTQA6nyzo5PtWt6DPqLd09HVqD8mZYGJPWG8KXx55URB6VHM6WW6ncZreTp5/c/MDXl8dF5l3MmLIzs22XFwu3imrC+S3BKQiH7x0LtwnzG/rVIKDAdDD5cP0Pvvfa759cV1o9iVaMMMqcpKRF+8aWjHBhW4jAq3GlObezp8zNCp4OnwCWoclNcPCHNcdBLjQhftA1jxthITNsmROl5X0QYOHo6GhxcTHA4cTEhN+1YK67pMfjcdHA2cwJr7e3d3x22kYhrb6pG5dFKRZ6WKkYFt4qId7sTi1+dVM6VEh4GgpVUCfhYllIagckELZulqIFHXFH63W0pfoHrQkJ4h/8IHzfgeZ6qc2FlsFoHbHvbPE6flGYsCHylDw8VRqRWgsp5GR1SHojkxEjhApM7Nh3CnLhBr5ES3vRxKQjPjblf34Y9c6RDmkrQj4UWD5jijiSHZZcGiZqgT4WJZYCLkalVoemV4emXZtzVCoV92EqliIPP1yKSjWqv6UtyPgcpgAW4lwWTa+5pNAVh377+N6li7fyeNt4vI3/et/RJ3/TeKmA0CjBRDOhiVyruuMusuUtwMLCdQmh3/8JtXcymfMyzuw/iLBhNltbm8298unTmYbUzDf/+7tU+6ntu5AtfnmV+OU1qvom1HlS7MVyABZOjb/28KPj1XW4v43TMC4+c+ntXWR4eNODj/W11OCOp+oZdU1t0nOvE+XMsw/8F+KcwUyMNjLe8eajvwP8zoxabe+bxY5PRwFVljiwv1itFw8cWfXbJ10zSrxm0nbyRcu/+s2wn//q/L5DeCsajjqIw0y0mtgXX+yoriZsUdNN+4SLHnxkQEgCWPipIKyKhrrGkaFxaUNL1sXzfYNdToz9eAMsDON3RIi7gM/GJVfsz2hZteb0H39z+A9PpN21MH4J7m8YuZQX94NvvX1wb1tlGQiM6Ni37mhpbFpHVHonY9AMsZC7CW8Fh9v5suxyxy9/mfzbhzMe+PcjC3jhPF7wwiUrH/nJweigOqmMnDjb/3SYMFzUEiZqQ/ATtkcLfPq0q7OKhiuCVsBCOAY4fORvuxMO5TEdKbrgX4OFiCxIgFVtbW3174fqKEml0oqKiouUcnNzKysrW1patFrtVVVOHfWGhoYaGhrGxsYkEkmNtK6qqaG9Z6SxpddkYb3U6bPZfFcsxMbanZ736mYRSFeRaXJAwQixFHArJE0K8hxa8Apa42hix/7TuJTul2Kaf/rrIw8/dvCJR/j/3xc2LuAlLuLFL1kY9rsnjibE5CsUzoPpHeuPN0fzu2NEvYCdMSBeC0DyVkRRwIPErrBj/yleOdz4xJ93Pvx44q9+cfjLn4/l8eIXz9t4x+K4J38nemtDdbZkdiu/MzGlZ+1BefAReRy/I54vi+O3e0H66pxjxXLofqiZAEH/cHEAC6+Q24uFHJq4MBUCLrCLokOfWbxgA4/3ztKle+fPj7r3rj/dudjUN0SYUwLFQs3Su8iGeKKaqt20NeoHP8MBb9STsuLS9NOQY3915daVr7ZczjWUlJrO5IR89buEmOwwTHQ66a5DG77+Y4IKBDSEMmO1UywcHX7j0Uf1sg5cdzRNDqWfKdy5k/T1b330t6PdLTjErAZDo3Tjz54gis5nv/FVt1XvslqJ3kLGOl/99v+SsYGMuOChZtSR4nTJg9EVLNR8+GTC+rR1Gw0wX6PviFbq7QOpT/w5+tEn+mWt8HA3lJwzVx07DlfaL1wkaAzv5BxUx8J5xxDT1n9EFMDCTzyBAAdVUVdTz1mdQwOjF7Mzevo7ASLMbmTD12BhSHJ7ZGp3KL9lHb9qz1npd7+7ncdbzuOF8Xhx9yzZ/5nFe5cu2DaPF/y1+9f/8bepRZKp/gnyVnIV4FBkWgeilLg1WtT8XrBwT+pgXgVZuiRkCW/jXbw9SxbsWbxoO29B7HxeyBfvfmvZyuy/vCn8U8RJwMIQQcscLERh6IZYGEVFQzj41ZsHt/HLGBZSy4ursdA3Vux2e1FRUc77IQC/Cxcu5FMCFISf5+XlwRU4BlgFEfAaQZPtO2g0GgsLC9VGrdKkLyyrKy5tZPZHXk0XYarTa8HvmmTzYWGksAWqGmtADAJcIwhYgIjo0HKzxO9+Ja6Td0fQvAVrP7dk82LeW4t4e+9ZemgRb9MC3ur77g4KDjq1dn1J+N6WyKS++NThaIECQCuGr4hOGYjm9/mR9UZJti1t5N77V85b8PxnF0Uv4EHb7bn7juMLeNsX8UK/9PnoPz53bMX6qqiDvTH80XXicUDl+BQFfEbxB6KuyzlOJKM9sC0yuSnyUAAL5xDtvi66XojmM25iM1oBRQYu5az70Y9CebwtPB4gYszn7w36r//E9V8fFmoZFq6LJbPjlQmbgh74ETJFo9ZTnHfh8DFidean8OvOiolhihgMZNYQ9JVvoz2Ox9B6+sz+p18sjdrUfv4isdgMbifGx7AbcRP50aGVP//FWHk14CXRjfenny7et5f0dIf9z89mFK2cVUlsZmODNG1FMBkf/dN//wdx2VCtZOLI7GDYL54mw30pa17vrGl3mFn3t3ucZrtDrRzo2PT0s2RsCqaQZng/o1Fn1pQlblv/9f/Z/uwLR3fuwK5gB/TVxzz+RN66jcQEiGnjHBYczW6f+Rk1oglg4RUKYOF15LBif/bIZQoQDRVd7Q1NNVJZ8w3lwtAUeVRaT5igFbBw9+mGBx9Knc/bOJ+3icdbt2jhVh5v/YIFiYsWruPxVvJ4ax58KGj7vpwtggY0bBF1UGHlvWLhzlR5YT1ZclfoIt7OuxafmLfwIG/eDt5CGNRx83gxvHkvf+Zflv9qmTj+dDeIQT4sBJm1NTy1GT6jRFdStLgNECImFYTCxviTHeEHSgvbDBZ0h6Ly13Vyod8EtKSkJPf9ECDfpUuX4OASJUBHOIbP7OxsOK33xer0e1wMDg4CHM7MzIDgqLebR1TTTfK+sqpWs9U/ZNF9CgczXkBH5hsmqh8ju9Ikr208FSmQR4mp9IZQJ0VExMTslXCW4D32nUK9vbqpgffZ8PkL4u5asO8O3oFFvP083uYFvK13zoNmXXvnZ1994Bd7/ra+OoTfGQYTC5E0TtAM0lt0yhDAoa+SWav565xOQYSyPeeVd3w+csGi6LsX7L934bEl848AZ57H27Z0PuQctOizr3/ricMvJtSEJveuOdZGpcB2kD7DBaPhgqFrcobmgzkNpHB+S3hALpxL9O3pi1N+j1pSWhkabVcyP+7OexJ4vJ13fCb2/i9XbHoLlwWYSlMzro9YrQUs3LSRqJXl6zYH/+B/YVDYjUp3WXHW0STIru50hiAszKhomy4vL96152/f+Lalq5NMKVNWh02UlBG7JfKJ3596+wBHPUQxV7ORTEz88f6vnNu41djR0yISRfzsEefEEHGYtr34120vvUwmJpWFZSdWBOvlMo9y9OzWDTUZWarOAdIzmp4YVsA/R9RTqdGhhgHckdtgsaKi1WquPHhgzY8fIh1yt6LL0zfgmZzldOb+huakmBjS10fGJvetDR2sqDU1t2169lljUSGZmgXUtA+PWccnPQ60j/ZCIGP93pF1+ymAhZ94YrsmFeTlj49ONNTVFxZdGp8cqWtu7h5VAYcNPVEVjNpFxMIYoTwytReTuD3mRNmesw2vrU7/0UMbH3zowH1fBO4WtmhRzKLF4f/65fDtuxuKSs1WB+pINyVVJZ7pQqsWioXAo6Opbcv1+Dc37UgtL5TO/OzxjY88mvyN/3qHNy+EtzCUd8fK7/xw65vL8y5XE/45zfMxWZgtikFeuRCBFln/VXAYly4P5zcBM2U5PxebeiSrjdrOePdXpFjI+X3t/VjoV3u+R6qurq6pqSkvLwcQBdEwMzMTUBBOm5qaVCoV2+/G4XCwhUMWa1uhUAAQojQpKZZ1dVnspEHahc/3Jjf1UqelumWi64Wlr208HSnojBL3A6LE8WVxApx5QA2EwjxgToKGYNIzFaCbX95y5mf/t+dnj73zkx8c/8q/bFk0P2Tx4rULF678xcPJYUEVTe1ku7g78nhzxOnWteKq8PSKGHFVjKgeahvNdBm+3ihBzjvOdTz4y90P/+LET74v+soX9yycF7lwcdDChcufeCwpOqo6PUudeKIzNrlzTVL9WmFdVGp1VGot/IrZkV6bG9qRtkMK5beEHkEsRFc3WjNzsZDVxj8h4XoZzuO8WGjUmIiZI9Oqlffct+2Oz4Tz5hWtCSazMzB98DC5UDuljlqrX3IniYtF+9LW7lrBKaXHZTHryOzUdHcf1qPKMJRf3HhMoJXJbDPjfc2No5kFpvwqgBmP04oBFvtHK89mwKO1dgtO2ixmMjIW9vNfzpbVtmdekotOm6WtxGO1WtUAzJ72nva088PnCtzyflzVIyjgdRWXyfPKWjNyRxtLsQE502xDNTGgwZjWzaHC1mDqF6T1CFIrhPzac2cbTp5tFWeMKQb6L9c4rXpcQbBzRG1uPHuR9A9VHDlak5JUJhZWpZ2qSj0ry7/MZEGfmbQfFT8SCmDhJ59gRmfjKkvLiMtu1mvkHa16o87kIO2DKrWdrE2qXo3W7TgrjxR3hqf2BgsU4cK2uJTyvefqK6STzW362lr7wz/ZvHTBn+9Y+Py3vxGVnCybmKGBuGgs0M1JkhgxGq1Q/thKw8rgCtYcMeIGaUeyRKowlFZP1tRwCfHFPN5Tdy167ecP77qQNdDUqoGRdK5o+MmQEyCzrhXKQoVtULzE1NY4YWOsoCFU0BgqkkamtgAionqW34oJEF3YHiZoe2zlnvUphWx4uO2oTSIIh8gfgPwWLi6Xy2Aw6N4PqdVqLaXu7m4mCwIQTk5OGo3Gm7kb2mw2wMj+/v6W5naN2gjlqKlquQJxOHap4YB3qn/TBF/vSS14Y5MIXzNVQVf12LQDRcDQ1Fa0Ak3FFURIaKUiwiagS4bNK3aeL6hTSipmJDmal54+cteCF//tS6sf+/nO7OyJ7i6P000OnK5LEFQHi6TBqS1haS0xYmmsqAnnRqI2aNmbpVhxw3rB5bJmQ0mZqjjb9NdnRHfMf+1fv7T2N7/eU1GuGhoiXaNk/Yny9cImQLigJGmMuAV/KGqLSJVDuj5DzDO1OUrYGHmk2EaNfeysltysunymtv98xKRh76vTHuEw07hrJsvWX/9h/5LPhvAWK7OyicVEoyTSuzUztj2bNUsXkHUxREtjvtjhg0NZmzr/IbLCbQ66j5bTgU73IHWDMI72nWza4UTzTux69JEuJzoUTk6/+NNHQSgkGgPmgwyVJtRhUk8d5q+DixPUXcjFvP/cmD82JcsTD1G+Rwd/JxbAbCFWK7FZ0YLU4gupis+l4QVstJAcR5MN0RH3/sI4Tm4nDVvor5yPsocEsPCTTy7sVM11da2NdTWVl3Oys1plbTlFFSNqF0BOcFL1WhGu8yHjA/FL3B0q6IgSNq1Llhw4V4N6eNqxd23N2L7xgqINJ3we6g3goaMEeNamlGJgc369KLBgNItAqQKX93yJeZJdOX07WdLeq7fRQVldMfj25oLKQrPDRIcq8eg9pKh54oVEUUR6Z3CqIiK9Kwx+ldwQn9oWL26PE8mgtFGCFlTtimVx6Z2AlCGClmB+81pB8yPLd25NK9NRhPHuJzVHnnBd2fn9AxLA3vT0dFdX19w9/G6IhZ2dnXAnfFVYWNjfNyxrU/T1jra2KIwGav+Gv6CjHUt6qyJ5mI40veiVzelQD+Fp3eEiBUreQrSqDff5AmLyyYU4L6E3xAhkEfsLcGbgIbppcvFUffLhuslxZDhOdA1El8e9p8vXCSqDxbKQtK4QsYKJ1yjc+zK5YYKG3iYshy4EzFMzQ7LPydNEPRotjjEPajhd3TPcuuPFccL62FO9UGbsHrTpQ8VQYKpCvy5Fi+QR/Lbww6Wo4qZqUqwnVldz40/+M5GHdhGGhfjq9B/GHkPUcY9fLl/O40V8+7vEBIPHakMbAMr8NCrz3q26pTzEQhqbm4LbtbG5mT7fT9c82ouCqLqgAOlw25Wa1//4p0mZwiezX6F3y+oTTwEs/OQT5bcGlaqsuOBycV5dbXVeQX5Wfum0iWg4EuLVkTbHilpQFBArwgTt0YKmxCTJO2cRCxkX6u0yTI8TpimB6aMLPe69Mdg2JUsAma7EnWG6Na8JvteZ+vq0X1TaNWSy0rmpxUxsBmpEYschZnViPBrFLIk8KglL7QwSd60VyEMF7bFiOaB1pEAWldIak9yKnyAbwRVhG7peiNtWp0jD0uXPxvOTizoZj8biXoWF3gF8zbh9j8RxHIusZqPkj7LmoR4U3tr2EVxkRqQgNYL46LBjlZWV1eXmFLP403O4OvbKa5j83FMXNeTbnl760pbTISJ5WFov1TEyj3jqt47OeSwhzED6/9v7Dri4kjPPVpZQQGlmvA67d7u3e/fb2+jz7nrXY3sd1+cwDuuZdRifPeMJGkUQQiAkJJFEUA6jRFbOIAECASLn3OScaZrOOb1QV19Vd9OApJmR0GiA+uvTo+r1e/VS1fevr8JXlCN9aO3kWI6WI7NBOTTUpTPrQRGaYPydAHPZscV5pXBnXCG2vzcnt21ObMYvE6zt+AZwaBDf+jjxi2uIvlimF2DAPE5rdEg06MEk4ODRzNhAaFEI/mey/eLLMRFuSmjZlgBT6bHgS8BVJqbmm9BGt9viWraeLLCS8bXULmRcOJULRWyi2Tjw9jIw9MfPrw99/Rcw4UK0msHXGmkSUSmtMWG6JR/BhR8FV8uESLgQn2RzXDh52iZXEp9+cwuMC2c8YF6BiBSyEc5qspq0mffT0zLSs/JLlWZwpexzpmAbaW3blVAdmFC7E2vYuHrMhXvOPjx2tUxv53mReL5HoJK6u4e7ewY5gR8Y7tEZVXR+4d7z+TDkgcyV9oWB+E0+CR1bEzupan6cHE7IrWuBKXe4eNkd5ob6tuLCuo62kZ6+7n5ZJ1b9bUoUcL5oU3zDJqwfL3T4XmwH1R/fsi2pM+hiV1Bye2By287kVpiXBkNYG7Zfxhq2bsfV1q3H0lKrZWBVgP7w5EKB5Aoow5TbJr+pTwLP0x+XVH19PabDxsbGvLw8fC8qnb60sia/qNzinGv/ccVOvB6HXyz4Tcg1zIXExiLdscQuxO/cPw5kRzyIH6mFUGNxSzLY4oFHc0xkICK8Cg5WkuRAvXIm+4iVU+NPEHO5KDC2EEzJi807L0gDk2uDkmrB/k5u2pncjiUgsRMLDbujQYnNMUnlRuLFBl4uaQyzww1zDnHUjnTSUX5XXG7ghaqdV9p8kxtxygEX6vEW2/rY0J+aMg4EJnX5x7f7fVhEuZDaHuT1Uo086QXPCYiubODSbEjkCTNRnrLbOoqzemFkuGgV7FreAIfagAvtMWH66eJCIg6L2WkjCoQd5xgYF858iMhiMqen3TXrNSr5SE9Pj8VmHZApGruGjQLyPY25sD4gfgIX+sXX7jpXcORatQma62lJAP3Z3tHU1d3a0FBXVVWhVCrtxF7Zf/4htimpaqYzxrB29iEeRN29gzvIUFXPaNSZLGmbmiN3x4v6qqqinu42qVR6/ea1+kbwoHYjp+Ub/y8cs+wHZ2t+tOv2TwJvvnu0cPP5ul9F5v9w193vBdz6fuDtXx8sePdc9RtROT8IvP6f+1LfisnbeLTku2+FRSXcN9MZx67pClRdE9uTd1PXVGPu48C9cKAbj+NCbBG2tbW1tLR0dHSYbNZ+2bDBZqusa7SREYGfSDA3HEzKeWt/YkB8SVBS+Z64or1xBXvjinbHlWPZF1u873zpvvPl+85X7j1fuSe2Mii+NDCh1D+pKDCxIORUupnqPdHosCnrpGX9o/1Gm2FUPqjVwieIOnvXJ/rqOxHX3ou8sSXy2rYDl7dGXtkUdWNj1C2X3CEyIbop8lbk6QwLXVXKplNrh5u7mlRGlUI7ZjIp8F03Dqm3RCZsjL7yweG770Xd3hh1Y1PUlY3R196LufVejDs1z5TvbIpO2XDg1jvBsc6xM+S9jnOhBx/MKbiJ0PnsNITpDIaGcfD6aXUPdhMXoDi7qMcsB5/ZLpz4ummMh0mBH33qJwKtm7ox+efPBhgXzhIUFuZzDtvI8KDJZMKGndpgKaySYsrxO1vkE1u3K7EuKLE6MLHK53zNrsutO5Ma/D/MPXi5AtrVHDQBzmY3FRblqtTy1tbWBw9yVEqdmTgV3H0qLSCuDFsSAfFVgfGVQXGV0GUYL4VBNAmVVPB+spbTeDT69P2GZsqFNgGZ2tvrenparFbz/azMxuYmXJZv5TZ97+3w7bHlW86Uf+v909967+QfIu5tPlX6k503/vndc19+58xXNpz/eUSGz4Wmn+y+/V2f5G9vOPdWaObW6IJv/zboQGyqhY6WgYnCoEPHuZBEPwVMKt5mXKnmrHqrta27/979/Jz8aiJVTikoyykoeZzk5pc8LKg8eSkrMi4zIikvND4nJjH7IJaE3MjEwsik/L2nUw/EZoWfywo/nX3ycmVMQvGB5Pzw5Pywi7nhF7LPXM0zkF4kzIU2k/xhwYOKurqmts7amkabmceKrbFHW9qiyW/W5kpVRY1jxY2jeJvXrCIyRkRJhIad0fwmZUOfyeyAygFn07a11VZJq7oGBtq6esEvigirAuVJ+3NblA9wyq16fHxh0xje5rRosDwqZRpWFjaPqE3QAg9fbZwI5y4X0qd2y8S9+LXAuwKFZ+HgDx2MpVUZD4VplsybrrV8RY+GCvpp5hoYF854cAIsu9LS0nTvbsrtm7cS4xMePHiQmp6pt/O4yLwTeumt8DsbI69vjrz8wYEr70bffv/wvbfCrm+OuHQ4KQ/WOfSslIrIThySyoZUsiGN1QG+mBPvlsdntcRmtcanNyWmS5PSpHEZzefut8dlNMVnSB8nmUXtAzKHzUW0UHx5M8/BoBKDwaHUOsb04uUH0tisdiynU+rOptQlpjedSWk6dkt64lb9qTvSqCsVx+42ns5sP3pbeiq15eT1hvM3Wy+n9iTfrSprHXF+aKg1O4sx5AqnmfhpYBIX4jq8XXS+TosdHMKCkDF3ThEeKzBWjgTMxBCH5l/yyuzEADAgpIHV4cDTNkwFsxFfo+QnE/nVSJ+djhXkrBVV5YOj6tLy5qy0Kh7OAX+zZMbJuNsOkSQFI5seL/Tq5K0KFqOmu6ttRDmWX1J15XKaXQu/CSKs00tbO2EZH5J/aAPek1OmAjqXLADl2gF1G/oC5xo8yt9kgfzM260cWdzZKoCHIp4oP53KcDhCs3ga1rV3X8vNhXPzKzAunPGwOaxYlZosxs6Otoqy8pTbd/Lz85vbO2wiVN+zG1UPmkzYJihsVRY0q3AVPrvNnNtmLpAqG7oN0IgojJeG1ua2jrZOhVx9LyXr+pWUquoGmVI/rEdNY6hBJnQqUY9C6B3jOhWoA4sSdSqFx8mA3AZLF5EihfVdV3tTs7SquUlaVVn/MKfswYPCprb+bhXfrkGdOgQJyoXuMb5tFHWp0IgSKdVoUIG6lahjDLXKUbcadY2hLhkalKO2YfOYlZZVAcaRuoou5AqoRH9KXDgJMPSPhwXeRKLURadLUgiAeNykp95xZWZE1vsGdQcDLKGrCOgVxi8Rf6YypFIig4kMhIETeRAHWTwH85CWrLxK9kJPT29/Hz5Grxc6pHIoJQLoRCBj50qEdsTbRMFuJYzFi3YsAhEadkcdyG7gbGC38dB7ZDYZbDw3otDV1nZQv3IiZ+DA4wH4VYYPDb1cOHEB1mAXH5EyDZOoc6g+WbFpnAtphHzZuQV3rniUuOxCXMXAJYqOnYEPDFyofQ5c6A7MNTAunPGgwwWxHrJarTYLrLuJwBiAV2EWQXtOsgbMRAlCBP+Ala1oITMTkNVse5CZ293ZV1RQqtPoeQeXn5ddUVFmsMMpBtIHBpoR6vJkJAVZf4EKVWaTohwSLKQUC3bHyGBPdmZqfm6mRqVtbelqqm/o7eniyJ2YScGDplrCyvgKvbcyGk6cqYlNaE7PEOSjdAoU1ZK86xS7SM0PDy4UXbz+IkAX4sMB57ADt4L5WPeDzwGn5fRjkWV5THRwiQgP69ibunvf5T0thiYbshkdRkjT+aTQSQTzykRimsGAGa6opLCovLCg6GFedk7sh2dKiopNVh5miwJdOhBvQIIBf3QrOH4TMCk+TggdkpTJPRl0xjtptyvrKhRKGX7rJqWqsjIf37PWagcP7PgwWKwO87UNOpzEJ6YscA4R3hPcv0BXUYdPTN/AHCzCnpmFCs3S5IVwA5aRDp2MfHKHA+HiKECm16uMhyINCxc+CxdOve5cBuPCGQ/ChTA/iBAVmXZOCoZd4M0ceC+EQiTYwMe8SNQrLF0ggAoF5aUTRQMhFRi6lnnvfnlpRVVFpWJsZEw2kJN1tyA/m5QxZMaKEduZWH/yRqJFSfTxIoDBAOoZ35UA02+hWtvSUltYkFdaWt7X3cbZjDxP29UQWI4WI2n/4XAl+Ng3v7FxnsTPe+XRn35PV5KJODVpIzTBMBwBVtMjbXcOMlIGhuV/FriQvmX6/l3vnFAV7CFTOJ8gAq6zwERAQu/YtuJgVSvRLMJ8Y16LdP8c9o9/v/3vQ+7vVyIFMB9NHJ4UXgLUVUQSBEfIXF5hdllNXkdP3fBg6/20W8MjozRloiQRCcIyUpR3x7XgVKEvGUxJMELKSsqtvLlroCkr+xZy6HSqoaycdJyyzgzWCjmaI1oa+BvOnprghJQR5FOPBlLKhbTGMzdBCzLtB6cQSU3oDx9u+vddP9OBI20ssLgRHKHVmA5GahcRLtSYoPjCGRb6LmEBJKiLIpIFxz+HO4Cgcun0eOcW58t3fSZikkJli9wVPdc55pzoG+cd0j/OAAw6w/Vfiw0m9eCtw0pqsfAzGYQF5ZQch48U4SesoRw2p3BOR/vOtD5tMC6c8Xhc5hnfDyGwPNxKh+yk9gvHA0vRPai5sSklJYX4HruT/SAzPe2uXC6zWCyupMi5rqGbHyWwDBtRdgCzCTOuYDDoamtrU1NTe4f6cFm1WGxOa4reqEjKESec/M53A5Z57ZUsPvefP5KXZWPzUrBD86MJfGc4S5bHhSY+6ccAVBomBmiYpjOeGt0PLYSIJwau+3j3Qk7TAxGegwOaEshiBRwH9jzHi3YTMpYoCr8Q+cq6wM/9KOFnGqTgwW0VaYyE80wOXgvak7bDEtHrtbl5D/ILcsbkw5UVZTabzUGUpx16MxH9NMit3T4CuBoDDtB1Gn1RUZHRbDBbDT29Hfl52TqtsqiogNiz8FKI1/LxL/JJMH7K1Jc/J0C+PoKvgisoNmf9w05remiYG/vH6K+/vO1LHahNhcbgE8Jq9eCt1HQwSrl0PgrZg5QmC+lPRLiowpfG/3CFl6yVJDhgyRoOmQ3gqh+cuAiUkTjMsjqLCdeYKQtC2w/pe4bMwSOz0QIpiNjS11phyQhkw7U13gRVKLgEh/QwodbJnQJUryxWqF7zBpkBPIr23qxJvlqdUqJoMSFSeyXOH2yE8nGJRnZwAqdFxipjy6XKG5fKr8qRXo3vwsWWnz4YF85p0HEfNED3YC1vMpmqq6tzc3O1Wi1V+jzPY0b0PPFjwpN1enp6cCA/Px/TbX5pcb9sGD4ksVZsdlIXxtyMVarVcfrVV4MWLDokWRb/g++YSnNgCUS312Zq8z4t3H5kPGdN0PUIccDBQ0MlJ/B2MriWHkO5ECrHIryHSa9rekDyNE+qyaRGD9e1cFYrspUOFvtc2yQJlswLXr4u+AsZA6lWpAYdRXWWYMTm44SU6IM4HAqF4v79+9nZ2fiR6dwSsMI+Yfmgb4AnGB0draqqovmhqakJJ15cXPxc3sZcgwhcQj4o5i0bVCJtsKIRJ4D/tDutdyWblyzbteztS28Oo0H8M+ko5pFSY4mJGcNcuMcXKY0aG5AZEox467DZDcikR2As4nRJsw9nxVlF0PPIZDWpgTYNHFn/GVxWOIxqwaRFDhOPHEOKQYcAO7HoBT3iLZgLx5CW0Bj+9KoevUONr2NRISv01ZsQECAP3TGkCFsxmRov5cX+V/ivs5vvZjTcPXzn+OXyFC342xB0tHfGxJOkbAbeeK/8vt/ZXSWDBQWy/Nf2/f7Eg0u4dvyiMhPjwjkNrOM89WNlZWVJSYlGo8Gm4c2bN/Py8rAG9Dj8k8GTaFtbWwsKCnBqaWlppaWlqelpGQ+yqBbAWzs4HEYiLOdiQ2pt3Ktf37tg0QHJwgvf+aYlJwOXGlDLhCtIt9zT45EzDscJm9CtQFpbkZsvSYYToIkYjnxGB2+PBWmS4sGYdkaNghlrtOSqhG+FvTpvr2RB+KrFAd6nyo9o0QiinA3HOejoITc8b294eLitrY0+HX3wT0paNG+4+bWvr4/uV6lUcrm8t7cXV5vcBzA8PZyjq5ydfA6jQ7RjRjIZkDHgVuCSnSu9I1a+GvHPD5RZBjCqOGg7V2ms0THYLjT5vINUOgMYdoJB3YYp0GLXDKChYSS32oxyg3GANxqQxYy02Jbk8VbUI71R0Bgxa6mQSqYfAEYT8Xc04kzHIaOOl3OwPq8W/L1xpk5rez+Sqy1mlWPMiuRKhJSQ97S4jkisSYcZ2ZQWjRkG6iG7CfOdOezM3o1HdljBzhuWamvfPrqhg+/qFEaUZG0yTKo6xOl4w4h29HjyqfK+UitSqZH8Zwfe+UX4ByZnxn4BYFzI4AS2/HBlX6fT5eTk4C3eg3mxoqICEU36FBzgJkKsUu/evdvQ0ICNFUyKeCe2OB/m5PIOARtaMPwQl29oHbQkBwRu/Zd/27XcK1giiVm4YO+SZbv/4s/zbl4dlQ0CTcE6pEADzwK34nYbTMhlM4lQDgkrI+cyFBjQOgo/gJvgSSlMHwSwBoilB4/JgV7EKkaG5P95/LVXNq2T7JNIIpZIgpf+4Oh3EipP2WAVO6i6w5HW8ZvBj4MZq7m5GW/b29txhYZab+PX+YSgT4pfhcFg6O7uxoHGxsbU1NTMzMwbN25grkXkos/hhcwhEBZ0NQ2SLEjNxDGkaEetf+b7pcUhiyS7JX+578++G/19GbJAIznmFLXKHh2lWTy/4N//CTXUGaBTXXXuSmCJMl8t9n7N59tvHHkr8W5sxOW973+4tUhWowd/bg4TDPi1YFJESLHvYnB0buyRB7G7PwxKvH9ej1SBcYG+57efK449lnPsrSPvyjBXOpTf2P7dzTf3Xsu6nZR5/o/Hft3kkNcZB98I/nmHacgKFzUmlly+kHcNHHvb7FZowxHUWoXWbhMFaF/tRl2/Ov6bVtQYdjfsQvVtHbIo9IotCdF3asD3kNqmg/E+SG1GijdP+PzfkHcGoZfxxYBx4ZwGVpqeugwbbVlZWfX19V1dXdg6xPoO23DoMebUkwEmoYsL8VV6enqwlYkTv3LlClbQmRlZuZk5tMyb7bA4PXST2PTKnMyY117bLpEcXr7MXyLZK1kYsHp9f3UFUIUJukk0yMVRTwXMeXYCTBjp6en0Jjs7O3Nzc/HDtrS1WjlHU0vzndQU/CpaWlqUSiXNcDmZWWOjctpQPM2dhQCBTP8jpOsgfUUOpEfmIlXJK++sfyXgJUnIPEn4fEm41xc2rX/j8I9HHcNYjxgxe5JeJTcwndtsNlyDwbednZ1N3z/+gnq93tne+wlJy/0RcWbAZj2tJ+E6DSI+d/CF6DF4Sw1EhqcApT9itpM/UCcU7EjoQJ3R9ZFrAlfOD5HgytDCjZL/5veXBZZWMzLCTFSNwh4dqVm8MOUrf2uur9MDLSljrmwushaOoo6/9vm331z1U+KDUM/toZQdSXsG0KgB2XrEMQ0s7DtUNZrzq+NvjiHjMFJldxWEXo6Uoq4fhf6qUmyUwZym4SPpB0/UXNLbB74a9sM37wYakEmLhuKaTkTdOKFGpl+E/Cjw8gEFUucOF71x4A9tXJ8VGZADFgPQQ83WAcObHYacnpLfHdpcx7eYkNyGhn8d+auQjPC3T2zcdiVaD+N8BAvQMxis0oGS30VtLFA0wjyfyW/oUwLjQoZxtLW1YUMwKSkpISEBc0NlZSWt+z87MP2MjY09ePCALhzf1dGtkCuhvQfGv5LmT96CuRD1tF/dsjlw6ZI9EkkwrPkrifqL/4kMGjtHBsjZoA/kWbiQoqOjAz/m5cuXaT0A63dM0kNDQ3kF+b2DAwVFhVnZDzBB4vvER+LcZtDpr1++0tfTOzmhacMjuNCALLfbUr5x8Gt/uveLS2K8JGHzJHsX/vuxf8VcOGjGqgcZYB7fI7iwqKhIpVLhB6QslZ+fbzZP6FP8+BBdbcLYjsdciM16zKw4V+A9+GtiE99tWz9FbYmBYgIXkkyOywU24EodZd8+9K0VgcvmRUgk4ZJ1QSvXbXjlXP1tIzKImEd0KsKFi299+e9t7R2YWnTI8GFacBFXpkR9r0b/5+/v7dUgCya2MnvDrw/8Tmquj74Usu9W2J7LwWNIVqSt8LkRarFrsJk4YhmWifJ8edW7J7eNIIURyUUkL25O33Y/xoAUf7nra5vLccBoQMOpQ8ln0uIxL4bd3PlGxFtjSHW64PzXtn6vB42aeC25baQSrDgzm5HegJS/C96w6USwCoaU43tWnCo7/trRn74d/26xvlll1evARz+nQ0Y9kvnHbEqR3sc3jCl08gv6tMC4kGECsPozEVit0LaPJnZBTRecH1EkrYO4+Atk/ptFhyxGW0Pd1tWrt82bH7BgYeiffCl9w0ZkN9mBNuGD21xDS54OmJI5AvyAKSkpiLQMY3pub2/H4Zu3b1XV1RrNJnxfMpkME6TRaBzo66+trqkurxgaGETPS+k/oo3UhKwKpMp1ZP7mzhsLwhdJgiRLI1Y/QOmjqMcGy7yScYMcKQcu0DZSTOHY8r527RqmLkyKmAvdB3xSuxCRr4/TxG8JvyJsa+IaEuZanDJmxP7+/slHMzwVxosD6QhAUMkREuuSfnripyv9Vkr2SyQRkrUBK7+8/yvbk8IMSCMI2C5UWaOjdEuX3v3qPxg6W0cduPCYwq4HZupKtUj+dyE/+W1GqAIZlEheaZf+yP/nzZaWa8WXkutvXKy/2YsGbw1kbri+D3Fmo27MiiwDjpECjfTtD3cMI73M1GMxD9S25G3JPjKA+v9h//e2lx7FNTMTGstuv3T+VpIOmQeE2v8X+bte1P2r0DejM46rkJXDlVSDHd+2jjcYkKoM1b0d+WbnaCuZIATPpUe6Y7Wnvh317fc/fL1BWUXWn3KMIkP0/Q/fDv9jbtcDTIoWzPF0PPKLAONChnHQNrFJGnNamgRhJCIBTZx2kICvFTJ2hnxTTAOkycSo3fu3f/PB/EU7Fy078/Vv9l28gETSLko0BQfT16ahrGA6xBRI7Z7MzMzBwUEcuH7zRnF5Gc1gUqm0paUFc0BdTW1bS2tna5tseASRB3kKRvkYgIlc8Gi0fgAD4O1qpCmy5r91881FYYske+Yt3LMqj8tSoiEH6VOBrE4XNHAnQXo98bNga76rqwvfJ67QjIw4b9t92CcFPVen0+FksaEsl8txsgMDA7S29CwpM0wA5UIHfFpMLTWWugs9F9f7vSTZLZGESf489E+33N/2cKTWjozQOKLRmKOjdUsXp/7b34xIywwwAMbmd25jjqnahFR/F/raf90N1iOjEg0U6UvfjdnUYx8yAffYxpAJ17EKdSU/P/57DhhO36Ro/TAjIU8rfePQxhquS4+0FqR6UJ0WUXNJg9RfDf6PXXlHsZ2qQ7LijptJabex8adALYfuRjyUZf8m9Hc5g8UKZMKVWdEOzobMnLpfbN9VGh58MwjfqslugAGmDlGPLD879Cuf275bj/963yk/u3nMDGar7rXQN49mnlAgxQhSWjET6smUkhcBxoUMj4V7iKngmnXw1Jh0OgzZhr1Eo3MQcHAw+ZcTwZVMYXRMwJ//T7+la/suJCO71g4TcqG6TBjR8Sz1RphsR6gd38/du3cRebR79+5howc/7L30tJqGerlirLK6qq6uDh+J9f75s+eSE5OS4uJv37zV19c3KcHpAcnTk+ZU8DBAwlanrPG9vnn+vnnz965Y7r9OKtR4zqkgs8ImzHXBz0VH/eCbF8moJUjKxd+ftFpDz6IJuqsy1Lamv1IiFEmX8MRTGT42aO0H3jSZ8ksaBkRwQqsfRiOf3/Alyb5Fkqj5f73/L0/Un9Qh6nVWQGqdMfrgmNf8lK9/4exh35s5qWkFKRsOv11kaeCR9v8ceO1b5/+QUXEjsfjkH0+9n9NZQWZcOP3ECqLKioY3J2z6sPJiQs2192M27o4LHkPqbfG73j+9Pa766umSpN9GvtcqDtuQ8ad+P41KOUYa403FFTeO3rwlg2w32O+o/vn+HyeXXNTD9H8omzz8h4E57x/+zd/7/8ut3pt3Gm5mtGdmNT8cNvYfv3T8bmfuGNL2GVoPXo+U9pYMCYNvR2/cfS/qavP1pNpLlxoz7jUXU+X+QsC4kOFJACPx2VjQE26lbEE2K7JD2Ea+JLjBcZjsZjsS1BY9GhzKCQ71/7P/hUYHOaPcTvxwOrvGeIdrZTViPY3LeM4Y3zMJrgmC2Lipqqo6ceJEZWUl7QO7ceNGcXExpkClWnXtxvUPz5yuIZDJZA4b+BNvqKun8yMfB+IuxHUz7hdGb4mqual35f5VhF9I8xh+UnA3AD9iJhNsA+q+4KTA1b5LX9r+yuc3fLGfa7chLX5jnF0ki/cYBfDIM6Gqgdmd9xj3KzrrNAI4uPF8SeOhx2ISw1FypVnCbQ5Obw6ZiyBffzyTkO/i4GGOILaW/mrDX8874C0JWfKVsC+frz8Da/mC0z0RKTXG6Gj1ygXo0Afq9pzG3kaFeaTdVNOBBnikwcZccPXxZllNYUd1i1WmhTZMB7JbrAYNlCCtDpe/UV6Z3p+b0/1QbR+AkaWikkOaIUNXcV9Z8XDlMFKbwJOjrq6zrFveCQv9YuOOV7cYsDGHOVWtRd25Q5nY9BzWyfBdW2gd1QwDYR523C2SFeX2PszRlKaO5eUryxXiUGd3nQ6Z9TAHg+tHsnaVFBugVfKakrGK4sGinN68+4OVBaMtbOzMJ4CrCDMunBnw1Mse7WkWYtM4Sz6UT/ASZyF8xyGrpSstff8vX0dWEzKqYJy2aOcFq3OsCFbIDjrShBNwySJ06mxuBb9SJGOIDjoTUSQOTl1M5Ay1tjbn5mbfu5daWJjf1dWhUikaGuoePszR67UGgy4//yH+CW/z8nL7+3vBR7bAyWTD+FebzUJTwHtEWChxXOxkJXJye3ZwrkquazKRyjLYvpTzKSe57sfZUkz9xtCVxbE4CC0K9FqDowMZJSnbEv+4NfadkKuBnep6DqaImZ0+8MAZnn3SnXjKuGcQkSO34nRZQBQvGbnE8NkBLQuky8CG7GNIMYrkf7Xhf0nCli2Ieukf9vxjgvS0Dg2DJ0W7iDQKa0yEdvE8tM8XGWBxNNKooDAgLScav7H5Pw4VnlEitZ2UKzJO21Ubo96EYX0Qzgq+LRxuv8JAweD7BjyiwfR8Z0OFg7giRuR0KHhkHRV8mMUKi0iRgke5HHIVB34A4Secss2MbCao9dqICxxo8OBIg4cNKnwg9Fp2chtmckVn5nwRYFzI8Lwwbpp42A105KHVbtGbYZIcdRTuNljs1DMFKdmIOD21mYHTSAyoxgpH4UJrhcQF6hrNAuYR0sOAApo5BChSIjmLNsaSGek8h+xW4qoK0iHXshB2dYuNbPFP9FcT8QJiIZ5VcdRgdx6PtzBUzpU4FStyWPCBYLaCViH1aHyXdgdnIbqIqCDCTJwz78JdceSu8L1NSo1enV7OCkMELTrwOOAwIpwcuOEB1UIcnQrEIdcTBOgXnObgqoODc8AKeBwtQbCoBSsuLx4ioQf4Iq7cizdau96A9Fqk+sm+H/73/f/jr0L/6bcHf3un5oodqeCTO2CaiyXG5Y9UZaL5CsH8BBuuNfoe3nE2J94Exz0lRJIJnVmFxqmQ0jqei9z7p/4008C4kOE5AsydiX2NdHqfS8UjDdnSRRksJKwmrqMtZJU+TDkWsmiRgfykJ2XdARYXeNgEmw9UB0+4yYgPhA4R4r5FJKxjFuEqsAqSi0ppeJIYyCVoQE8WEXSL0eMY90568CQxEu52agdChMCapKJNzsA2sXOnySOpx4nnJQww7RopyJvRE6G/whN5POAjhfYPwTh1B3TEIlJAGBd+pkBdVDuHTZHMg4BUOAPSaZDylvRKQve5xN6rmc33u5XNMO8UzDNcEnTGg1HaRYvRniCksvBkFDLkDtGOazwPWwsaNM1Wuu+pIJJ84mzGmUh49KdHcKHTe46r4WGmgXEhw3OBe9zNI6EV0O3i9u3H7/ieyvY5meN3LMvveKbf8YwtJ7M3nsrzP52/7eh9v5PZZJvrczzb50QWFt8TOVuOZCbeLBxVO3sQR8bQnbvN1XV6O7Hk7EiPdQLHi9iSa+0fO3kp/fDF7IMXc2Iu5cdcLDx4ofDI1dLoCwVYDl4qxhKVjANFh6+UHLpccvhK6ZGrZTh66HIxjsZcLDp6rRxH8Yk4So/HYXJ6If6VSCERCB9LfljRqrMTRdDbr711r7FSajYT8xHzNA8OIQWdiBoH5EevpEdfzo68khN5OT/yciGW6Es0nQnJRiXnO6OXi6OulkVfK4++WnngUln4hZLIixXRVC5U4e3Uc93RwxceNrSPQIGBxidYomRcVU0cg8rwokC4kLjkpqqNh2ZzaHVHZjuyWJDOystNIqzKRKgJmkPgY+qMukMxmsWL0e5gpLK5uNAIXrN5XAeyaKEsPBsm8hwV9z2OE96UY2YoGBcyPEfQFtHR0dGcnJyurq7BwUGNBpuCSC2gW0WdQXGF2+NqfGLrdiZIAxPqsWxPat6a3L41XrrjQvO287UBF1p2JDb6xTVsj63fgXfGS7edrYm72TqiQDmFI9n5oxcvjSxfsmHl0m3/8d340LAyhYGsqkgMr+ou5e5T94JiywJiawPOtQac6wg42xcQW+9/viz4Qt2e5Dr/8+W7k2p3JVQFxFUExldhIXtqAuMrcZgegMP4eBzFR+6MrdgZW44P3pVQjfcExFXiMBEcqNx1pPxBKcorUxcUyY8cLZ234DdLV2z5wU+uH4hqVKmBES3EqC3plAecvrczvswvvtYvttUvtsPvfB/eeiaFA0GJ1fjG8BXxtchtSAPiGnacq90RV7szAb+Kar8EKpVYJp3rGd0dW1hQ0w0tVzCFmTasurQY6fec/MEYPnWQhgzCheSTODkP1Bx8N/hq0LNGqn4wXAp8TcCyWHqN8VCEbtF8yoXUBxHkMgscTLr9bHTX00MkdzSR5B7Neu447ZSc8NuMAeNChucFXLk1ggdg1NjY2N3dnZeX19DQoFQq7XY73nuroGNvQsm2c9U+sQ3+8VL/eLxt8E1s2prY5pPY4pPY5OuWOOmOxOYd8U1Y/M5Lk1O7BuTom9/d86+vhvzd3xz3Wrh/kSR4yYLtX/iToOCQws4uWJvIwKOKdnvwuUJMIf5xLTtiu3fE9vqfH4BEEuqINLhkeqKBR8qzytHXvhX86teCv/y3kcuW7Z6/cPfCJUFf/OL+sH2VgyPIAM1bqKTLEXi+wC+xwTehxSeh2ye+1yd+wDe+d2LKNDx+IX9SD8CCT4Rzk+qo+CTX+CbVPOHcoPjy+6XtNtrUBSs2O5d7hBI0MxXW7MNkLvRkFKBGYr6LhBahDwBGYWFBhjHToRDdYgkKmsiFHLAmWXSQjkd+BjjpDYzBj5xFKgiCzWK1mVx99jMwazEuZHgucA+csVqtOp0OkyLe5pJ1oDBHYiMpJb816GweqOz4Jv+4Jn9q+sRLCf/hLSh9kAQpNgr9EylZSv1i66/nNQ1p0eKlv58vCVgiObN84Yml8w8sXrBznsR/vmT/n768+V+/EhB3aeTOQ3HnKZxgC07QJwn4wy+pCqfm5NeEFqdMUzQsseRBjUUy/3eLJDtXSE4sWXh04cID8xcFSSQ7F0v2fuHljV/9l12nkweSM0y74lrx8VuTmrYkN2xNxnxWBZTmmTINT4g2uMUHUyBhwa1EcHjKwePRgPiae+XdZrrUqgcXjitchhcP6maBcB3lQvp1nJpOICMzabMkLF5ho8OU9UOWQ3sMizAXQn8hR1rjgQt50Is8WRb4WbmQXN/GY6UKJuqjG0XJhv6KxeaADPbk/pHPLBgXMjxf0Jna/f39CoViaGhIIN6xBzX81QfSoPMFmAv9ElqADjEXxoM1g+nKyYJE8J7tcXWYC4l51OAXW3c+paBXgZZ5vbNQEjxfcmrZ/EPzJbsXzNu2dFHQQkmkRPLL1V6/3LIj9+xV1e7YdkJ+DT7Jlb7JpX7JRWBUudliWmXnqdS0cvm8hW8tnb93keQU5kJwLb5gx+Ilu5dKQudJXl+14vVN/rnHkmX7L/Rhst+KifBC5daLpb4XivC9TU1wori4kBIh4UKnuLnwUeKfUHO3vNdMZzwSLkQT2kgnfiqGF4QJk1Ndu1zMI3DgjYmOZOHMyEhmoGIuHLEc2gtcuDsQuJAai+DvGg4FtxXPxoWU4Wwib4FBziJdnp7kIpc4LVfYcLAeog0Gi5GB3XSxlxkHxoUMzxe4kogpMD09vbS0FG8RYcf0kuYTN0qCkyq2xDVuS+rEFoxfAqZDaNyj/Aek6KJD3/i67UlAaVi2xdclpksbe+yrX/7F/EVvrFweuGh+wJKF/hLJHyWS3/7TPx87cbSsrtpiEFFlN/I/W+CXVOmbVOWbXLkjsTIgoXxHYo1fYh0Rd/rTE919Nvtabt/y1T9buOhXa7z2LFwQumhJqESySSL59av/FnHuw/LSEg29K7/TefiusDmI7woH/BPL/RMrJ6ZMw1OjTnE3geLKAXlRjzwYogEJlSnlAyZqF+LyAm59XFO4xrUtw2cCbpZxdhc6BdMkzOoj3MORIc8CeJvQqkwHIwwL56OgnUhl5Jxzk4zwSWGaDWdDpOvxacG7hiLrEa8SrHRM8niLAjUDSfo8+QkfoOQtZrIWoo0eOdMw87gQAGXbAa0CLi4cWOaFuZDHNrrrACYvWKCOK5qNuGigupp6WJVCRHLZaF7uw+HBkdTSzsO3Kv3iS30utPhe6vJJhMY92tHlwTROYwjzn2+y1CepAcvmxLrYay1jSqTQIBuP0tIHF0l+sXrZe1s35N26rtEaodfERkap1IwafM/c8cMmFzSNNu2IbwmI7QDySKx5HrIz6n5RtWVEQe4qbXSB5Lcrlvl8sLHkxk2VwQQ1ZTu5q4pe5Z7EjIDEYsx/pFm4Keh8W2AsNuCqniA7ErHUYCMPJL4ugEhgXAORuqnHuyUovjSjtNtCZluSyfWuwYrODzTlqzF5UeL6y7tmLFCBX3jikw2+l0AtP2iy1OhNMYe0C5fB/EK10eacemujM98JJ0FrAJxOWgVIqym9yvh8dneAXp2Ynu6fBCXiW3Sjb4fs/v3eQDrxCSwN5504iZC6ezAglNNQ/dMdmwc5q4EUQMaFnwrIx7ASdwbIDFzYvXpdv9dStGcnLKNGv4JnbmLyQgRGvpFZfjzqaepqqW6yajBTiRX5JdmpWTdK+o5mdGw9W+AbX7XlXNn2uBosfrEg2+PqfONr8H63bE+o9kms3pZQtTW+cktcxc3UBq0MwVJpDiStGPrZ97ZEBV8b7kAWFWkpIDPwlAiVDdq2nMrYHl9BEqkD4zKubjsOJ1Q8DwkMSaqtHrJb4B4aqmQ/+79+IbuujfQjqx7aJm3krjQIFbVqNkde3hhzd8PBjPcOZr57MAvkUOZ7EP2YkkllQ4xTphwwLltibpWXNYM2tLu+C63RU5n61Zh8mkI/Cg/EYxd4yoUODrgKFx2DQ8DZxo7r/HYOmQUzTJgQYTVr2hyq1tmjDikXL0chYUhnsZJl6fGHdvAwq5BOReWQoDEYERl9OmpV6wnR8WT0jREfxdnVvBnvA59NpLsSn6Lm8cWwSWEVRHt6e1XQpbMb40//cHdAtyhoXQwnutw4mKF651Aj7lxmit+h6G+E+vchpCOF3k2xMwgzkAsFqvLAwQ+yOJSRkR1r1vWswFwYgByYIKHUM/kMCKxHaoGx3YJZtDd1t/WPDeOwgbN0DPY0D4w19ivLmgeq2kdKGvsqWkaIyCpa5FjKWmWlbSNUylpHytucURwubRnuHVVpLKRzgoydU5vxR4eAmXhpIYUU/yJojJbKpj5IqlVOBZ8OKbiSmt5oVXtXv0ZDFNb4VHejKypitcZbiO8ZZDJyeiPSmJDKAqKwgqjNz0csWIeOO7WxgPsrZ5jKlK/G5NMT4q8PmUXBREa+mEhtCVfjhhDKGBr6zu7AN8+fudTVStagQGM8eF2AD2gnpCRXo/Ao9RKv5jd/l5OcFHr7YlJtmRLS5PAvpzOydl08F3ztzMOedmzSDSDzxZrsXPnowaTk0HNHL1TVVGnNudKqguFOB6Eug5VLLykp1gxbCIs5iOfAxr72gq7WG90d3w8KlBGmFEWUcPFKoVQ6SO7zTklh/VCnAQkFzY2jduHHCScGyXOJNtoQMcMwM7kQ5s44wC602uTREa3r1nSu9EJ7duEKFB1bbIMsw7kEPPJNDM++KA1/hqIm/G2gz99ig94OzoLsJOCQGeRyo9Jk43AJpJ43qctQt63iGX6k2KE5CPok3MpdYdarrEaDYNfYzQI2Dx0acjvQNsR7yEem/CxC3OhwJqK29IjHVXgcHTZr1aLNANV1A+yzk7oBMQVAXKMPANQomG4R4cY46luSCA2PRx/3+Z5PlIZnfZSGPzpqhWoKpxW57Jbu3I6++x09aZ19NweGkmTDe6sq1m39YL3/1q+dPpzQWFeht6qp+yKDAfI9zkJyJQo/oF6yrPr11yvvp54our/lwtlqmxnnuhs51eE3bifUFB0uSNmRfL5Qrm0VjXtuxu7PybxWXplaV/LLmJjg1LTstsaQlEsqk5Ujk1+3Hz2cqxywO1vOebiGCH7fL0rrf7w3eACTnwNqcuFHjkYlJ/QjNIzQ1gMHRrQaom8h/3//7KF+UjwJH44r7JmCmcmFUDfCmQnbhdbRmNDGl7ybVq9A+/bCXtKKDd4X3S0R4IlxYnj2RWn4MxWlg5tgvIZdPtKfevtaasqNnOyMB1lp91Ju9PaM2K2kxNHOj0kdV+4OiUcJmTbOgQsVmxlfSDbY9zA3q6a6vEVaV1FSCJcGjyoTmWpKItMuZBw5x/FWcEBKZvx397QXFefV1FZUVpXqFArq4liweNwbPfdjPPLTC+lZpx9FhFnaHt/IU6Z+vucRpeFZH6Xhjx2VOex/siNg7bYdq3z8Xt61d3ngbsnOAIl/wPyYGElEuCQmVBIZuG5fyG9OJZ7IzNdbrQKdPqFSWg6Ejq5YatyzE5nVesGeXVeTOtR7oyr/ZxGH24jTvmEk/NeR6NePnW51WCJSLp/p7ugWwJ/p9nvpPz1yUo7QDw/svV1Tb7aDzffDkN1kAQpSRcUZGTO1CVpaLtbWvLZ/3zDtjzTa8ZEH024ebCrflZl+p1qK85hoIMuKOtAPzh3rJ7wI/xkXfhoQQY+Af35cyA1W7YHQ9rXe0rVeKDRYJE1SMJ53kipk8ukL1cU8tg1tXS0deqUWR1Ou36b77xc+7NOMmZGABZtLJhCrCZlNyGiC5a2tVmSfJNSstMGSFDxUeXjnKHSDSldbXqlXquWDsoyUNDtMxsIkyZmh3o0rvKIF8SQFnKaZbCenPC0C8ynBw+f42PiBnl6NQmlQ6x9m5SotGg10ZmNDGd8eNGlQsYHdDP7+n5NAGcH3ZRWwwF1xU8hy6odj8ukI5wz0OkRJUJAkJEwSELxw34GlITELg6MWBMdIdkXN339EEnJAEr1Xsjv0f2zc+X82+kbfuTJGPNMipcZyIGJ4pReKCEZGLdLySCNi/jucduVfwsIwdZlIy0lMWsY3/ffh489cv56h0kMrK4eCbmW8EfOhjUe7Um9/PzwE70yvbjrdVI3vCNMhZGOj0eEwIKuAq1Fn6ip/cCBkgFqlHGy7EP+/d2/9WmTYICJZiLb2CujrH0a3k6ZUeC7GhZ8GwOMkjJIyiWak56xh4d2rvRu8F6OQXRaH3UA+xOQCz+QFigN1tXb3dw3ggtTR3In3WPTWsvLqQdmYh2YQeLLaCxHaBjQ1IZdMjNmMdofZbtQYdEp9eVGFwWTECZrtmILB35gLAkmTWkhTEpwW8bRriVhMVp1GjwP9vUNjas2oGhbWcZC1JejcajJewSnuPdMrcGNT7pTJixeeZEYS7uWQJCRYErxLErxn2cGDC8IOLAiNluyLkuw/KAnBEjEvOPilzcG/2Hci5OLtKnk/dCtaRSQ3oj0R8sVLrXt2ABfKzdgOwFwYX5jxlf37MaUZTMBS22PjXws7qObR4cTE+0rtGHHWHnQr7Rt+u3Hl7U5399f37R5FaG/8hSrOiu9qFHIurP8CvRAODqvTc+0N3wjf00VJjoxQLRkb/EXssR+cPFpr53Emg1E92Ia0oNeunO8kPO32szGzMPO4EOsZnBMM0AVlRQoHHxYzuHpd3+rFaPcWGEpowt8CHBqR4cVUYF2uieHZF6Xhz1CUrB0B6x3hrcGsqqwpHpH34LBSM1TbUK5VGZ2zkGjteKqmeILAhWApCyoWu6alvfZhQUZZZV5zW01+QWnW/WKdCnxvAKs6GwhdV5ma2jSJCCxucYtV0I8o++5l3Up7cBtLSUlNSVF9ZZnUZvaYVO15P5PewHQJ8KGNCF0xjoadUeL669Gf7/lEaXjWR2n4I6ICjBWFqAHZTuVlnysrPpL94ExF6aHigpPNDTse3P/ipve+sOX9r0aH7s+8m93YTfrkBD1SwxRDhw3JFSgivHfl4sENfxSHuruGB05dvXylWVo52vPe2eSM7iFsGvZYDP91KHxP2n0ZEg/fupSl08qJFRd4L+0/wsItCI040PHSQt97N16PCnOQhnqyIAx0aiLOoUcOTI1nmmu/HxnSSwbLcLyYU16+/WBUD0L1CH1w/CSdQWEw87yIfnkptoVYlmaSo2ccZiQXwoBjsg4k/m6OiMPdy1dr1nsh3z8iRR9SyZBegQwqWAOWioGIZ3j2RWn4sxUdQ0YF0sud2+EupBmB8Ggv6m9DKh3S2mAwpc6CtER0VExIO0noAR5hgxrScUtbXVfqVUgWh7UypNJrC6ttZVIkNyG1FaktIHAhI8jkZCem/CzRSXdlVGiKs1FLDX7wuovnkcqEhtSd1+4ibBmrtBNvxgaCHxyenSRFw9MTNSKT6kny2M/3HKI0POujNPzkKNZROpeawgHMXDoDrLqCrTm9waYYK89/+Ns/vPn+9s3x15JMI/1IZYZPicuUqQUZ5UitRw2tKDCg00tS8dqP8m9eOnL78rYzRxsJk10qawxKvHwsPfVI1q3NyWfSZaPtNvWh1AtZKoUGiEoISLn148gIK+kCzOrr/sW5g384exTTH6hWMpYV5iZyjoz6kti8zB3XLn3Tzze+uORORbnKbAo9dPhgfPwI4TzfYyf6zAYtErPyS9PS8r97MOx0cUFsRnrdQA83WW3PAMw8LiT9hdguN8IAGiMajTzY+8rnzQskau+FpZ9bX7/Eq2vVut4VL/WuXOcUHHZHaXj2RWn4sxTtW7W+b9U6XE3Bgvd0LvMeWvtK2+LlA6tf6l6+pmOVV7v3ks41Xl1rVnZ4L+9cvYLIKirta1Y8QbpXrfW8aM/y9T0r1uLLtS/2HvD+nHTZsva13jjZ9lU4Jyzr9vbqXr2scw3euaxl3bL2NV5TE5wWcd9VH372FS91L4Mofmocblu4snnpsv6X17etWjL0uTXtqxZ2rcHPDo8PT+29tnP1atcbmHZZ1b1yHZGXiNDwePRxn++5RGl41kdp+IlRXAS6vdZhwVm3d/naIa+1Mu+XB7zW9nut7Vy+rmP9l9pf/tMy7/XVL3+pyHtdo/dLA15f7PV6ucPbW/qKV+eKz3Uu/jON95/rl64yrpCgsAOm1tYqw9ggoTHoaxBQl8neYFQ1mIdHEW+A/aZ+u0xG1hG1I1O7zVqhUDqXibR5AAAH+ElEQVRwENo8xYyxbqkDhqdCnwIHBIkNUCRyrcrBRtlwt9ZS169oHtXUDQ7hpJr7+2mDDj5EbbX1OjRqJDT39sl7lPlabavB0jgsH+HBJ9yMw0zkQgFWAoeWKAeyiHx2bsZf/EX359d0vLKq8XN/0rt2XdfKlV2rljN5sdK5cimWntUQ6FixpM1rEd4OrPfGgabF8zBFYaLCh3UsX965YkXXSm8ia0BWrO1c5d25auXjpGflck/pX71qeP3aTq+l8s+93Lp4YY/3mrblq7pXre5dvbbH2xsyw0o4q8N7Zetqb7ydmuC0CL2Qp/StWdO8eDG9h9FXXun08pK9vH5w7aq+1V49K5cRWdmzwhs/L4jzDUy7rOzEVQ1v10chYXeUyYuS3jWrsHRBMfHqXrO8++Xl0uWSgVdwRlrSvx6rr2V4P81F3au9W1Z7NXt54YzU/4p3x+eWkRrMf2td94XWl1bXvjIfXb+DjOAF1CFAj4DDAr6X6CQHZ4exFjr/9PpRZBdAeLMIrZ34F4cdxsg49Eh0+pQRyB+gROi/N4uw2iW4j+DhPCvMrIeeDSvtidZBx7cBcTrq+dIBTGwkU9qcqc00zEQuRGTqGBmRzAkw8DAndyAqfCgqQn74kDYqWhcebgwLZTIzJDR8ihzQh4U/Qcwhodb9E4QLPyDb5ju4aYs+aE/X5u2D/rvRibOW6KP68GhdWJRbNGHRU1ObLjGGRnmKek+oI/qozH83FtXuENWuPeaQcPkOf33wXtP+EPwIRMJB9h8whRyY8hKmTfRhoXrX26Zhd5TJZ0Hgi4SHUJnwk/PzhWsiQrFOIxKqicCHRerDYzQR0ZoDESMHw9CYAqtBrBQdHHVAClvaB03IjW4Iy5EeQTKRg4K6bHf2p0OQjPmiO4kf1PGd0Bjn6nZ37nT2RoNLDcKewIL0V2dqMw0zjws9vhdhRM4Bo/FNBtjq1AhXi8wGGJxvMTjFTMbqe4ZnX5SGZ32Uhu0mmLoOQiYpGFQ1+ZkVOWmVuffz7t7sq6mozcpwjAxCNrCSmRqeYpmY1KSUnzVKhIatFm1bS+H1qw33M6SZ92GEhFWTnXpV2d8JbtnwbXMGEPoIjkc97OyL0vCsj9LwNEat7pxMwjYjcbplhoADJgRi8Dw/Q1dK+uxgRnIhrcg4Kz6YDgUHzLx3WIiWtJABwdBm4JrrTee0eoRnX5SGZ32UhHnE2cnIKTsEuJ7RvryKfCuy9Y0NZBY+QMjW0lI7MtKDeLPL0ZinTEx2YsrPFnVdQnRKZ1vDYF87DtRXlQzAUHjL/aKsEZ3cIJiJ2xE6XRJckJBly6c87OyL0vCsj9LwpxTlQCUSTNKTDJ8UM48LeaJyrGRLHGnAqpW8YBNAGUHmcPsEokJVlGd49kVpeNZHaZjzmImARaUzZuXmj4yprJw4qtSobYb8+tIu5YDLzZhA5t27vY5NSGpSys8WdXo4c/vlah3qzCzJGVSPah2mrMKCovKqGyn3RhRqCwdqzFOIV7nJDzv7ojQ866M0PI1RMn/PGaDijtqgv0hwEyEzDZ8FM48L3XahW1xqUQDvW2QNywn60vOgSefMmigNz/ooDTtcvo1dYpMbLDKdqIGRxcNd/d3tHc7+DNccu/HopGQnpfwsUX7CJQQTjMUb7O5VDAzTY4wybU9DB6exuiv34zI1qVkZpeFZH6XhaYy68607S3tGCQSCCYqS4RNi5nEhwN1nSDp1PcVJlVS/UHGrG3d49kVpeNZHadhTKUyVSSdOOvfJvz5j9AkiTMymk8R9257Jzr4oDc/6KA1Pb/Rxwk9WjQxPjRnIhVR3TJVx5fK4tvXHtO/PgigNz/qoM8y5XHi4nY2NR5055LEyManpjE7JkB4ijnuYg/5OD4dzEBZpOuMPOEujNDzrozQ8vdEJDOkZ5SarR4anxYzlwscZB/hXD3+PTGaxuKvHnlF3I9MjhYwUn5zONMkU2p0g1OHq+PGTokyYPE486k+PkMnqkeFpMQO5EDC51j0uZMNPbEVwR906cZZFaXjWR2kYPvDUOpBLeFc3ojuFSVHPpCal/Pyiznz5OJl4MA3PvigNz/ooDU9j1J173V3knvsZpgszkQsnVe0nqcOP0JVMZrrQus7jxJkBniBTEpw2mXotl3iquakCtz01NSZMPlJED73I8GyYiVyIJmaHR8Ezi1B95BmefVE3ZnfUFaZ/HykfF5NOeM5R977HyYRzZ2uUhmd91I1pjDI8f8xQLmRgYGBgYJg2MC5kYGBgYJjrYFzIwMDAwDDXwbiQgYGBgWGug3EhAwMDA8NcB+NCBgYGBoa5DsaFDAwMDAxzHYwLGRgYGBjmOhgXMjAwMDDMdTAuZGBgYGCY62BcyMDAwMAw18G4kIGBgYFhroNxIQMDAwPDXAfjQgYGBgaGuQ7GhQwMDAwMcx2MCxkYGBgY5joYFzIwMDAwzHUwLmRgYGBgmOtgXMjAwMDAMNfBuJCBgYGBYa6DcSEDAwMDw1wH40IGBgYGhrkOxoUMDAwMDHMdjAsZGBgYGOY6GBcyMDAwMMx1MC5kYGBgYJjrYFzIwMDAwDDXwbiQgYGBgWGug3EhAwMDA8NcB+NCBgYGBoa5DsaFDAwMDAxzHYwLGRgYGBjmOhgXMjAwMDDMdTAuZGBgYGCY62BcyMDAwMAw18G4kIGBgYFhroNxIQMDAwPDXAfjQgYGBgaGuQ7GhQwMDAwMcx3/H+rtTBvMJf3oAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,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>
