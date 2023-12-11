# J.A.R.V.I.S-URDU
This is a desktop-based voice assistant project called "Jarvis" that aims to understand spoken commands in Urdu and control various functions on a computer.

# FYP Team

- **Mr. Arbaz Ameer Khan**
- **Mr. Anus Abdullah**
- **Mr. Zohaib Aamer**

**Supervised by**

- **Mr. Ali Raza**

**Department of Computer Science**

**National University of Computer and Emerging Science**

**Chiniot, Pakistan**

**2023**

---

## Title: Jarvis - Urdu

This work is the sole contribution of the author(s), and no part hereof has been reproduced on an "as it is" basis (cut and paste), which can be considered as plagiarism. All referenced parts have been used to argue the idea and have been cited properly. The author(s) will be responsible and liable for any consequences if a violation of this declaration is determined.

---

## Abstract

The goal of this project is to develop a desktop-based voice assistant that can understand and respond to commands in Urdu. Given the lack of publicly available Urdu speech datasets, a key component is collecting a dataset of Urdu speech samples from a diverse group of speakers, including children, young adults, and the elderly. Natural language processing techniques will be used to understand intent and generate appropriate responses. The result will be an Urdu voice assistant that can accept voice commands, understand the intent, and take actions or provide information back to the user through speech synthesis. In summary, the project will demonstrate the application of machine learning and NLP for developing conversational agents in low-resource languages like Urdu by creating the required annotated datasets. The working voice assistant can serve as a useful tool to improve accessibility and interaction for Urdu speakers.

---

## 1. Introduction

The document outlines a project to develop Jarvis, a desktop-based voice assistant that can understand Urdu speech commands and control Cross-OS functions. It discusses the motivation for increasing accessibility for Urdu speakers and bridging the gap in voice assistant technology. The project will involve collecting a diverse Urdu speech dataset, using machine learning for speech recognition and natural language processing, and mapping Urdu voice commands to Cross-OS actions. It details the functionality like launching apps, media control, web browsing, etc. that Jarvis aims to enable through conversational interaction. Overall, the project aims to create an Urdu voice assistant to improve hands-free desktop usage and accessibility for the Urdu-speaking community.

---

## 2. Vision Document

### 2.1. Problem Statement

Amidst the rapid advancement of voice assistant technology, a pressing issue remains: the exclusion of Urdu-speaking non-technical individuals from efficient desktop navigation and other functions. This language-specific gap underscores the need for a tailored solution.

Among these issues are:

- Exclusion from Digital Benefits: A significant portion of Urdu speakers are excluded from the advantages of modern computing due to the complexity of PC usage, hindering their participation in the digital world.
- Desktop Voice Navigation: Current voice assistants excel on mobile devices but lack efficient desktop solutions.
- Inconsistent Voice Recognition for Urdu: Accents, dialects, and regional variations can lead to inconsistencies in voice recognition, affecting user experience.

### 2.2. Business Opportunities

| Market Focus            | Description                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Market Demand: Urdu Support            | Growing demand for voice assistants catering to non-English languages, with a focus on Urdu. Significant market potential among Urdu speakers.                                              |
| Accessibility Solutions | Targeting individuals with difficulties in using traditional inputs (keyboard/mouse), including people with disabilities and the elderly. Tailoring the voice assistant to meet specific accessibility needs. |
| Cross-OS Compatibility   | Offering a voice assistant compatible with various operating systems, providing a unique selling point. Potential to attract a wider user base compared to assistants limited to specific platforms.        |
| Data Collection Services | Utilizing the dataset for Urdu speech samples to offer data collection services to companies and research institutions developing Urdu language technologies, such as speech recognition systems.        |
| Customization for Businesses   | Providing customization options for businesses to integrate the voice assistant into their operations. This may involve industry-specific commands or integration with business software.         |
| Language Technology Development | Applying natural language processing techniques beyond voice assistants, such as language translation, and text summarization.                                                                          |
| Education Sector         | Applications in the education sector, assisting students with language learning, pronunciation, and accessing educational content in Urdu.                                                           |

### 2.3. Objectives

- Develop a voice assistant that can understand natural spoken Urdu and carry out commands on a Cross-OS machine.
- Create an extensive Urdu speech dataset with audio samples to train the speech recognition model.
- Allow users to control Cross-OS applications like media players, web browsers, Microsoft Office, etc., through Urdu voice commands.
- Implement wake word detection to activate the assistant through a phrase like "Jarvis السلام عليكم" and many more.
- Achieve good accuracy for Urdu speech recognition as it lacks tools available now.

### 2.4. Scope

| Scope Description                 |                                                                         |
|-----------------------------------|-------------------------------------------------------------------------|
| Language Expansion                | Initially focusing on Urdu, the project aims to expand to include other languages and dialects in the region, significantly increasing the user base and market reach.        |
| Cross-Platform Compatibility       | Adapting to evolving technology, the voice assistant will work on various operating systems, including Windows, macOS, and Linux.                                                               |
| Continuous Improvement             | The voice assistant requires ongoing updates and improvements to enhance accuracy, add features, and adapt to changes in language usage and technology. The scope includes long-term maintenance and enhancement.                                      |
| Machine Learning and NLP Advancements | Keeping up with advancements in machine learning and natural language processing to improve the accuracy and capabilities of the voice assistant is part of the project scope.            |
| Voice Recognition for Diverse Demographics | Expanding the dataset to include a wide range of speakers, encompassing different age groups, accents, and dialects to improve recognition accuracy and cater to a broader audience.        |
| Language and Culture Preservation    | The project plays a role in preserving the Urdu language and culture by promoting its use in technology, including collaborating with cultural organizations and language experts.             |
| User Experience Enhancement         | Continuously working on improving the user experience, making the voice assistant more intuitive, responsive, and user-friendly.                                                             |
| Community Engagement               | Engaging with the Urdu-speaking community to gather feedback and insights, shaping the direction and scope of the project.                                                                    |
| Legal and Regulatory Compliance     | Staying informed about evolving regulations related to voice assistants, data privacy, and language technologies to ensure compliance.                                                        |

### 2.5. Constraints

| Constraint                               | Description                                                                                                                                    |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Collection Constraints              | Limited Urdu Speech Data: Collecting a diverse dataset of Urdu speech samples can be challenging due to the limited availability of publicly accessible Urdu speech data. This constraint can affect the accuracy of the speech recognition model.                                                        |
| Language Complexity: Urdu Dialects and Accents | Urdu is spoken in various regions, with significant dialectal and accent variations. Recognizing and processing these variations accurately can be challenging.                                                                                                           |
| Privacy and Security: Data Privacy         | Collecting and processing user voice data requires careful attention to privacy and security concerns. Ensuring compliance with data protection regulations is essential.                                                   |
| Language Support and Compatibility        | Ensuring seamless functionality across multiple operating systems is technically demanding and may require continuous updates to adapt to changes in those systems.                                                  |
| Regulatory Compliance                     | Voice assistants are subject to various regulations, including those related to data privacy, accessibility, and telecommunications. Staying compliant with these regulations is necessary and may require ongoing adjustments.                                                  |
| Testing and Quality Assurance             | Testing Variability: Testing a voice assistant across diverse Urdu-speaking populations is challenging due to differences in accents, speech patterns, and dialects. Ensuring accurate recognition for all users is complex.                                                                      |
| Linguistic Data Annotation                | Annotating Data: Creating a dataset for training the model involves annotating a significant amount of speech data, which can be labor-intensive and time-consuming.                                                    |
| User Education                            | Users may need training or guidance on how to use the voice assistant effectively, requiring resources for user education and support.                                                                          |

### 2.6. Stakeholder and User Description

## Stakeholders:

| Stakeholders Description | Responsibilities |
|--------------------------|-------------------|
| Project Team             | - Arbaz Ameer Khan - Anus Abdullah - Zohaib Aamer | - Development of end product, considering user needs. - Proper testing should be applied |
| End Users - Urdu Speakers | Primary stakeholders relying on the voice assistant for improved Urdu desktop accessibility. | - A little know-how of computer systems. Or the desired task they want to perform. |
| Panel                    | - Dr. Qamar-uz-Zaman - Mr. Usman Joyia - Mr. Ali Raza | - Gives direction to development team. - Ensures that the system will be maintainable. - Monitors the project’s progress. |
| Supervisor of Project    | - Mr. Ali Raza | - Requirement reviewer - Senior manager - Reviews implementation |

#### 2.6.1. Market Demographics

| Geographic Location      | Description                                                                       |
|--------------------------|-----------------------------------------------------------------------------------|
| Pakistan                 | Pakistan is the primary market for Urdu-speaking individuals. It has a population of over 220 million people, and Urdu is one of its official languages. |
| Diaspora Communities      | Urdu-speaking communities exist worldwide, including in countries with significant South Asian diasporas, such as the United Kingdom, the United States, Canada, and the Middle East. |

### 2.6.2. Stakeholder Summary

| Name           | Description                   | Responsibilities                                                  |
|----------------|-------------------------------|------------------------------------------------------------------|
| FAST Jarvis Developers | It includes those who are involved in designing and implementing this project. | - Development of end product, considering user needs. - Proper testing should be applied |
| End-Users      | End users include FYP Panel, students, admin, young, elderly, and children. | - A little know-how of computer systems. Or the desired task they want to perform. |
| Supervisor of Project | The supervisor will be stakeholders of this product as they are involved in the development process of this project with the development team. | - Gives direction to development team. - Ensures that the system will be maintainable. - Monitors the project’s progress. |

#### 2.6.3. User Environment

Some of the major user-environments can be:

- **Home:** Many users utilize the voice assistant in the comfort of their homes for various tasks, such as searching the internet, managing tasks, and controlling smart devices.
- **Workplaces:** In professional settings, employees may integrate the voice assistant into their workflow, enabling efficient access to information and improved productivity.
- **Educational Institutions:** Schools, colleges, and universities may implement the voice assistant in classrooms and libraries to aid students in language learning and accessing educational resources.

#### 2.6.4. Stakeholder Profiles

**2.6.4.1 Supervisors of the Project**

| Representatives        | Supervisor: Mr. Ali Raza                                                 |
|------------------------|-------------------------------------------------------------------------|
| Description            | He is involved in supervising activities of development process         |
| Type                   | He is our technical stakeholder. He has expertise in domains which are being applied to this project i.e. NLP, machine learning, Desktop-development. |
| Responsibilities       | 1. Gives direction to development team.                                  |
|                        | 2. Ensures that the system will be maintainable.                         |
|                        | 3. Ensures that there will be a market demand for the product’s features. |
|                        | 4. Monitors the project’s progress.                                      |
|                        | 5. Ensures that the project is following the documents generated during project planning and work products are properly delivered. |
|                        | 6. He will facilitate development team to complete this project within specified resources. |
| Success Criteria       | The completion of features which are being committed by development team at the start of the project. |
| Involvement            | 1. Requirement reviewer                                                 |
|                        | 2. Senior manager                                                       |
|                        | 3. Reviews implementation                                               |
| Comments/Issues        | None                                                                    |

**2.6.4.2 Developers of the Project**

| Representatives           | Mr. Arbaz Ameer, Mr. Anus Abdullah, Mr. Zohaib Aamer                |
|---------------------------|---------------------------------------------------------------------|
| Description               | They are involved in designing the system.                          |
| Type                      | They are technical stakeholders.                                     |
| Responsibilities          | 1. Should design this desktop application considering user’s needs. |
|                           | 2. Proper testing should be applied to make it as effective as possible. |
|                           | 3. Proper data is required for better recommendations                |
| Success Criteria          | The completion of features which are being committed by the development team at the start of the project. |
| Involvement               | 1. Designers                                                          |
|                           | 2. Testers                                                            |
|                           | 3. Data acquisition                                              |
|                           | 4. System Training                                                   |
| Comments/Issues           | None                                                                  |

## 3. System Requirement Specification

### 3.1. System Features

#### Speech Recognition

The system should accurately recognize and transcribe spoken Urdu commands from users, considering various accents, dialects, and speech patterns. Accurate speech recognition is fundamental for understanding user intent and executing commands.

#### Speech Synthesis

The system should be capable of synthesizing natural-sounding Urdu speech to respond to user queries and commands. Natural speech synthesis contributes to a more human-like and engaging user experience.

#### Wake Word Detection

Implement a wake word detection feature that activates the voice assistant when a specific phrase (e.g., "Jarvis عليكم السلام") is detected, allowing for hands-free interaction. Wake word detection ensures that the voice assistant is responsive when needed without the user having to press buttons.

#### Multi-Platform Compatibility

The voice assistant should work seamlessly across different operating systems, including Windows, macOS, and Linux. Cross-platform compatibility expands the user base and ensures accessibility on various devices.

#### Continuous Learning and Improvement

The system should continuously learn and improve its speech recognition accuracy and understanding of user intent through machine learning and user feedback. Ongoing improvement ensures the voice assistant remains up-to-date and responsive to user needs.

### 3.2. Functional Requirements

#### 3.2.1. Requirement Analysis

| Requirement                | Description                                                                                                                                                         |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Profiling             | User profiles like considering age groups (children, young adults, elderly), technology proficiency levels, and typical use cases among Urdu speakers.           |
| Feature Prioritization     | Prioritizing features based on the needs of Urdu speakers, emphasizing functionalities that enhance accessibility, usability, and address language-specific challenges. |
| Privacy and Security       | Identify and document privacy and security requirements, ensuring that user data, including voice commands, is handled securely.                                    |

#### 3.2.2. System Design

| Design Aspect              | Description                                                                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scalability                | Designing the system to be scalable to accommodate future enhancements and the addition of new functionalities specific to Urdu language nuances.              |
| Modularity                 | Ensuring a modular design to facilitate updates, maintenance, and the seamless integration of additional features for improved Urdu voice recognition.           |
| User Interface Design      | Designing an intuitive and culturally sensitive user interface that considers the diverse needs of Urdu speakers, providing a seamless and accessible user experience. |

#### 3.2.3. Implementation

| Implementation Aspect      | Description                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code Quality Standards     | Adhering to coding standards and best practices in .NET using Visual Studio to ensure maintainability and readability for developers working on the project.                |
| Error Handling             | Implementing robust error-handling mechanisms specific to Urdu language intricacies to gracefully manage unexpected scenarios and provide clear error messages.             |
| Version Control            | Utilizing version control systems like Git to track changes, collaborate among team members, and facilitate the rollback of changes if necessary.                          |

#### 3.2.4. Testing

| Testing Aspect              | Description                                                                                                                                                                       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Usability Testing          | Conducting usability testing with Urdu-speaking users to gather feedback on the voice assistant's user interface and overall user experience.                                     |
| Performance Testing         | Performing performance testing to ensure the voice assistant responds promptly to Urdu commands, considering various accents and dialects.                                       |
| Accessibility Testing       | Validating accessibility features by testing with users having diverse abilities, ensuring inclusivity for all Urdu speakers.                                                      |

#### 3.2.5. Deployment

| Deployment Aspect           | Description                                                                                                                                                            |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Training               | Providing comprehensive user training materials in Urdu, including guides and tutorials, to facilitate a seamless transition for end-users.                             |

#### 3.2.6. Maintenance and Support

| Maintenance Aspect          | Description                                                                                                                                                        |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug Tracking System         | Implementing a bug tracking system to efficiently log, prioritize, and address reported issues, with specific consideration for Urdu language-related bugs.           |
| User Feedback Mechanism      | Establishing channels for Urdu-speaking users to provide feedback and suggestions, fostering a continuous improvement cycle for the voice assistant.                     |

#### 3.2.7. Documentation

| Documentation Aspect         | Description                                                                                                                                                               |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Release Notes                | Maintaining detailed release notes for each version, outlining changes, fixes, and new features introduced.                                                            |
| End-User Documentation       | Developing comprehensive end-user documentation, including FAQs, troubleshooting guides, and best practices for using the Urdu voice assistant.                        |

#### 3.2.8. Timeline Management

| Management Approach         | Description                                                                                                                                                        |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Agile Methodology           | Agile methodologies will be used to adapt to changing requirements and deliver incremental updates, ensuring flexibility in response to user feedback and evolving needs. |

#### 3.2.9. Continuous Learning and Adaptation

| Learning Aspect              | Description                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Machine Learning Model Updating | Developing a mechanism to periodically update the machine learning models based on new data to improve recognition accuracy.                                                 |

### 3.3. Non-Functional Requirements

#### 3.3.1. Performance Requirements

| Performance Aspect          | Description                                                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Response Time               | The system should respond to voice commands in Urdu within a maximum duration of 1 second to ensure a seamless user experience.                          |

#### 3.3.2. Scalability Requirements

| Scalability Aspect          | Description                                                                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User Base Growth            | The architecture would gracefully scale to support a growing user base and accommodate additional features.                                                 |

#### 3.3.3. Data Assurance

| Data Aspect                 | Description                                                                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Protocols              | Implementation of robust data protocols for voice recordings during transmission and storage to safeguard user privacy.                                      |

#### 3.3.4. Reliability and Interoperability

| Reliability Aspect          | Description                                                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reliability                 | The system would demonstrate high reliability, ensuring consistent performance.                                                                       |
| Interoperability            | Ensuring interoperability with various devices and operating systems commonly used by Urdu speakers.                                                    |

#### 3.3.5. Internationalization and Accessibility

| Accessibility Aspect        | Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Usability Across Demographics | Evaluating the system's usability across different user demographics, including those with varying technology proficiency levels.                             |

#### 3.3.6. Maintainability and Resource Utilization

| Maintainability Aspect      | Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code Maintainability        | Code would be organized and documented for ease of maintenance, with clear comments for future development enhancements.                                 |

#### 3.3.7. Deployment and Installation

| Deployment Aspect           | Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Installation Ease           | The deployment process would be straightforward, with easy installation steps for end-users.                                                            |
| Adaptability during Deployment | The system would be adaptable to different environments and configurations during deployment.                                                           |

#### 3.3.8. Support and Updates

| Support Aspect              | Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Update Frequency            | Regular updates would be released to address bugs, introduce new features, and enhance performance.                                                     |

#### 3.3.9. Documentation and Translation

| Documentation Aspect        | Description                                                                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical Documentation      | Comprehensive technical documentation would be maintained that includes system architecture and interfaces.                                             |
| Accessible User Guides       | Ensuring that user guides and documentation are accessible to users with varying abilities.                                                             |

## 4. High Level Architecture Diagram

![image](https://github.com/arbazameerk/J.A.R.V.I.S-URDU/assets/90482025/4729fb1d-314f-4e27-9cbf-8b10a6c9c199)

