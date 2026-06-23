**EDURA – LEARNING MANAGEMENT SYSTEM** 

**By** 

**W.G.N.DANANJAYA SE/2021/047 R.W.V.I.D.RAJAPAKSHA SE/2021/029 P.D.D.RANSIKA SE/2021/034 H.T.MADUSHANKA SE/2021/011** 

**A report submitted in partial fulfillment of the requirements for the degree of Bachelor of Science Honors in Software Engineering (B.Sc. SE)** 

**Name of the Supervisor: Dr. Tiroshan Madushanka** 

**Software Engineering Teaching Unit** 

**Faculty of Science** 

**University of Kelaniya** 

**Sri Lanka** 

**2026** 

## **Declaration** 

I hereby certify that this project and the all the artifacts associated with it is my own work 

and it has not been submitted before nor is currently being submitted for any other degree 

programme. 

Full name of the student:…………………………………………………………………….. Welihena Gamage Nandun Dananjaya Student No:……………...... SE/2021/047 Signature of the student:……………………………                Date:……………………….. 30/04/2026 Br 

Full name of the student:…………………………………………………………………….. Rajapaksha Waththe Vidanalage Imansha Dilshan Rajapaksha 

SE/2021/029 Student No:……………...... Signature of the student:……………………………                Date:……………………….. 30/04/2026 ie 

Full name of the student:…………………………………………………………………….. Pathirage Don Danindu Ransika SE/2021/034 Student No:……………...... Signature of the student:……………………………                Date:……………………….. 30/04/2026 (772 

Full name of the student:…………………………………………………………………….. Hewage Thushan Madhusankha 

Student No:……………...... SE/2021/011 

Signature of the student:……………………………                Date:……………………….. 30/04/2026 

Dr. Tiroshan Madushanka Name of the supervisor(s):…………………………………………………………………... 

Signature of the supervisor:…………………………               Date:……………………….. 

ii 

## **Acknowledgements** 

The development team would like to express sincere gratitude to all those who contributed to the successful completion of the EDURA Learning Management System project documentation. 

We extend our deepest appreciation to our academic supervisor Dr. Tiroshan Madushanka, at the Software Engineering Teaching Unit, Faculty of Science, University of Kelaniya, for the invaluable guidance, constructive feedback, and continuous encouragement provided throughout the project. 

We are sincerely grateful to Mr. Dimuthu Prabath, founder of ICT – Dimuthu, Anuradhapura, for his willingness to engage as our client, for sharing his domain expertise, and for the time and effort dedicated to requirement discussions, prototype reviews, and feedback sessions. His practical insights into the operational realities of A/L ICT education were instrumental in shaping the EDURA system. 

We also wish to acknowledge the open-source community and the developers of technologies such as Next.js, PostgreSQL, Redis, RabbitMQ, and Microsoft Azure, whose tools form the foundation of this system. 

Finally, we thank our families and fellow students for their patience and support throughout this academic undertaking. 

iii 

## **Abstract** 

This report presents the design and prototype of EDURA, a cloud-native Learning Management System (LMS) developed exclusively for ICT – Dimuthu, an Advanced Level ICT tuition institute in Anuradhapura, Sri Lanka. The existing operations of the institute rely on manual methods for distributing course materials, administering assessments, and verifying student subscription payments, resulting in significant administrative inefficiency and limited scalability. EDURA addresses these challenges by centralizing teaching, assessment, and student tracking within a single, unified digital platform. The system is built on a microservices architecture using Next.js, Python, PostgreSQL, Redis, RabbitMQ, and Microsoft Azure, and incorporates interactive gamification, automated assessment grading, AI assistance, and an integrated hybrid payment system via PayHere. The design process followed a structured software engineering methodology, producing a formal Software Requirements Specification and a Software Design Specification prior to prototype development. A high-fidelity prototype was developed and validated with the client through a formal demonstration session and feedback review. This report documents the complete design journey from client engagement and requirements capture through to prototype validation and ethical considerations. 

**Keywords:** Learning Management System, LMS, Microservices, PostgreSQL, Next.js, Gamification, Assessment Automation, PayHere, E-learning, Software Design 

iv 

## **Table of Contents** 

Declaration............................................................................................................................. ii Acknowledgements .............................................................................................................. iii Abstract ................................................................................................................................. iv Table of Contents ................................................................................................................... v List of Tables ....................................................................................................................... vii List of Figures ..................................................................................................................... viii Abbreviations ........................................................................................................................ x Chapter 1: Introduction .......................................................................................................... 1 1.1 Client Details ............................................................................................................... 1 1.2 Problem Statement ....................................................................................................... 1 1.3 Proposed Solution Overview ....................................................................................... 2 1.4 Stakeholders ................................................................................................................ 2 1.5 Client Agreement Letter .............................................................................................. 3 Chapter 2: Software Requirements Specification .................................................................. 4 2.1 Overview of the Specification ..................................................................................... 4 2.2 Architectural Revision: Database Selection ................................................................ 4 Chapter 3: System Analysis and Design ................................................................................ 5 3.1 Architectural Overview................................................................................................ 5 3.2 Core Design Artifacts .................................................................................................. 5 Chapter 4: Prototype Development & Client Validation ....................................................... 6 4.1 UI/UX Design .............................................................................................................. 6 4.1.1 Design Approach and Tools .................................................................................. 6 4.1.2 Prototype Screens ................................................................................................. 7 4.1.3 Navigation Flow ................................................................................................. 34 4.2 Client Involvement .................................................................................................... 35 

v 

4.2.1 Client Demonstration Session ............................................................................ 35 4.2.2 Client Feedback Report ...................................................................................... 38 4.3 Ethical Considerations ............................................................................................... 39 4.3.1 Data Privacy and Confidentiality ....................................................................... 39 4.3.2 Academic Integrity ............................................................................................. 40 4.3.3 Fairness and Non-Discrimination ....................................................................... 40 4.3.4 Environmental and Resource Considerations ..................................................... 40 4.3.5 Informed Consent ............................................................................................... 41 4.4 Reflection on Stakeholder Communication ............................................................... 41 4.4.1 Communication Strategy .................................................................................... 41 4.4.2 Key Milestones and Stakeholder Touchpoints ................................................... 41 4.4.3 Challenges in Stakeholder Communication ....................................................... 42 4.4.4 What Worked Well .............................................................................................. 43 4.4.5 Lessons Learned ................................................................................................. 43 4.5 Formal Sign-off from the Client for the Development .............................................. 44 Chapter 5: Conclusion ......................................................................................................... 46 5.1 Degree of Objectives Met .......................................................................................... 46 5.2 Usability, Accessibility, Reliability, and Friendliness ............................................... 47 5.5 Future Modifications, Improvements, and Extensions Possible................................ 48 References ........................................................................................................................... 50 Appendix A: Client Agreement Letter ................................................................................. 51 Appendix B: Software Requirements Specification ............................................................ 54 Appendix C: System Design Specification ......................................................................... 55 PROOFREADING CERTIFICATION ................................................................................ 56 

vi 

**List of Tables** Table 1: Table of Abbreviations ............................................................................................. x Table 2: Business Model ........................................................................................................ 2 Table 3: Color Palette ............................................................................................................ 6 Table 4: Typography .............................................................................................................. 7 Table 5: Feedback Summary Table ...................................................................................... 38 Table 6: Stakeholder Communication Plan ......................................................................... 41 Table 7: Objective Completion Table .................................................................................. 46 Table 8: Timeline ................................................................................................................. 48 

vii 

## **List of Figures** 

Figure 1: Register Page ......................................................................................................... 7 Figure 2: Login Page ............................................................................................................. 8 Figure 3: Forget Password Page ............................................................................................ 8 Figure 4: Email OTP Sent page ............................................................................................. 9 Figure 5: OPT Verification Page ............................................................................................ 9 Figure 6: Password Reset Page ............................................................................................ 10 Figure 7: Student Dashboard ............................................................................................... 11 Figure 8: Logged-in User Exam Course Page ..................................................................... 12 Figure 9: Visitor Exam Courses Page .................................................................................. 13 Figure 10: Logged-in User Video Courses Page ................................................................. 14 Figure 11: Visitor Video Courses Page ................................................................................ 15 Figure 12: Purchase an Exam Course .................................................................................. 16 Figure 13: Enroll for an Exam Course ................................................................................ 17 Figure 14: Visitor Course Content View ............................................................................. 18 Figure 15: Video Course Purchase Page .............................................................................. 19 Figure 16: Video Courses Enrolment Page .......................................................................... 20 Figure 17: Visitor Video Content Page ................................................................................ 21 Figure 18: Video Lesson Page ............................................................................................. 22 Figure 19: Exam Page ......................................................................................................... 23 Figure 20: Exam Paper Submit ............................................................................................ 24 Figure 21: Exam Result Page .............................................................................................. 25 Figure 22: Graphical Dashboard ......................................................................................... 26 Figure 23: Numerical Dashboard ........................................................................................ 27 Figure 24: Logged-in User Leader Board ........................................................................... 28 Figure 25: Visitor Leader Board .......................................................................................... 29 Figure 26: Admin Dashboard .............................................................................................. 30 Figure 27: Edit Courses ....................................................................................................... 31 Figure 28: Create a Course .................................................................................................. 32 Figure 29: Navigation Flow Diagram .................................................................................. 34 Figure 30: Demonstrate User Login .................................................................................... 36 Figure 31: Discuss Student Dashboard Features ................................................................. 36 Figure 32: Walkthrough Courses View Page ....................................................................... 37 

viii 

Figure 33: Client Agreement Letter - Page 01 ..................................................................... 51 Figure 34: Client Agreement Letter - Page 02 ..................................................................... 52 Figure 35: Client Agreement Letter - Page 03 ..................................................................... 53 

ix 

## **Abbreviations** 

_Table 1: Table of Abbreviations_ 

||_Table 1: Table of Abbreviations_|
|---|---|
|**Abbreviation**|**Full Form**|
|LMS|Learning Management System|
|SRS|Software Requirements Specification|
|SDS|Software Design Specification|
|API|Application Programming Interface|
|UI/UX|User Interface / User Experience|
|RBAC|Role-Based Access Control|
|OTP|One-Time Password|
|JWT|JSON Web Token|
|MQ|Message Queue|
|CDN|Content Delivery Network|
|WCAG|Web Content Accessibility Guidelines|
|A/L|Advanced Level|
|ICT|Information and Communication Technology|
|B2B|Business to Business|
|SLA|Service Level Agreement|



x 

## **Chapter 1: Introduction** 

This chapter introduces the EDURA Learning Management System project. It outlines the client background, the problem that motivated the system, the proposed solution, the key stakeholders involved, and the formal client agreement that governed the engagement. The chapters that follow build upon this foundation by presenting the full requirements, system design, prototype, and validation work undertaken by the team. 

## **1.1 Client Details** 

- **Client Name:** Dimuthu Prabath 

- **Organisation:** ICT – Dimuthu 

- **Address:** No.472, Right bank, Pemaduwa, Anuradhapura, Sri Lanka 

- **Contact:** +94 76 373 5379 

ICT – Dimuthu is an Advanced Level ICT tuition institute operating in Anuradhapura. The institute provides educational content, assessments, and coaching to A/L students across Sri Lanka. At the time of engagement, all operations, including distributing course materials, conducting assessments, and managing student payments, were handled manually, limiting the institute's ability to scale and deliver consistent quality education. 

## **1.2 Problem Statement** 

The existing manual methods for distributing educational materials, administering assessments, and verifying monthly student payments for Advanced Level (A/L) ICT students at ICT – Dimuthu are inefficient and difficult to scale. The absence of a dedicated digital platform means: 

- Course materials are shared through informal channels with no structured delivery. 

- Assessments are conducted manually with no automated grading or progress tracking. 

- Student subscription payments are collected and verified by hand, creating administrative bottlenecks. 

- There is no centralized dashboard for teachers or administrators to monitor student progress. 

A dedicated digital platform is required to modernize and streamline these educational and administrative workflows (Pan et al., 2024; Liliasari and Riza, 2023). 

1 

## **1.3 Proposed Solution Overview** 

EDURA is a smart, cloud-native Learning Management System designed as a B2B custom solution exclusively for ICT – Dimuthu. The system centralizes teaching, assessments, and student tracking on one platform, making learning more efficient, engaging, and easy to manage. 

Key capabilities of the proposed system include: 

- Structured creation and delivery of digital course modules and video lessons. 

- Automated execution and grading of student assessments with progress tracking. 

- Streamlined collection of student subscription fees through an integrated hybrid payment process (automated PayHere gateway and manual receipt verification). 

- Interactive gamification to increase student engagement (Zeng, 2024; Nguyen-Viet et al., 2024). 

- AI assistance for students and teachers. 

- Comprehensive analytics dashboards for administrators and teachers. 

- A secure and fair assessment environment. 

The system is built on a microservices architecture using Next.js, Redux, Python, MongoDB, Redis, Azure, Docker, RabbitMQ, NGINX, and PayHere, with cloud hosting on Azure. 

Business Model: 

_Table 2: Business Model_ 

||_Table 2: Business Model_|
|---|---|
|**Aspect**|**Detail**|
|Client Focus|B2B custom solution developed exclusively for ICT – Dimuthu|
|Revenue Model|One-time development fee with ongoing SLA for maintenance<br>and cloud hosting|
|Value Offered|Reduces manual grading and tracking while enabling island-<br>wide student access|
|Cost Structure|Cloud hosting, database services, and third-party platforms|



## **1.4 Stakeholders** 

The following stakeholder groups were identified for the EDURA LMS project: 

1. Client and System Owner: Dimuthu Prabath (ICT – Dimuthu) The primary client and owner of the system. Responsible for providing domain knowledge, validating requirements, reviewing the SRS, providing feedback on the prototype, and formally signing off on deliverables. 

2 

## 2. End Users 

   - _Students:_ A/L ICT students who access course content, take assessments, track progress, and manage subscriptions. 

   - _Teachers:_ Educators who create and manage modules, lessons, and assessments, and who monitor student performance. 

   - _Administrators:_ Institute staff who manage user accounts, subscriptions, payments, and overall system configuration. 

3. Development Team 

   - W.G.N.Dananjaya (SE/2021/047) 

   - R.W.V.I.D.Rajapaksha (SE/2021/029) 

   - P.D.D.Ransika (SE/2021/034) 

   - H.T.Madushanka (SE/2021/011) 

4. Academic Evaluators 

Supervisors and assessors from the Software Engineering Teaching Unit, Faculty of Science, University of Kelaniya, who evaluate the project against academic requirements. 

## **1.5 Client Agreement Letter** 

A formal agreement has been established with the client, outlining the project scope, deliverables, timeline, and mutual responsibilities. The complete, signed Client Agreement Letter can be found in **Appendix A.** 

In summary, this chapter established the foundational context for the EDURA project by outlining the client's background, the problem statement, the proposed solution, and the key stakeholders involved. Building on this context, Chapter 2 will present the Software Requirements Specification (SRS), translating these high-level objectives into the formal technical requirements necessary for the system's design. 

3 

## **Chapter 2: Software Requirements Specification** 

The formal Software Requirements Specification (SRS) for the EDURA platform is established in this chapter. The precise functional and non-functional requirements necessary to build the system are outlined. These specifications serve as the definitive blueprint by which all subsequent architectural and system design decisions will be guided. 

## **2.1 Overview of the Specification** 

The core capabilities of the system, project boundaries, and operational constraints are defined within the SRS. It is utilized as the contractual baseline between the development team and the client. Due to its length, the complete specification is included at the end of this document. Refer to **Appendix B: Software Requirements Specification** for the full details. 

## **2.2 Architectural Revision: Database Selection** 

Following the initial SRS compilation, the primary database technology was revised from MongoDB to PostgreSQL (Neon). It was determined that a relational database better supports EDURA's microservices architecture by ensuring strong transactional consistency and relational integrity (Kleppmann, 2017). The appended SRS should be evaluated with this final architectural decision taken into consideration. 

In summary, the SRS was introduced in this chapter as the strict functional guide for the system, and a critical revision to the database architecture was formally documented. Building directly upon these requirements, the structural design, data organization, and component interactions of the system will be detailed in Chapter 3. 

4 

## **Chapter 3: System Analysis and Design** 

The complete System Analysis and Design for the EDURA Learning Management System is presented in this chapter. The architectural structure, data organization, component interactions, security measures, and user interface designs are formally defined. These technical specifications serve to translate the established system requirements into a comprehensive development blueprint. 

## **3.1 Architectural Overview** 

A cloud-native microservices architecture is utilized for the system infrastructure. The platform is supported by a technology stack comprising Next.js, Python, PostgreSQL (Neon), Redis, RabbitMQ, and Microsoft Azure. Through these structural artifacts, the theoretical requirements of the system are translated into the practical framework of the implemented solution. 

## **3.2 Core Design Artifacts** 

The system design is detailed through comprehensive modeling, encompassing class diagrams, sequence diagrams, and database schemas. In addition, initial UI/UX wireframes are established to guide the visual interface. Security frameworks, including Role-Based Access Control (RBAC) and JWT-based token management, are also formally documented within this phase. Due to the comprehensive nature of these technical models, the complete System Design Specification (SDS) is attached in **Appendix C: System Design Specification** . 

In summary, the architectural structure, data schemas, component interactions, and security designs of the EDURA platform were established in this chapter. The transition from these theoretical design artifacts to a high-fidelity, interactive prototype will be documented in Chapter 4. Furthermore, the UI/UX validation process and subsequent client feedback will be detailed in the following section. 

5 

## **Chapter 4: Prototype Development & Client Validation** 

This chapter documents the transition from design artefacts to a validated, interactive prototype. The wireframes and user flow diagrams established in the SDS (Chapter 3) were developed into high-fidelity prototypes and reviewed with the client. This chapter covers the UI/UX design and prototype, the client involvement and validation process, ethical considerations governing the project, a reflection on stakeholder communication, and the formal client sign-off. 

## **4.1 UI/UX Design** 

## 4.1.1 Design Approach and Tools 

The high-fidelity prototype for EDURA LMS was developed using Figma. The design followed the wireframes documented in Chapter 6 of the SDS, extending them with final color schemes, typography, iconography, component styling, and interaction flows. 

The visual design language for EDURA is built around the following principles: 

- **Clarity:** Clean, uncluttered layouts that guide users toward key actions without distraction. 

- **Consistency:** Shared component library (buttons, cards, navigation bars, form fields) applied uniformly across all screens. 

- **Accessibility:** Design adheres to WCAG 2.1 Level AA standards as specified in the SDS, including sufficient color contrast ratios, keyboard navigability, and screenreader-compatible markup patterns. 

- **Engagement:** Gamification elements (badges, progress bars, leaderboards) are visually prominent without disrupting the core learning experience. 

Color Palette: 

_Table 3: Color Palette_ 

|**Role**|**Color**|**Hex**|
|---|---|---|
|Primary|Teal (Teal-600)|#0D9488|
|Secondary|Blue / Cyan|#2563EB|
|Background|White / Gray-50|#FFFFFF / #F9FAFB|



6 

|Success|Emerald (600)|#059669|
|---|---|---|
|Error|Red (600)|#DC2626|



Typography: 

_Table 4: Typography_ 

|||_Table 4: Typography_||
|---|---|---|---|
|**Usage**|**Font**|**Size Range**|**Weight**|
|Headings|Inter|24px – 60px|Bold – Extrabold|
|Body|Inter|14px – 18px|Regular – Medium|
|Labels / Captions|Inter|12px|Semibold – Bold|



## 4.1.2 Prototype Screens 

The prototype covers the following key screens 

## 1. **Authentication Screens** 

_Figure 1: Register Page_ 

7 

_Figure 2: Login Page_ 

_Figure 3: Forget Password Page_ 

8 

## _Figure 4: Email OTP Sent page_ 

## _Figure 5: OPT Verification Page_ 

9 

_Figure 6: Password Reset Page_ 

10 

## 2. **Student Dashboard** 

## _Figure 7: Student Dashboard_ 

11 

## 3. **Course Catalog / Browse Interface** 

_Figure 8: Logged-in User Exam Course Page_ 

12 

_Figure 9: Visitor Exam Courses Page_ 

13 

_Figure 10: Logged-in User Video Courses Page_ 

14 

_Figure 11: Visitor Video Courses Page_ 

15 

## 4. **Course Content Viewer** 

_Figure 12: Purchase an Exam Course_ 

16 

_Figure 13: Enroll for an Exam Course_ 

17 

_Figure 14: Visitor Course Content View_ 

18 

_Figure 15: Video Course Purchase Page_ 

19 

_Figure 16: Video Courses Enrolment Page_ 

20 

_Figure 17: Visitor Video Content Page_ 

21 

_Figure 18: Video Lesson Page_ 

22 

## 5. **Assessment Interface** 

_Figure 19: Exam Page_ 

23 

_Figure 20: Exam Paper Submit_ 

24 

## _Figure 21: Exam Result Page_ 

25 

## 6. **Progress and Analytics Dashboard (Student)** 

_Figure 22: Graphical Dashboard_ 

26 

## _Figure 23: Numerical Dashboard_ 

27 

## _Figure 24: Logged-in User Leader Board_ 

28 

## _Figure 25: Visitor Leader Board_ 

29 

## 7. **Admin Dashboard** 

## _Figure 26: Admin Dashboard_ 

30 

_Figure 27: Edit Courses_ 

31 

## _Figure 28: Create a Course_ 

32 

## 8. **Profile and Settings** 

_Figure 29: User Profile_ 

The complete system prototype can be access through this link : https://www.fgma.com/design/CB3GDL3dKsDPegDXhxUDFj/Untitled?node-id=01&t=qEOOU9KuvRrZ8R9l-1 

33 

## 4.1.3 Navigation Flow 

## _Figure 30: Navigation Flow Diagram_ 

34 

## **4.2 Client Involvement** 

This section documents the active involvement of the client, Dimuthu Prabath (ICT – Dimuthu), throughout the project lifecycle. Client participation was central to ensure that the delivered system accurately reflects the real operational needs of the institute. 

## 4.2.1 Client Demonstration Session 

A formal prototype demonstration session was conducted with the client on 29/04/2026 via Google Meet Platform. 

## Attendees: 

- Dimuthu Prabath (Client, ICT – Dimuthu) 

- W.G.N.Dananjaya (SE/2021/047) 

- R.W.V.I.D.Rajapaksha (SE/2021/029) 

- P.D.D.Ransika (SE/2021/034) 

- H.T.Madushanka (SE/2021/011) 

Agenda: 

1. Walkthrough of the high-fidelity prototype covering all three user roles (Student, Teacher, Administrator) 

2. Demonstration of the payment flow (PayHere integration and manual receipt verification) 

3. Demonstration of the assessment and auto-grading module 

4. Review of the gamification and AI assistance features 

5. Open Q&A and feedback collection 

35 

## Proof of Demonstration: 

_Figure 31: Demonstrate User Login_ 

_Figure 32: Discuss Student Dashboard Features_ 

36 

_Figure 33: Walkthrough Courses View Page_ 

Summary of Discussion: 

The demonstration session commenced with a brief overview of the project scope and the design decisions documented in the SRS and SDS. The team then guided Mr. Dimuthu Prabath through the high-fidelity prototype, walking through each of the three user roles in sequence. 

For the **Student role** , the client observed the registration and OTP-verified login flow, the student dashboard displaying enrolled courses and gamification badges, the course content viewer with lesson navigation, and the timed assessment interface with the auto-grading result screen. The client noted that the dashboard layout was clear and that the badge and progress bar elements would be motivating for A/L students. A question was raised regarding whether students could resume a partially completed lesson, which the team confirmed was a supported feature through the lesson progress tracking mechanism. 

For the **Teacher role** , the client reviewed the module creation interface, the lesson upload workflow, and the student performance analytics panel. The client expressed particular interest in the analytics dashboard, noting that visibility into individual student progress was something entirely absent from the current manual system. The client requested that assessment results be exportable, which the team noted as a post-prototype enhancement. 

For the **Administrator role** , the client reviewed the user management panel, the subscription status overview, and the payment verification workflow covering both the automated PayHere gateway and the manual receipt upload path. The client confirmed that the hybrid 

37 

payment model accurately reflected how the institute currently collects fees and that the manual receipt path was essential for students without access to online banking. 

The session concluded with a general discussion of the planned technology stack and hosting approach on Microsoft Azure. The client expressed overall satisfaction with the prototype and indicated that the system, if deployed, would significantly reduce the administrative workload at ICT – Dimuthu. 

## 4.2.2 Client Feedback Report 

Following the demonstration, client feedback was collected in writing via email. Feedback Summary: 

_Table 5: Feedback Summary Table_ 

|**Feature /**<br>**Area**|**Client Feedback**|**Action Taken**|
|---|---|---|
|Student<br>Dashboard|The layout was found to be clear<br>and intuitive. Gamification badges<br>and progress bars were appreciated<br>as motivational elements for A/L<br>students.|Design<br>remained<br>as<br>presented.|
|Assessment<br>Interface|The timed quiz interface was well<br>received. The client asked whether<br>partial<br>question<br>saving<br>was<br>supported in the event of a network<br>interruption.|Noted as a reliability<br>requirement,<br>to<br>be<br>addressed<br>in<br>implementation through<br>session-state persistence.|
|Lesson<br>Resume<br>Functionality|The<br>client<br>enquired<br>whether<br>students could resume a partially<br>completed lesson.|Confirmed as a supported<br>feature<br>via<br>lesson<br>progress tracking. No<br>change required.|
|Analytics<br>/<br>Progress<br>Tracking|The client highlighted this as a key<br>value-add, noting that individual<br>progress visibility does not exist in<br>the current manual system.|Retained. The analytics<br>dashboard will be a<br>priority<br>in<br>implementation.|



38 

|Assessment<br>Result Export|The<br>client<br>requested<br>that<br>assessment results be exportable<br>(e.g., as CSV or PDF) for record<br>keeping.|Logged<br>as<br>a<br>post-<br>prototype enhancement<br>for the implementation<br>phase.|
|---|---|---|
|Payment Flow<br>(Hybrid)|The manual receipt upload path<br>was confirmed as essential for<br>students without online banking<br>access. The automated PayHere<br>path was also approved.|Design<br>retained<br>as<br>specified in SDS|
|Overall<br>Impression|The<br>client<br>expressed<br>general<br>satisfaction with the prototype and<br>stated that the system would<br>meaningfully reduce administrative<br>workload at ICT – Dimuthu.|No<br>changes<br>required.<br>Formal<br>sign-off<br>to<br>follow.|



## **4.3 Ethical Considerations** 

The EDURA LMS project involved working with a real client, real institutional data requirements, and a system intended for use by students and educators. The following ethical considerations were identified and addressed throughout the project. 

## 4.3.1 Data Privacy and Confidentiality 

As stipulated in the Client Agreement Letter (Section 1.5), the team committed to maintaining strict confidentiality of all proprietary or sensitive information disclosed by ICT – Dimuthu. Client-provided information was used solely for the purposes of this academic project and was not disclosed to any third party without prior written consent. This obligation extends for a period of two years beyond the project's completion. 

Within the system itself, student personal data (names, contact details, academic records, payment information) is protected through the following measures defined in Chapter 7 of the SDS: 

- Role-Based Access Control (RBAC) ensures that only authorized roles can access sensitive records. 

- JWT-based token management with short expiry and secure refresh flows. 

39 

- Data encrypted at rest and in transit using industry-standard protocols. 

- Input validation and sanitization to prevent injection attacks. 

## 4.3.2 Academic Integrity 

This project is undertaken solely for academic purposes. The Client Agreement Letter explicitly establishes that the University of Kelaniya and the student developers disclaim all warranties and accept no liability for direct, indirect, or consequential damages arising from the use of the software. The client acknowledged and agreed to this condition prior to engagement. 

All work presented in this report is original. Any third-party libraries, frameworks, or resources used are acknowledged in the References section. 

## 4.3.3 Fairness and Non-Discrimination 

The EDURA system is designed to serve all registered students equally. The assessment module implements an automated, rule-based grading engine that applies identical evaluation criteria to all submissions, removing potential human bias in grading. The gamification features are designed to motivate all students, not to disadvantage lowerperforming learners. 

Accessibility was considered in the UI/UX design phase. The interface adheres to WCAG 2.1 Level AA guidelines (W3C, 2018), ensuring the system is usable by students with visual or motor impairments. 

## 4.3.4 Environmental and Resource Considerations 

The system is hosted on Microsoft Azure, which provides cloud infrastructure with industryleading commitments to renewable energy and carbon neutrality. By digitizing course materials and eliminating physical distribution, EDURA also reduces paper usage and the logistical footprint associated with manual educational operations. 

40 

## 4.3.5 Informed Consent 

The client was fully informed of the academic nature of the project, the scope of the system to be developed, and the limitations of the student development team. All agreements were formalized in the signed Client Agreement Letter dated March 22, 2026. 

## **4.4 Reflection on Stakeholder Communication** 

This section reflects on how the team managed communication with stakeholders across the project lifecycle, what worked well, what challenges arose, and what lessons were learned. 

## 4.4.1 Communication Strategy 

From the outset, the team established a structured communication plan to ensure the client and academic supervisors were kept informed and involved in key milestones. The communication channels and cadence used were as follows: 

_Table 6: Stakeholder Communication Plan_ 

|**Stakeholder**|**Channel**|**Frequency**|
|---|---|---|
|Client (Dimuthu Prabath)|WhatsApp / Email / Over<br>the Phone|Weekly|
|Academic Supervisor|Email|Monthly|
|Team|WhatsApp group/ Over the<br>Phone/ In Person|Daily|



## 4.4.2 Key Milestones and Stakeholder Touchpoints 

- Initial Requirement Gathering Meeting - February 2026 

The first meeting with Mr. Dimuthu Prabath was conducted to establish the scope of the EDURA project. The client described the existing manual workflows at ICT – Dimuthu and the specific pain points around course material distribution, assessment administration, and payment verification. Key outputs from this meeting included a shared understanding of the three user roles (Student, Teacher, Administrator), the need for a hybrid payment model, and the requirement for island-wide accessibility. This discussion directly shaped the problem statement and scope documented in Chapter 6 of the SRS. 

41 

- SRS Review and Validation - March 2026 

Following the completion of the initial SRS draft, the document was shared with the client for review. Mr. Dimuthu Prabath confirmed that the functional requirements, use cases, and business rules accurately reflected the operational needs of the institute. Minor clarifications were incorporated into the final SRS. The client signed the Client Requirement Sign-off page included in the SRS appendix. 

- SDS Completion and Internal Review - March 2026 

The Software Design Specification was completed by the team, covering the microservices architecture, PostgreSQL database design, security design, and UI/UX wireframes. 

## • Prototype Demonstration - April 2026 

A formal prototype demonstration was conducted with the client. All three user role flows were demonstrated using the high-fidelity prototype. Client feedback was recorded and is documented in Section 4.2. Following the session, the client's feedback email was received, and the formal sign-off process was initiated. 

- Final Report and Submission - April 2026 

The final design report was compiled, incorporating all prior deliverables, the prototype documentation, client validation evidence, ethical considerations, and this stakeholder communication reflection. The report was proofread and submitted in accordance with the Software Engineering Teaching Unit submission deadline. 

## 4.4.3 Challenges in Stakeholder Communication 

- Geographic distance between the team (Kelaniya) and the client (Anuradhapura) required all meetings after the initial contact to be conducted online, which occasionally limited the depth of interactive feedback possible. 

- Aligning the client's availability with the project's academic deadlines requires flexible scheduling. 

- Translating technical design decisions (e.g. microservice architecture, the Database Schema) into client-accessible language required the team to develop clear, nontechnical summaries and visual aids. 

42 

## 4.4.4 What Worked Well 

- Regular, brief updates instead of infrequent long meetings kept the client engaged without being burdensome. 

- The structured Client Agreement Letter established clear expectations from the beginning, preventing scope creep. 

- The visual prototype (Figma) was highly effective in making design decisions concrete and reviewable by a non-technical client. 

## 4.4.5 Lessons Learned 

- **Establish written expectations early:** Using formal agreements (like the Client Agreement Letter) at the very beginning is crucial to prevent scope creep and ensure everyone is aligned to the project's boundaries. 

- **Translate technical choices into business value:** When communicating with a nontechnical client, it is essential to explain architectural decisions (like using microservices or PostgreSQL) in terms of their practical benefits, such as scalability and reliability, rather than just technical specs. 

- **Optimize remote communication visually:** Managing a long-distance client relationship requires structured, asynchronous updates to avoid meeting fatigue, as well as using high-fidelity prototypes to make the feedback loop faster and more effective. 

- **Document all interactions for traceability:** Keeping formal records of client discussions is vital for tracking exactly why specific design decisions (like the payment model or dashboard priorities) were made, making it easier to justify your work. 

43 

## **4.5 Formal Sign-off from the Client for the Development** 

## _Figure 34: Customer Sign-off Letter_ 

44 

In summary, the transition from theoretical design to a high-fidelity, interactive prototype was documented in this chapter. The UI/UX design process, the client validation session, and the formal acquisition of client sign-off were comprehensively detailed. Furthermore, critical ethical considerations and reflections on stakeholder communication throughout the development phase were addressed. Building upon these validated deliverables, the overall success of the project will be evaluated in Chapter 5. The degree to which project objectives were met, system limitations, and potential future enhancements will be formally concluded in the final chapter. 

45 

## **Chapter 5: Conclusion** 

This chapter draws together the key themes and outcomes of the EDURA LMS project. It reflects the degree to which the project objectives were met, evaluates the system's usability and quality attributes, acknowledges limitations, reviews the project timeline, and identifies future possibilities. It also comments on how the project experience connects to the team's academic formation and future careers. 

## **5.1 Degree of Objectives Met** 

The primary objective of the EDURA LMS project was to design and prototype a smart Learning Management System that centralizes teaching, assessments, and student tracking for ICT – Dimuthu. The following table summarizes the achievement of the project's key objectives: 

_Table 7: Objective Completion Table_ 

|**Objective**|**Status**|**Notes**|
|---|---|---|
|Define system requirements<br>in a formal SRS|Achieved|69-page SRS completed and<br>validated with the client|
|Produce<br>a<br>system<br>architecture<br>and<br>design<br>(SDS)|Achieved|58-page<br>SDS<br>covering<br>microservices architecture,<br>database design, class and<br>sequence diagrams, UI/UX<br>wireframes, and security<br>design|
|Develop<br>a<br>high-fidelity<br>interactive prototype|Achieved|Prototype<br>developed<br>in<br>Figma covering all three<br>user roles|
|Conduct<br>a<br>client<br>demonstration and collect<br>feedback|Achieved|Formal<br>demonstration<br>session held on 29/04/2026|
|Address<br>ethical<br>and<br>confidentiality requirements|Achieved|Client Agreement Letter<br>signed;<br>data<br>protection<br>measures defined in SDS<br>Chapter 7|



46 

|Obtain formal client sign-<br>off|Achieved|formal client sign-off signed<br>on 29/04/2026|
|---|---|---|



## **5.2 Usability, Accessibility, Reliability, and Friendliness** 

**Usability:** The EDURA prototype was designed with simplicity and role-specific clarity as guiding principles. Each user role (Student, Teacher, Administrator) is presented with a dashboard and navigation tailored to their specific tasks, reducing cognitive load and minimizing navigation depth to key actions. 

**Accessibility:** The design adheres to WCAG 2.1 Level AA, ensuring sufficient color contrast, keyboard navigability, and semantic structure for screen-reader compatibility, as specified in SDS Section 6.3. 

**Reliability:** The microservices architecture chosen for EDURA (SDS Chapter 2) provides fault isolation; a failure in one service (e.g., the payment service) does not bring down the entire system. Redis caching and RabbitMQ message queuing further contribute to system resilience underload (Sharma, 2025; Thallapally, 2024). 

**User-Friendliness:** The prototype's user-friendliness was positively validated during the client demonstration. Navigation is effectively streamlined via role-specific dashboards, and student engagement is fostered through gamification. The analytics tools were specifically commended for resolving past manual inefficiencies. Although formal end-user testing is pending, initial usability expectations were successfully met. 

## **Limitations and Drawbacks** 

- The prototype represents a design and UX validation artefact; a fully functioning production system has not yet been deployed. 

- External service integrations (PayHere, Asgardeo, Azure deployment) were designed and documented but are dependent on production credentials and infrastructure provisioning beyond the scope of this academic project. 

- User testing beyond the client demonstration was not conducted due to time and access constraints; a formal usability study with actual students from ICT – Dimuthu would strengthen the design validation. 

47 

- The AI assistance feature was designed at a conceptual level; the specific AI model selection, prompt engineering, and integration testing remain as future work. 

## **5.4 Timeline** 

_Table 8: Timeline_ 

||_Table 8: Timeline_||
|---|---|---|
|**Milestone**|**Planned Date**|**Actual Date**|
|Project initiation and client<br>identification|December 2025|December 2025|
|Initial client meeting and<br>requirement gathering|January 2026|January 2026|
|Idea pitching and poster<br>presentation|28/02/2026|28/02/2026|
|SRS v1.0 draft completed|12/03/ 2026|15/03/2026|
|SRS reviewed with the client and<br>finalized|21/03/2026|21/03/2026|
|SDS v1.0 draft completed|12/04/2026|19/04/2026|
|Prototype (Figma / XD)<br>developed|25/04/2026|27/04/2026|
|Client demonstration session|28/04/2026|29/04/2026|
|Final report drafted|28/04/2026|29/04/2026|
|Final report proofread and<br>certified|29/04/2026|29/04/2026|
|Final submission|30/04/2026|30/04/2026|



## **5.5 Future Modifications, Improvements, and Extensions Possible** 

The current scope of EDURA was defined to meet the specific needs of ICT – Dimuthu as a B2B custom solution for A/L ICT students. Several future enhancements could extend the system's value: 

## **Short-term (0–6 months post-deployment):** 

- Full production deployment on Azure with live PayHere integration. 

- Onboarding of initial student cohort and teacher content creation. 

48 

- Formal usability testing with real users and iterative UI improvements. 

## **Medium-term (6–12 months):** 

- Mobile application (iOS/Android) to complement the responsive web interface. 

- Enhanced AI assistance: personalized learning path recommendations based on student performance data. 

- Automated certificate generation with digital verification upon course completion. 

- Integration with third-party video hosting (e.g., Vimeo, Bunny.net CDN) for improved streaming performance. 

## **Long-term (12+ months):** 

- Expansion beyond ICT – Dimuthu to serve other A/L tuition institutes as a multitenant SaaS product. 

- Advanced analytics with predictive modelling (e.g., at-risk student identification). 

- Live class / virtual classroom integration. 

- Offline content access capability for students in low-connectivity areas. 

49 

## **References** 

Kleppmann, M. (2017). _Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems_ . Sebastopol, CA, USA: O'Reilly Media. 

World Wide Web Consortium (W3C). (2018). _Web Content Accessibility Guidelines (WCAG) 2.1_ . Retrieved from https://www.w3.org/TR/WCAG21/ 

Liliasari, L., and Riza, L. S. (2023). The Impact of Learning Management System (LMS) Usage on Students. _TEM Journal_ , 12(2), 1082–1089. https://doi.org/10.18421/TEM122-54 Nguyen-Viet, B., Nguyen-Duy, C., and Nguyen-Viet, B. (2024). How does gamification affect learning effectiveness? The mediating roles of engagement, satisfaction, and intrinsic motivation. _Interactive Learning Environments_ , 33(3), 2635–2653. https://doi.org/10.1080/10494820.2024.2414356 

Pan, Z., Biegley, L., Taylor, A., and Zheng, H. (2024). A Systematic Review of Learning Analytics: Incorporated Instructional Interventions on Learning Management Systems. _Journal of Learning Analytics_ , 11(2), 52–72. https://doi.org/10.18608/jla.2023.8093 

Sharma, S. (2025). The Impact of Microservices Architecture on System Scalability. _American Scientific Research Journal for Engineering, Technology, and Sciences_ , 102(1), 140–148. https://asrjetsjournal.org/American_Scientific_Journal/article/view/11677 

Thallapally, N. (2024). Microservices architecture in cloud-native applications: Design patterns and scalability. _International Journal of Science and Research Archive_ , 13(02), 4140–4145. 

Zeng, X. (2024). Exploring the impact of gamification on students' academic performance: A comprehensive meta-analysis of studies from the year 2008 to 2023. _British Journal of Educational Technology_ , 55(4), 1471–1492. https://doi.org/10.1111/bjet.13471 

50 

## **Appendix A: Client Agreement Letter** 

_Figure 35: Client Agreement Letter - Page 01_ 

51 

_Figure 36: Client Agreement Letter - Page 02_ 

52 

_Figure 37: Client Agreement Letter - Page 03_ 

53 

**Appendix B: Software Requirements Specification** 

**EDURA - Learning Management System** 

**Software Requirements Specification (SRS)** 

**By** 

## **W.G.N.DANANJAYA** 

**SE/2021/047 R.W.V.I.D.RAJAPAKSHA SE/2021/029 P.D.D.RANSIKA SE/2021/034 H.T.MADUSHANKA SE/2021/011** 

**A report submitted in partial fulfillment of the requirements for the degree of Bachelor of Science Honors in Software Engineering (B.Sc. SE)** 

**Software Engineering Teaching Unit** 

**Faculty of Science University of Kelaniya** 

**Sri Lanka** 

**2026** 

54 

## **VERSION HISTORY** 

|**Version**|**Date**|**Author(s)**|**Changes**|
|---|---|---|---|
|1.0|18/03/2026|Nadun Dananjaya,<br>Imansha Dilshan,<br>Danidu Ransika,<br>Thushan Madhusanka|<br>Initial SRS<br>document creation|



i 

## **TABLE OF CONTENTS** 

## CHAPTER 1 

INTRODUCTION .............................................................................................. 1 1.1 Project Background.................................................................................... 1 1.2 System Overview ...................................................................................... 1 CHAPTER 2 ......................................................................................................... 3 PURPOSE ........................................................................................................ 3 2.1 Document Purpose ..................................................................................... 3 2.2 Intended Audience ..................................................................................... 3 CHAPTER 3 ......................................................................................................... 4 SCOPE ............................................................................................................. 4 3.1 System Name ............................................................................................ 4 3.2 System Capabilities.................................................................................... 4 3.3 Explicit Exclusions .................................................................................... 5 CHAPTER 4 ......................................................................................................... 6 DEFINITIONS, ACRONYMS AND ABBREVIATIONS ......................................... 6 CHAPTER 5 ......................................................................................................... 7 DOCUMENT OVERVIEW ................................................................................. 7 CHAPTER 6 ......................................................................................................... 8 PROJECT SCOPE.............................................................................................. 8 6.1 Business Objectives ................................................................................... 8 6.2 Project Deliverables ................................................................................... 8 6.3 Development Boundaries and Responsibilities ............................................... 8 CHAPTER 7 ....................................................................................................... 10 STAKEHOLDERS ........................................................................................... 10 7.1 Client and System Owner ......................................................................... 10 7.2 End Users ............................................................................................... 10 7.3 Development Team .................................................................................. 10 7.4 Academic Evaluators ................................................................................ 11 CHAPTER 8 ....................................................................................................... 12 FUNCTIONAL REQUIREMENTS .................................................................... 12 

ii 

CHAPTER 9 ....................................................................................................... 15 NON-FUNCTIONAL REQUIREMENTS ............................................................ 15 CHAPTER 10 ..................................................................................................... 19 BUSINESS RULES .......................................................................................... 19 CHAPTER 11 ..................................................................................................... 21 CONSTRAINTS .............................................................................................. 21 11.1 Technical Constraints .............................................................................. 21 11.2 Operational Constraints ........................................................................... 22 11.3 Time and Resource Constraints ................................................................ 22 ASSUMPTIONS .............................................................................................. 24 12.1 User Capabilities and Access ................................................................... 24 12.2 External Systems and Dependencies ......................................................... 24 12.3 Operational and Business Assumptions ..................................................... 25 CHAPTER 13 ..................................................................................................... 26 USE CASE DIAGRAMS .................................................................................. 26 13.1 System Actors ....................................................................................... 26 13.2 Student Subsystem Use Case Diagram ...................................................... 26 13.3 Teacher Subsystem Use Case Diagram ...................................................... 27 13.4 Administrator Subsystem Use Case Diagram .............................................. 28 CHAPTER 14 ..................................................................................................... 30 USE CASE DESCRIPTIONS ............................................................................ 30 14.1 UC-001: User Authentication and Login .................................................... 30 14.2 UC-002: Upload Subscription Receipt....................................................... 31 14.3 UC-003: Create Educational Module ........................................................ 32 14.4 UC-004: Attempt Timed Assessment ......................................................... 33 14.5 UC-005: Automated Subscription Payment via PayHere .............................. 34 CHAPTER 15 ..................................................................................................... 37 ACTIVITY DIAGRAMS .................................................................................. 37 15.1 User Authentication and Verification Flow ................................................. 37 15.2 Lesson and Content Management Flow ..................................................... 38 15.3 Assessment and Auto-Grading Flow ......................................................... 39 15.4 Subscription Payment Verification Flow .................................................... 40 

iii 

CHAPTER 16 ..................................................................................................... 42 EXTERNAL INTERFACE REQUIREMENTS .................................................... 42 16.1 User Interfaces ...................................................................................... 42 16.2 Hardware Interfaces ............................................................................... 42 16.3 Software Interfaces ................................................................................ 43 16.4 Communication Interfaces ....................................................................... 44 CHAPTER 17 ..................................................................................................... 46 DATA REQUIREMENTS ................................................................................. 46 17.1 Logical Data Entities .............................................................................. 46 17.2 Data Storage Mechanisms ....................................................................... 47 17.3 Data Security and Integrity ...................................................................... 47 17.4 Data Retention and Backup ..................................................................... 48 CHAPTER 18 ..................................................................................................... 49 ALTERNATIVE SOLUTIONS CONSIDERED .................................................... 49 18.1 Architectural Approach: Monolithic vs. Decoupled RESTful API .................. 49 18.2 Platform Delivery: Native Mobile Application vs. Responsive Web Application .................................................................................................................. 50 18.3 Payment Processing: Automated Gateway vs. Manual Verification vs. Hybrid Approach ..................................................................................................... 50 18.4 Content Delivery: Local Server Storage vs. Third-Party Media Platforms ....... 50 CHAPTER 19 ..................................................................................................... 52 FEASIBILITY STUDY..................................................................................... 52 19.1 Technical Feasibility ............................................................................... 52 19.2 Economic Feasibility .............................................................................. 53 19.3 Operational Feasibility ............................................................................ 53 19.4 Schedule Feasibility ............................................................................... 54 CHAPTER 20 ..................................................................................................... 55 RISK ANALYSIS ............................................................................................ 55 20.1 Identified Risks and Mitigation Strategies .................................................. 55 20.2 Continuous Risk Monitoring .................................................................... 57 CHAPTER 21 ..................................................................................................... 58 REFERENCES ................................................................................................ 58 

iv 

CLIENT REQUIREMENT SIGN-OFF ................................................................... 61 

v 

## **LIST OF TABLES** 

Table 1:Definitions, Acronyms and Abbreviations ................................................................ 6 Table 2: Functional Requirements ....................................................................................... 12 Table 3: Non-Functional Requirements ............................................................................... 15 Table 4: UC-001 – User Authentication and Login ............................................................. 30 Table 5: UC-002 – Upload Subscription Receipt ................................................................ 31 Table 6: UC-003 – Create Educational Module .................................................................. 32 Table 7: UC-004 – Attempt Timed Assessment ................................................................... 33 Table 8: UC-005 – Automated Subscription Payment via PayHere .................................... 34 Table 9: Risk Analysis and Mitigation Strategies ................................................................ 55 

vi 

## **LIST OF FIGURES** 

Figure 1: Student Subsystem Use Case Diagram ................................................................ 27 Figure 2: Teacher Subsystem Use Case Diagram ................................................................ 28 Figure 3: Administrator Subsystem Use Case Diagram ...................................................... 29 Figure 4: User Authentication and Verification Activity Diagram ...................................... 38 Figure 5: Lesson and Content Management Activity Diagram ........................................... 39 Figure 6: Assessment and Auto-Grading Activity Diagram ................................................ 40 Figure 7: Subscription Payment Verification Activity Diagram .......................................... 41 

vii 

## **CHAPTER 1** 

## **INTRODUCTION** 

## **1.1 Project Background** 

The transition of quality education toward online platforms has been increasingly observed; however, traditional learning environments remain frequently constrained by limited resources and difficulties in continuous progress tracking. Within the operational context of the ICT - Dimuthu educational institute, it has been identified that the majority of administrative and educational tasks are executed manually. Consequently, this manual execution leads to operational delays and procedural errors. Furthermore, the evaluation of student performance is recognized as a time-consuming and inconsistent process under the current framework. 

The preparation of individual student progress reports presents significant administrative difficulties for educators. The absence of a centralized platform for managing lessons, quizzes, and student data results in limited tracking and monitoring capabilities. The mitigation of such administrative burdens and error costs through the adoption of new learning technologies, as opposed to traditional manual tracking methods, has been strongly supported by recent educational research [1][2]. Studies have demonstrated that LMS platforms can significantly reduce administrative workload while improving the consistency and accuracy of educational assessments and progress tracking [3]. Therefore, the necessity for a comprehensive digital solution was established to overcome these operational bottlenecks and optimize the institute's educational delivery. 

## **1.2 System Overview** 

To address the aforementioned limitations, the EDURA Learning Management System is proposed as a comprehensive educational platform. The system is specifically designed to enable educators, students, and administrators to efficiently manage courses, digital lessons, and interactive assessments. Through the implementation of this centralized platform, the educational process is transformed to be highly flexible, engaging, and measurable. 

Role-based access control is utilized to ensure secure interaction across different user categories (Admin, Teacher, and Student). Furthermore, core functionalities such as structured lesson management with video integration, automated quiz grading, and comprehensive progress tracking are incorporated into the system architecture. The capability of Learning Management Systems to utilize data from student interactions for 

1 

early interventions and improved learning outcomes has been highlighted as a critical advantage in recent academic studies [4][5]. 

In alignment with these findings, the learning experience within EDURA is further enhanced by interactive gamification elements, including point systems and leaderboards. Finally, measurable outcomes are provided to all stakeholders through the generation of exportable analytical reports and the automated issuance of digital certificates upon successful course completion. 

2 

## **CHAPTER 2** 

## **PURPOSE** 

## **2.1 Document Purpose** 

A comprehensive description of the EDURA Learning Management System is provided by this Software Requirement Specification (SRS) document. The functional and nonfunctional requirements, system constraints, and design specifications necessary for the successful development and deployment of the EDURA platform are explicitly outlined herein. Furthermore, the contractual basis for the project is established by this document, ensuring that a clear and mutual understanding of system capabilities, limitations, and expectations is maintained by all involved parties. 

## **2.2 Intended Audience** 

This document is intended to be utilized by various project stakeholders to guide the development, testing, and validation processes. Specifically, the SRS is directed toward the development team (Team ZYNAPTRIX), the primary client (Mr. Dimuthu Prabath), other relevant project stakeholders, and system administrators. It is intended that the document will be used by the development team as a foundational blueprint for system engineering, while it will be referenced by the client and administrators to verify that the delivered system aligns comprehensively with the agreed-upon requirements. 

3 

## **CHAPTER 3** 

## **SCOPE** 

## **3.1 System Name** 

The system is officially designated as EDURA - Learning Management System. 

## **3.2 System Capabilities** 

EDURA is defined as a comprehensive web-based learning management system that is specifically tailored for the "ICT - Dimuthu" educational institute to facilitate online education for Advanced Level (A/L) students aged 15-18 years. The creation, management, and delivery of digital courses, assessments, and learning materials by educators will be enabled by the system. Furthermore, an engaging, interactive learning experience that is enhanced by gamification elements will be provided to the students. 

The specific functionalities to be executed by the system are outlined as follows: 

- Role-based access control will be provided for administrators, teachers (content creators/editors), and students. 

- Comprehensive course and lesson management will be enabled, incorporating video content, supplementary notes, and organized learning modules, utilizing MongoDB for flexible data storage and Redis for high-performance caching. 

- Multiple assessment types, including multiple-choice questions, true/false, and short answer formats, will be supported alongside automatic grading capabilities. 

- Student progress, encompassing video viewing completion, quiz performance, and overall course advancement, will be continuously tracked. 

- Detailed analytics and progress reports for individual students and entire classes will be generated and made exportable in PDF and Excel formats. 

- Secure authentication, paired with email verification and strict anti-cheating mechanisms for assessments, will be implemented. 

- Gamification features will be incorporated through the use of performance-based leaderboards, points systems, and achievement badges. Research has demonstrated 

4 

that such gamification elements significantly enhance student engagement, motivation, and academic performance in online learning environments [6][7][8]. 

- Digital certificates will be automatically issued upon the successful completion of a course. 

- Platform navigation and learning support will be provided through an AI-powered assistant utilizing Google Gemini AI. 

- Monthly subscription-based payment processing will be facilitated through a hybrid approach; automated, real-time subscription activations will be securely processed via the PayHere payment gateway, while manual receipt uploads paired with administrative verification will be maintained as a secondary fallback option. 

## **3.3 Explicit Exclusions** 

The boundaries of the project are defined by the following explicit exclusions: 

- Social login or single sign-on (SSO) integration is not supported within the initial release. 

- Live video streaming and real-time virtual classroom functionalities are not included. 

- Integration with external learning management systems or third-party educational platforms is not supported. 

- Mobile native applications (iOS/Android) are not part of the initial scope; the system will be strictly restricted to a web-responsive application. 

- Advanced AI features, such as automated content generation or personalized learning path recommendations, are excluded from this release and reserved for future development phases. 

5 

## **CHAPTER 4** 

## **DEFINITIONS, ACRONYMS AND ABBREVIATIONS** 

All domain-specific terms, acronyms, and abbreviations utilized throughout this Software Requirement Specification document are defined in the following table to ensure clarity and a mutual understanding among all stakeholders. 

_Table 9:Definitions, Acronyms and Abbreviations_ 

|**Term /**<br>**Acronym**|**Definition**|
|---|---|
|**AI**|Artificial Intelligence - Technology by which human intelligence is<br>simulated by machines.|
|**API**|Application Programming Interface - A set of protocols and tools utilized<br>for the building of software applications.|
|**CDN**|Content Delivery Network - A geographically distributed network of<br>servers employed to deliver content efficiently.|
|**LMS**|Learning Management System - A software application utilized for the<br>administration, documentation, tracking, reporting, and delivery of<br>educational courses or training programs.|
|**MCQ**|Multiple Choice Question - A specific format of assessment utilized within<br>the platform.|
|**OTP**|One-Time Password - A password that is generated to be valid for only a<br>single login session or transaction.|
|**REST**|Representational State Transfer - An architectural style utilized for the<br>design of networked applications.|
|**SLA**|Service Level Agreement - A formalized commitment established between<br>a service provider and a client by which the expected level of service is<br>defined.|
|**SRS**|Software Requirement Specification - The primary documentation artifact<br>utilized to detail system requirements.|
|**UI**|User Interface - The visual elements through which the system is interacted<br>with by users.|
|**UX**|User Experience - The overall experience of an individual by whom the<br>system is used.|



6 

## **CHAPTER 5** 

## **DOCUMENT OVERVIEW** 

How the remainder of this Software Requirement Specification document is organized is outlined in this section. Following the initial introductory and definitional sections (Sections 1 through 5), the structural layout of the document is established as follows: 

- The overall project scope and all relevant stakeholders are detailed in Sections 6 and 7, respectively. 

- The core capabilities and quality attributes of the system are comprehensively documented as functional and non-functional requirements in Sections 8 and 9. 

- The business rules, system constraints, and underlying assumptions by which the system behavior and development process are governed are defined in Sections 10, 11, and 12. 

- System functionalities and user interactions are visually and textually illustrated through use case diagrams, detailed use case descriptions, and activity diagrams, which are provided in Sections 13, 14, and 15. 

- The external interface expectations, including user, hardware, software, and communication interfaces, are specified in Section 16. 

- Data requirements and database specifications are detailed in Section 17. 

- Alternative solutions that were evaluated and the justification for the chosen approach are discussed in Section 18. 

- A comprehensive feasibility study, encompassing technical, economic, operational, and schedule aspects, is presented in Section 19. 

- Potential project risks and their corresponding mitigation strategies are analyzed in Section 20. 

- Finally, the external documents, standards, and sources cited throughout the document are listed in Section 21, which is subsequently followed by the formal client and project supervisor sign-off pages. 

7 

## **CHAPTER 6** 

## **PROJECT SCOPE** 

## **6.1 Business Objectives** 

The primary objective of the EDURA project is to establish the comprehensive digitalization of the educational processes currently utilized by the "ICT - Dimuthu" institute. The manual administrative and grading workloads currently experienced by the institute's teaching staff are intended to be significantly reduced through this transition. Furthermore, the accessibility and engagement of Advanced Level (A/L) ICT educational resources are to be enhanced for students through a centralized, highly available web-based platform. 

## **6.2 Project Deliverables** 

The successful execution and delivery of a fully functional web-based Learning Management System is encompassed within the boundaries of this project. The specific artifacts and components to be delivered to the client by the development team (Team ZYNAPTRIX) are formally defined as follows: 

- This comprehensive Software Requirement Specification (SRS) document is used to finalize the system requirements. 

- The complete compiled source code of the EDURA web application. 

- A fully designed and configured database architecture utilized for the secure management of user profiles, course content, and assessment records. 

- System documentation, including administrative and user manuals, by which the operation of the platform is guided. 

- The initial deployment and configuration of the system within a production environment. 

## **6.3 Development Boundaries and Responsibilities** 

The development phase of the project is strictly constrained to the design, implementation, and deployment of the software functionalities explicitly detailed within this SRS document. The procurement or provision of physical hardware, network infrastructure, or end-user devices (such as computers or internet connections for the students) is not encompassed by the responsibilities of the project team. 

8 

Furthermore, the creation, curation, and uploading of the actual educational content (including video lectures, quiz questions, and study notes) are designated as the sole responsibility of the client (Mr. Dimuthu Prabath) and the appointed teaching staff. Only the digital platform through which this content is hosted, managed, and delivered will be provided by the development team. Finally, the entire project lifecycle, from requirement elicitation to final deployment, is required to be completed within the academic timeline and evaluation schedule specified by the Software Engineering Teaching Unit of the University of Kelaniya. 

9 

## **CHAPTER 7** 

## **STAKEHOLDERS** 

Various individuals, groups, and entities with whom the EDURA Learning Management System interacts, is interacted with, impacted by, or developed for, are identified and categorized within this section. The specific roles and responsibilities of each stakeholder group are defined as follows: 

## **7.1 Client and System Owner** 

The role of the primary client and system owner is held by Mr. Dimuthu Prabath, the owner and principal lecturer of the "ICT - Dimuthu" educational institute. The overall business requirements, educational content, and final approval of the delivered system are provided by the client. The administrative and strategic oversight of the deployed platform will ultimately be maintained by this stakeholder. 

## **7.2 End Users** 

The system is expected to be utilized directly by three primary categories of end-users: 

- **Students:** The platform is intended to be accessed by Advanced Level (A/L) ICT students, primarily aged between 15 and 18 years. System features such as video lectures, quizzes, progress tracking, and gamified leaderboards will be engaged with by these users to achieve their educational objectives. 

- **Teachers / Content Creators:** The creation, uploading, and management of educational materials (such as video modules and multiple-choice questions) are executed by the teaching staff. The progress of the students and the outcomes of automated and manual assessments will also be monitored by these users. 

- **System Administrators:** The routine operational aspects of the platform are overseen by administrative staff. Platform configuration, user account management, and the manual verification of subscription payment receipts are handled by this user group. 

## **7.3 Development Team** 

The architectural design, software development, quality assurance, and initial deployment of the system are designated as the explicit responsibilities of Team ZYNAPTRIX. The project requirements and technical deliverables outlined within this document are required 

10 

to be fulfilled by the team members (Nadun Dananjaya, Imansha Dilshan, Danindu Ransika, and Thushan Madhusanka). 

## **7.4 Academic Evaluators** 

The academic oversight and final evaluation of the project are conducted by the Software Engineering Teaching Unit of the University of Kelaniya. The adherence of the project to formal software engineering standards, as well as the evaluation of the final system against academic grading criteria, is assessed by the appointed project supervisors and evaluation committees. 

11 

## **CHAPTER 8** 

## **FUNCTIONAL REQUIREMENTS** 

The specific behaviors, computations, and informational processing functions that are required to be performed by the EDURA Learning Management System are defined in this section. Each functional requirement has been assigned a unique identifier, categorized by priority (High, Medium, or Low), and traced back to its source stakeholder. All requirements are currently classified under a "Proposed" status for the initial development lifecycle. 

_Table 10: Functional Requirements_ 

|**ID**|**Description**|**Priority**|**Source**|**Status**|
|---|---|---|---|---|
|**FR-001**|Secure user authentication and authorization,<br>utilizing role-based access control for<br>Administrators, Teachers, and Students, shall<br>be enforced by the system.|High|Client|Proposed|
|**FR-002**|User registration and password recovery<br>processes shall be validated through the<br>implementation<br>of<br>email<br>verification<br>mechanisms (e.g., OTP).|High|Client|Proposed|
|**FR-003**|The creation, structuring, and modification of<br>lessons, including the embedding of private<br>YouTube video links, the integration of<br>Cloudinary media assets, and the uploading<br>of supplementary notes, shall be facilitated<br>for Teachers and Administrators.|High|Teachers|Proposed|
|**FR-004**|The creation and configuration of interactive<br>assessments,<br>specifically<br>encompassing<br>Multiple-Choice<br>Questions<br>(MCQ),<br>True/False formats, and short answer queries,<br>shall be enabled.|High|Teachers|Proposed|
|**FR-005**|Submitted quizzes and objective assessments<br>shall be automatically graded by the system<br>immediately upon completion.|High|Client|Proposed|



12 

|**FR-006**|As a fallback payment method, the uploading<br>of manual payment receipts by students shall<br>be facilitated, which shall subsequently be<br>verified<br>and<br>approved<br>by<br>system<br>administrators.|High|System<br>Admin|Proposed|
|---|---|---|---|---|
|**FR-007**|For automated subscription processing, users<br>shall be securely redirected to the PayHere<br>checkout gateway by the system.|High|Client|Proposed|
|**FR-008**|Payment status webhooks and server-to-<br>server callbacks dispatched by the PayHere<br>gateway<br>shall<br>be<br>securely<br>received,<br>authenticated, and processed by the system.|High|System<br>Admin|Proposed|
|**FR-009**|Course access shall be automatically granted<br>to the student by the system immediately<br>upon receipt of a "Success" payment status<br>from the payment gateway, without requiring<br>manual administrative intervention.|High|Students|Proposed|
|**FR-010**|Student progress, specifically measured by<br>the percentage of videos watched, quiz scores<br>achieved, and overall course completion<br>status, shall be continuously tracked and<br>recorded.|High|Client|Proposed|
|**FR-011**|Platform navigation and contextual learning<br>support must be provided to users through the<br>integration of a Google Gemini AI-powered<br>digital assistant.|High|Client|Proposed|
|**FR-012**|Comprehensive analytics and performance<br>reports for both individual students and entire<br>classes should be generated and made<br>exportable in PDF and Excel formats.|Medium|Teachers|Proposed|
|**FR-013**|Anti-cheating<br>measures<br>(e.g.,<br>browser<br>lockdown, tab-switching detection) shall be|Medium|Client|Proposed|



13 

||implemented during timed assessments to<br>ensure academic integrity.||||
|---|---|---|---|---|
|**FR-014**|Student engagement shall be stimulated<br>through the integration of gamification<br>elements, including the awarding of points,<br>achievement badges, and the display of<br>performance-based leaderboards.|Medium|Students<br>/ Client|Proposed|
|**FR-015**|Digital certificates of completion shall be<br>automatically generated and issued to<br>students upon the successful fulfillment of all<br>course requirements.|Medium|Students|Proposed|



Recent studies have validated the effectiveness of automated cheating detection systems in online assessments. Machine learning and deep learning approaches, including LSTM networks and computer vision techniques, have achieved detection accuracies exceeding 90% in identifying suspicious behaviors during virtual examinations [9][10][11]. The implementation of browser lockdown mechanisms and behavioral monitoring has been shown to reduce cheating incidents significantly while maintaining assessment validity [12]. 

14 

## **CHAPTER 9** 

## **NON-FUNCTIONAL REQUIREMENTS** 

The qualitative attributes, performance metrics, and technical constraints by which the EDURA Learning Management System is strictly governed are outlined in this section. To ensure a high standard of software quality, each requirement has been categorized in alignment with the ISO/IEC 25010 software quality assurance framework. Furthermore, measurable acceptance criteria have been assigned to each non-functional requirement to facilitate precise system evaluation and testing. 

_Table 11: Non-Functional Requirements_ 

|**ID**|**Category**|**Description**|**Measurable Metric /**<br>**Acceptance Criteria**|**Priority**|
|---|---|---|---|---|
|**NFR-**<br>**001**|**Performance**|The system response<br>time for standard page<br>loads<br>and<br>query<br>executions<br>shall<br>be<br>minimized to ensure a<br>seamless<br>user<br>experience.|95% of standard user<br>interface interactions<br>shall be processed and<br>rendered in under 2.0<br>seconds under normal<br>server load.|High|
|**NFR-**<br>**002**|**Reliability**|A continuous and stable<br>operational state shall be<br>maintained<br>by<br>the<br>system, ensuring that<br>educational<br>resources<br>remain<br>accessible<br>to<br>students.|A minimum system<br>uptime<br>of<br>99.9%<br>(excluding scheduled<br>maintenance<br>windows)<br>shall<br>be<br>maintained<br>consistently<br>on<br>a<br>monthly basis.|High|
|**NFR-**<br>**003**|**Reliability**|Automated<br>data<br>preservation<br>mechanisms<br>shall<br>be<br>implemented to prevent<br>the<br>loss<br>of<br>critical|Full database backups<br>shall be automatically<br>executed<br>every<br>24<br>hours.|High|



15 

|||educational content and<br>student records.|||
|---|---|---|---|---|
|**NFR-**<br>**004**|**Reliability**|Robust<br>fault-tolerance<br>mechanisms<br>shall<br>be<br>implemented to manage<br>connection timeouts or<br>failed<br>webhook<br>deliveries<br>from<br>the<br>external PayHere API,<br>ensuring that payment<br>statuses are accurately<br>reconciled.|100% of missed or<br>failed<br>payment<br>webhooks<br>shall<br>be<br>detected by the system<br>and queued for an<br>automated<br>status<br>reconciliation polling<br>process<br>within<br>15<br>minutes of the initial<br>transaction timeout.|High|
|**NFR-**<br>**005**|**Usability**|The user interface shall<br>be designed to be fully<br>responsive,<br>ensuring<br>optimal readability and<br>interaction across a wide<br>variety of devices.|The<br>platform<br>shall<br>seamlessly adapt to<br>desktop, tablet, and<br>mobile device screen<br>resolutions<br>without<br>horizontal scrolling or<br>broken UI elements.|High|
|**NFR-**<br>**006**|**Security**|Sensitive<br>user<br>credentials, specifically<br>passwords,<br>shall<br>be<br>cryptographically<br>secured prior to database<br>storage.|100%<br>of<br>user<br>passwords<br>shall be<br>encrypted utilizing the<br>bcrypt<br>hashing<br>algorithm; plain text<br>storage shall be strictly<br>prohibited.|High|
|**NFR-**<br>**007**|**Security**|Authentication<br>verification<br>requests<br>shall be strictly time-<br>bound to mitigate the<br>risk<br>of<br>unauthorized<br>account access.|One-Time Passwords<br>(OTPs) generated for<br>email<br>verification<br>shall be configured to<br>expire<br>exactly<br>5<br>minutes after issuance.|High|



16 

|**NFR-**<br>**008**|**Security**|The storage of sensitive<br>financial<br>data,<br>specifically<br>credit<br>or<br>debit<br>card<br>numbers,<br>upon<br>the<br>EDURA<br>servers shall be strictly<br>prohibited;<br>all<br>automated<br>payment<br>processing<br>shall<br>be<br>delegated to and strictly<br>governed by the security<br>protocols of the PayHere<br>gateway.|0% of primary account<br>numbers<br>(PAN)<br>or<br>CVV codes shall be<br>transmitted<br>to<br>or<br>stored<br>within<br>the<br>EDURA<br>database<br>infrastructure.|High|
|---|---|---|---|---|
|**NFR-**<br>**009**|**Scalability**|The server architecture<br>and<br>database<br>connections<br>shall<br>be<br>engineered<br>to<br>accommodate<br>high<br>volumes of simultaneous<br>student<br>access,<br>particularly<br>during<br>assessment periods.|The system shall be<br>capable of supporting<br>a minimum of 500<br>concurrent<br>user<br>sessions<br>without<br>experiencing<br>a<br>performance<br>degradation exceeding<br>20%.|Medium|
|**NFR-**<br>**010**|**Maintainability**|The<br>backend<br>architecture<br>shall<br>be<br>structured<br>in<br>a<br>systematic<br>and<br>decoupled manner to<br>facilitate future updates<br>and<br>collaborative<br>development.|The system shall be<br>organized utilizing a<br>modular REST API<br>architecture,<br>with<br>100%<br>of<br>API<br>endpoints<br>systematically<br>documented.|Medium|
|**NFR-**<br>**011**|**Maintainability**|The system shall be<br>developed<br>using<br>industry-standard|The frontend shall be<br>built<br>using<br>Next.js<br>framework,<br>backend|High|



17 

|||frameworks<br>and<br>languages<br>to<br>ensure<br>long-term<br>maintainability<br>and<br>developer accessibility.|services<br>shall<br>be<br>implemented<br>in<br>Python, and all code<br>shall follow PEP 8<br>(Python) and ESLint<br>(JavaScript)<br>style<br>guidelines.||
|---|---|---|---|---|
|**NFR-**<br>**012**|**Portability**|Platform<br>accessibility<br>across diverse operating<br>environments shall be<br>ensured by adhering to<br>modern web standards.|Full<br>system<br>compatibility<br>and<br>uniform functionality<br>shall be verified across<br>the<br>latest<br>stable<br>versions of Google<br>Chrome,<br>Mozilla<br>Firefox, Apple Safari,<br>and Microsoft Edge.|Medium|



18 

## **CHAPTER 10** 

## **BUSINESS RULES** 

The fundamental operational policies, academic constraints, and access regulations by which the EDURA Learning Management System is governed are defined in this section. These rules must be strictly enforced by the system logic to ensure the integrity of the educational process and the financial operations of the institute. 

- **BR-001 (Subscription Access):** Access to course materials and assessments shall be strictly granted to students under one of two conditions: either immediately and automatically upon the system's receipt of a successful transaction callback from the PayHere payment gateway, or upon the successful manual verification of an uploaded payment receipt by system administrators. If a subscription lapses without renewal via either authorized method, access to new course materials must be automatically suspended by the system. 

- **BR-002 (Assessment Grading):** Automated grading mechanisms shall only be applied to objective assessment formats, specifically Multiple-Choice Questions (MCQ) and True/False questions. Any subjective assessments must be flagged for manual review by the teaching staff. 

- **BR-003 (Timed Examinations):** Timed quizzes and assessments must be completed within a single, continuous session. Upon the expiration of the allocated time limit, the ongoing assessment shall be automatically submitted by the system, regardless of completion status. 

- **BR-004 (Certification Eligibility):** Digital certificates of completion shall only be issued to students upon the verified completion of all mandatory video modules (reaching 100% watch status) and the achievement of a predefined minimum passing score in all required course assessments. 

- **BR-005 (Account Integrity):** One-Time Passwords (OTPs) generated for the purposes of account registration, email verification, or password recovery shall be rendered permanently invalid exactly five minutes after their initial generation. 

- **BR-006 (Anti-Cheating Enforcement):** During the execution of timed, formal assessments, browser lockdown or tab-switching detection mechanisms must be enforced. Any detected violations shall be automatically recorded and reported to the 

19 

system administrators and relevant teaching staff. The global online exam proctoring market, valued at $836.43 million in 2023 and projected to reach $1.99 billion by 2029, reflects the widespread adoption of automated integrity monitoring systems in educational institutions worldwide [13]. 

20 

## **CHAPTER 11** 

## **CONSTRAINTS** 

The technical, operational, and environmental limitations by which the development, deployment, and ongoing operation of the EDURA Learning Management System are restricted are outlined in this section. These constraints must be strictly adhered to by the development team throughout the project lifecycle. 

## **11.1 Technical Constraints** 

- **Platform Limitation:** The system is strictly constrained to a web-based architecture. The development of native mobile applications (iOS or Android) is explicitly excluded from the current project scope. 

- **Connectivity Dependence:** Continuous and stable internet connectivity is required by all end-users (students, teachers, and administrators) to access the platform, view lessons, and submit assessments. Offline capabilities are not supported. 

- **Browser Compatibility:** System compatibility is restricted to modern web browsers. Full functionality must be ensured only on the latest stable releases of Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge. 

- **Technology Stack Constraints:** The system frontend is constrained to the Next.js framework for React-based development. Backend microservices must be implemented exclusively in Python to maintain consistency across service boundaries. 

- **Database Architecture:** The system is restricted to a NoSQL database architecture utilizing MongoDB for primary data persistence and Redis for session management and high-speed caching. Traditional relational database systems (MySQL, PostgreSQL) are explicitly excluded from this implementation. 

- **Cloud Platform Dependency:** System deployment and hosting are strictly constrained to the Microsoft Azure cloud platform. Migration to alternative cloud providers (AWS, Google Cloud) would require significant architectural modifications. 

21 

- **Media Handling:** The platform is restricted to handling pre-recorded video uploads. Real-time virtual classrooms and live video streaming functionalities are not supported by the system architecture. 

- **Authentication Limitations:** Social media login integration and Single Sign-On (SSO) mechanisms are not supported; authentication is strictly limited to the system's internal email and password verification process. 

- **Infrastructure Complexity:** The deployment environment is constrained by the necessity for containerization (e.g., Docker) and potentially orchestration (e.g., Kubernetes). A more complex cloud hosting infrastructure is required to manage, network, and monitor multiple independent services compared to a traditional monolithic application. 

## **11.2 Operational Constraints** 

- **Manual Payment Processing:** The activation of student subscriptions is constrained by a manual verification process. Because external payment gateways are not integrated, receipt uploads must be visually verified and manually approved by system administrators before course access is granted. 

- **Content Storage:** The capacity for video and lesson storage is inherently limited by the hosting and database infrastructure allocated during the deployment phase. Extensive scaling may require manual infrastructure upgrades by the client. 

- **Third-Party Media Dependency:** The system's video delivery capabilities are strictly constrained by the terms of service, API rate limits, and bandwidth allocations imposed by YouTube and Cloudinary. Any policy changes or service degradations on these external platforms will directly impact the EDURA system. 

## **11.3 Time and Resource Constraints** 

- **Academic Schedule:** The entire software development lifecycle, encompassing requirement gathering, design, implementation, testing, and deployment, is strictly bounded by the academic timeline mandated by the Software Engineering Teaching Unit of the University of Kelaniya. 

- **Team Capacity:** All system engineering and development tasks must be exclusively executed by the four assigned members of Team ZYNAPTRIX. Third-party development outsourcing is strictly prohibited. 

22 

- **Content Creation:** The generation and formatting of all educational materials (videos, notes, and quizzes) are strictly designated as the responsibility of the client; content creation is not accommodated within the development timeline. 

23 

## **CHAPTER 12** 

## **ASSUMPTIONS** 

The fundamental assumptions regarding the operational environment, user capabilities, and external technological dependencies upon which the successful deployment and operation of the EDURA Learning Management System rely are detailed in this section. If any of these foundational assumptions are proven to be incorrect, the project timeline, scope, or system functionality may be significantly impacted. 

## **12.1 User Capabilities and Access** 

- **Digital Literacy:** It is assumed that a foundational level of computer literacy is possessed by all target users, including students, teaching staff, and administrators, enabling them to navigate standard web-based applications. 

- **Device and Network Availability:** It is assumed that reliable access to personal computers, laptops, or suitable mobile devices, accompanied by a stable broadband internet connection, is consistently maintained by the students and staff. 

## **12.2 External Systems and Dependencies** 

- **Third-Party Service Uptime:** It is assumed that the external services integrated into the platform, specifically the Google Gemini AI API utilized for the digital assistant and the SMTP infrastructure employed for automated email verification, will remain consistently operational and highly available. 

- **Browser Usage:** It is assumed that modern, updated web browsers (such as Google Chrome, Mozilla Firefox, or Microsoft Edge) are utilized by the end-users to access the platform, as backward compatibility with deprecated browsers (e.g., Internet Explorer) is not accommodated. 

- **Hosting Environment:** It is assumed that an adequate cloud hosting environment and database infrastructure will be provisioned by the client to support the storage requirements of the uploaded video lectures and educational content. 

- **Cloud Platform Infrastructure:** It is assumed that Microsoft Azure will provide reliable cloud infrastructure services, including compute resources, networking, and storage capabilities necessary for containerized microservice deployment. It is 

24 

further assumed that Azure's service-level agreements (SLAs) will meet the system's uptime and performance requirements. 

- **Payment Gateway Uptime:** It is assumed that high availability and consistent operational uptime will be maintained by the external PayHere API to ensure the uninterrupted processing of automated student subscription payments. 

- **Media Platform Uptime:** It is assumed that high availability and uninterrupted streaming services will be consistently maintained by YouTube and Cloudinary. 

## **12.3 Operational and Business Assumptions** 

- **Content Provisioning:** It is assumed that all necessary educational materials, including recorded video lectures, structured notes, and formatted quiz questions, will be completely prepared and supplied by the client (Mr. Dimuthu Prabath) prior to the system's final deployment phase. 

- **Administrative Responsiveness:** Because subscription activations are reliant on manual verification, it is assumed that uploaded payment receipts will be reviewed and processed by the system administrators in a timely manner to ensure that student access is not unreasonably delayed. 

- **Academic Integrity:** While anti-cheating mechanisms are implemented within the system, it is assumed that a general standard of academic honesty is maintained by the students during unsupervised online assessments. 

- **Client Account Provisioning Readiness:** It is assumed that all necessary third-party administrative and financial accounts, specifically, a verified PayHere merchant account, a dedicated private YouTube channel, and a configured Cloudinary environment, will be fully provisioned and possessed by the client (Mr. Dimuthu Prabath) prior to the system's final deployment phase. Furthermore, it is assumed that the embedding of private videos strictly complies with YouTube's prevailing terms of service for educational platforms. 

25 

## **CHAPTER 13** 

## **USE CASE DIAGRAMS** 

The functional requirements and the interactions between the external actors and the EDURA Learning Management System are visually represented within this section. The behavioral perspective of the system is illustrated through these diagrams, detailing how the distinct user roles interact with the core functionalities of the platform. 

## **13.1 System Actors** 

Three primary actors by whom the system is utilized have been identified: 

- **Student:** Engagement with educational materials, submission of assessments, uploading of payment receipts, and tracking of personal academic progress are performed by this actor. 

- **Teacher:** The creation of course modules, uploading of video lessons, configuration of interactive quizzes, and monitoring of class performance are executed by this actor. 

- **Administrator:** The overarching management of the platform, including user role assignment, system configuration, and the manual verification of uploaded subscription receipts, is overseen by this actor. 

## **13.2 Student Subsystem Use Case Diagram** 

The specific functionalities accessible to the student actor are detailed in this subsystem diagram. Actions such as viewing video lectures, participating in gamified leaderboards, taking timed quizzes, and downloading course completion certificates are explicitly illustrated. Furthermore, the automated processing of subscription payments via the integrated PayHere gateway is now encompassed within the student's available actions, alongside the manual receipt upload fallback. 

26 

_Figure 38: Student Subsystem Use Case Diagram_ 

## **13.3 Teacher Subsystem Use Case Diagram** 

The instructional and content management capabilities provided to the educational staff are mapped in the following diagram. The processes by which lessons are structured, multiplechoice questions (MCQs) are authored, and student analytical reports are generated are demonstrated. 

27 

_Figure 39: Teacher Subsystem Use Case Diagram_ 

## **13.4 Administrator Subsystem Use Case Diagram** 

The operational and administrative tasks required to maintain the platform are isolated in this final diagram. The workflows through which user accounts are managed and manual subscription payments are verified and approved, are outlined. 

28 

_Figure 40: Administrator Subsystem Use Case Diagram_ 

29 

## **CHAPTER 14** 

## **USE CASE DESCRIPTIONS** 

The step-by-step main success scenarios, alternative flows, and system states for the critical system use cases are documented within this section. The precise sequence of interactions between the identified actors and the EDURA Learning Management System is detailed to provide a comprehensive behavioral blueprint for the development team. 

## **14.1 UC-001: User Authentication and Login** 

_Table 12: UC-001 – User Authentication and Login_ 

|**Element**|**Description**|
|---|---|
|**Use Case ID & Name**|UC-001: User Authentication and Login|
|**Primary Actor**|Student, Teacher, Administrator|
|**Preconditions**|A valid account must have been previously registered by the user<br>within the system.|
|**Main**<br>**Success**<br>**Scenario**|1. The login page is accessed by the user.<br>2. The email address and password are entered and submitted by<br>the user.<br>3. The credentials are validated by the system.<br>4. A One-Time Password (OTP) is generated and dispatched to<br>the user's registered email address by the system.<br>5. The OTP is entered by the user.<br>6. The OTP is verified by the system.<br>7. The user is redirected to the appropriate role-based dashboard<br>by the system.|
|**Alternative Flows**|**3a. Invalid Credentials:**An error message is displayed by the<br>system, and the user is prompted to re-enter the credentials.|



30 

**6a. Invalid or Expired OTP:** An error message is displayed, and the generation of a new OTP is permitted by the system. An active, authenticated session is established for the user, **Postconditions** granting role-specific access to system resources. 

## **14.2 UC-002: Upload Subscription Receipt** 

_Table 13: UC-002 – Upload Subscription Receipt_ 

|**Element**|**Description**|
|---|---|
|**Use Case ID & Name**|UC-002: Upload Subscription Receipt|
|**Primary Actor**|Student|
|**Preconditions**|The student must be authenticated and logged into the platform.<br>A digital copy of the payment receipt must be possessed by the<br>student.|
|**Main**<br>**Success**<br>**Scenario**|1. The subscription portal is navigated to by the student.<br>2. The digital receipt file (e.g., JPEG, PNG, PDF) is selected and<br>uploaded by the student.<br>3. The relevant payment details (e.g., month, amount) are entered<br>and submitted by the student.<br>4. The upload is securely stored, and the submission is recorded<br>as "Pending Verification" by the system.<br>5. A confirmation notification is displayed to the student.|
|**Alternative Flows**|**2a. Invalid File Format/Size:**The upload is rejected by the<br>system, and a warning message specifying the accepted formats<br>and size limits is displayed.|
|**Postconditions**|The payment receipt is stored within the database and flagged for<br>manual administrative review.|



31 

## **14.3 UC-003: Create Educational Module** 

_Table 14: UC-003 – Create Educational Module_ 

|**Element**|**Description**|
|---|---|
|**Use Case ID & Name**|UC-003: Create Educational Module|
|**Primary Actor**|Teacher|
|**Preconditions**|The<br>teacher<br>must<br>be<br>authenticated.<br>Sufficient<br>storage<br>capacity<br>must<br>be<br>available on the cloud server.|
|**Main Success Scenario**|1. The "Course Management" dashboard is<br>accessed by the teacher.<br>2. The "Create New Module" option is<br>selected.<br>3. The module title, description, and<br>required parameters are input by the<br>teacher.<br>4. The private YouTube video ID/URL and<br>any associated Cloudinary media links are<br>entered, and supplementary PDF notes are<br>uploaded.<br>5. The external media links are validated<br>and securely stored in the database by the<br>system.<br>6. The new educational module is published<br>and rendered accessible to active students.|
|**Alternative Flows**|**5a. Upload Interruption:**An error is<br>detected by the system, the incomplete file|



32 

is discarded, and the teacher is prompted to restart the upload process. A new, structured educational module has been successfully added to the system **Postconditions** database and made visible to authorized students. 

## **14.4 UC-004: Attempt Timed Assessment** 

_Table 15: UC-004 – Attempt Timed Assessment_ 

|**Element**|**Description**|
|---|---|
|**Use Case ID & Name**|UC-004: Attempt Timed Assessment|
|**Primary Actor**|Student|
|**Preconditions**|The student must be authenticated and<br>possess an active, verified subscription. The<br>assessment must be actively published by<br>the teacher.|
|**Main Success Scenario**|1. The specific assessment module is<br>opened by the student.<br>2. The "Start Quiz" button is initiated.<br>3. The browser lockdown mechanism is<br>activated, and the countdown timer is<br>commenced<br>by<br>the<br>system.<br>4. The answers (MCQ/True-False) are<br>selected, and the final submission is<br>executed<br>by<br>the<br>student.<br>5. The assessment is automatically graded<br>by the system.|



33 

||6. The final score is recorded in the<br>database, and the results are immediately<br>displayed to the student.|
|---|---|
|**Alternative Flows**|**3a. Tab Switching Detected:**A warning is<br>issued by the system upon the first offense.<br>Upon subsequent offenses, the assessment<br>is forcibly submitted and flagged for<br>review.<br>**4a. Time Expiration:**The timer reaches<br>zero, and the assessment is automatically<br>submitted by the system utilizing the<br>currently selected answers.|
|**Postconditions**|The student's grade is permanently recorded<br>within the database, and the overall course<br>progress metrics are updated by the system.|



## **14.5 UC-005: Automated Subscription Payment via PayHere** 

_Table 16: UC-005 – Automated Subscription Payment via PayHere_ 

|**Element**|**Description**|
|---|---|
|**Use Case ID & Name**|UC-005: Automated Subscription Payment<br>via PayHere|
|**Primary Actor**|Student|
|**Secondary Actor**|PayHere<br>Payment<br>Gateway<br>(External<br>System)|
|**Preconditions**|The student must be authenticated. The<br>system must be successfully integrated with<br>an active PayHere merchant account.|
|**Main Success Scenario**|1. The subscription portal is accessed by the<br>student.|



34 

||2. The "Pay via PayHere" automated<br>payment option is selected.<br>3. The student is securely redirected to the<br>external PayHere checkout gateway by the<br>system.<br>4. Valid payment details (e.g., credit/debit<br>card information) are entered and submitted<br>by the student on the external gateway.<br>5. The transaction is authorized and<br>processed<br>by<br>PayHere.<br>6. A "Success" payment status webhook<br>(server-to-server callback) is securely<br>transmitted by PayHere and received by the<br>EDURA server.<br>7. The student's subscription status is<br>automatically updated to "Active" within<br>the database.<br>8. The student is redirected back to the<br>EDURA dashboard by the gateway, and a<br>payment<br>confirmation<br>message<br>is<br>displayed.|
|---|---|
|**Alternative Flows**|**4a. Payment Declined:**A "Failed" status is<br>returned by the gateway due to insufficient<br>funds or invalid card details. The student is<br>redirected back to the EDURA payment<br>page, an error message is displayed, and<br>course access is not granted.|



35 

||**6a. Webhook Timeout / Network Failure:**<br>The server-to-server webhook is not<br>received by the EDURA system within the<br>expected<br>timeframe.<br>A<br>background<br>reconciliation process is triggered by the<br>system to poll the PayHere API, ensuring<br>the transaction status is eventually verified<br>and synced.<br>**3a. User Cancellation:**The payment<br>process is explicitly canceled by the user<br>while on the external gateway. The user is<br>redirected back to the EDURA portal<br>without any changes being made to the<br>subscription status.|
|---|---|
|**Postconditions**|The subscription fee is successfully<br>processed, and immediate, automated<br>access to the relevant course materials is<br>granted to the student without requiring<br>manual administrative intervention.|



36 

## **CHAPTER 15** 

## **ACTIVITY DIAGRAMS** 

The dynamic behavioral aspects of the EDURA Learning Management System are depicted within this section. The sequential flow of activities, control flows, and decision-making pathways for critical system processes is graphically illustrated through activity diagrams. A clear understanding of the step-by-step execution of core platform functionalities is provided by these models. 

## **15.1 User Authentication and Verification Flow** 

The sequence of operations executed during the user login and registration process is detailed in this diagram. The pathways for credential validation, role identification, and the generation and verification of One-Time Passwords (OTPs) via email are specifically outlined. 

37 

_Figure 41: User Authentication and Verification Activity Diagram_ 

## **15.2 Lesson and Content Management Flow** 

The step-by-step procedure by which new educational modules are created by the teaching staff is mapped in the following diagram. The sequential actions required for validating and embedding private YouTube video links, integrating Cloudinary media assets, attaching supplementary notes, and finalizing course structures are demonstrated. 

38 

_Figure 42: Lesson and Content Management Activity Diagram_ 

## **15.3 Assessment and Auto-Grading Flow** 

The sequence of events occurring when a formal quiz is attempted by a student is represented in this diagram. The initiation of timed sessions, the enforcement of anti-cheating mechanisms, the submission of answers, and the subsequent automated calculation and recording of final grades are explicitly illustrated. 

39 

_Figure 43: Assessment and Auto-Grading Activity Diagram_ 

## **15.4 Subscription Payment Verification Flow** 

The administrative workflow associated with the processing of student subscription payments is outlined in this final diagram. The uploading of manual payment receipts by the student, followed by the visual review, verification, and subsequent approval or rejection by the system administrator, is systematically detailed. 

40 

_Figure 44: Subscription Payment Verification Activity Diagram_ 

41 

## **CHAPTER 16** 

## **EXTERNAL INTERFACE REQUIREMENTS** 

The external interface requirements for the EDURA Learning Management System are formally specified in this section. A seamless and secure interaction between the software system, its end-users, underlying hardware infrastructures, and external third-party services is ensured through these specifications. 

## **16.1 User Interfaces** 

The user interface (UI) is required to be fully responsive, ensuring that optimal viewing and interaction experiences are provided across a wide spectrum of devices, including desktop monitors, tablets, and mobile phones. The visual design is mandated to be intuitive, clean, and aligned with standard educational platform aesthetics. 

Distinct interface layouts and dashboards must be presented based on the authenticated user's role: 

- **Student Interface:** A centralized dashboard by which enrolled courses, active assessments, gamification leaderboards, and overall progress metrics are accessed. A dedicated portal for the manual uploading of subscription payment receipts must also be provided. 

- **Teacher Interface:** A comprehensive content management interface through which video lessons are uploaded, MCQs are authored, and class analytical reports are generated and downloaded. 

- **Administrator Interface:** A system management console utilized for the moderation of user accounts, the configuration of platform settings, and the manual visual verification of student payment receipts. 

## **16.2 Hardware Interfaces** 

As a strictly web-based platform, no bespoke hardware components are directly interacted with by the EDURA application on the client side. However, the following hardware requirements are assumed for optimal system operation: 

- **Client-Side Hardware:** Standard web-enabled devices (e.g., desktop computers, laptops, tablets, or smartphones) equipped with functional displays and standard 

42 

input devices (keyboards/mice/touchscreens) are required to be utilized by the endusers. 

- **Server-Side Hardware:** The application is expected to be hosted on standard cloud infrastructure. Hardware interfaces at the server level (such as CPU allocation, RAM, and physical storage for video content) will be abstracted by the chosen cloud hosting provider and managed via standard operating system protocols. 

## **16.3 Software Interfaces** 

To facilitate extended functionalities, seamless communication with several external software components and application programming interfaces (APIs) is required by the EDURA system. 

- **Google Gemini AI API:** This external API must be integrated to power the platform's digital learning assistant. User queries are transmitted to the API, and contextual educational responses are retrieved and displayed within the student interface. 

- **SMTP (Simple Mail Transfer Protocol) Server:** An external email gateway must be integrated to handle the automated dispatch of One-Time Passwords (OTPs) utilized during user registration, email verification, and password recovery processes. 

- **MongoDB Database:** A NoSQL document-oriented database (MongoDB) is required to be interfaced with for the flexible storage and retrieval of user profiles, course structures, lesson metadata, assessment records, and payment transaction data. The schema-less nature of MongoDB enables rapid iteration on data models as requirements evolve. 

- **Redis Cache:** An in-memory data structure store (Redis) must be integrated for session management, temporary OTP storage, and high-speed caching of frequently accessed data such as leaderboard rankings and student progress metrics. Redis shall reduce database query load and improve overall system responsiveness. 

- **PayHere REST API / Webhook Interface:** This external payment gateway API must be explicitly integrated for the facilitation of automated subscription processing. The initialization of secure payment sessions is executed by transmitting formatted request payloads to this API. Furthermore, asynchronous server-to-server 

43 

transaction confirmations (webhooks) dispatched by PayHere must be securely listened for, authenticated, and processed by the EDURA system to automatically update student subscription statuses. 

- **API Gateway:** An API Gateway must be implemented as the single-entry point for all client requests. Front-end requests are routed by this gateway to the appropriate underlying microservices (e.g., Authentication Service, Course Service, Payment Service). 

- **Microsoft Azure Cloud Services:** The system must interface with various Azure services including Azure Container Instances or Azure Kubernetes Service (AKS) for microservice orchestration, Azure Storage for blob storage of payment receipts and supplementary materials, and Azure Monitor for system logging and performance tracking. 

- **Inter-Service Communication:** Seamless communication between independent microservices is required. This internal communication must be facilitated utilizing lightweight protocols, strictly governed by internal RESTful APIs or message brokers (e.g., RabbitMQ or Kafka) to ensure asynchronous data consistency. 

- **YouTube IFrame Player API / Data API:** This external interface must be integrated to securely embed and control the playback of private video lectures hosted on the client's YouTube channel directly within the student interface. 

- **Cloudinary API:** This external media management interface must be utilized for the optimized delivery, streaming, and potential format transformation of supplementary media assets required by the educational modules. 

## **16.4 Communication Interfaces** 

The protocols and standards by which data is transmitted between the client browsers, the web server, and external APIs are explicitly defined as follows: 

- **HTTPS Protocol:** All data transmissions over the network are strictly required to be encrypted utilizing standard SSL/TLS protocols (HTTPS) to prevent the interception of sensitive user credentials and assessment data. 

44 

- **RESTful Architecture:** Communication between the front-end user interface and the back-end server is required to be structured according to REST (Representational State Transfer) principles. 

- **Data Formatting:** The JSON (JavaScript Object Notation) format shall be exclusively utilized for the packaging and transmission of data payloads between the server and the web client. 

45 

## **CHAPTER 17** 

## **DATA REQUIREMENTS** 

The logical structuring, storage mechanisms, and security protocols concerning the information managed by the EDURA Learning Management System are outlined in this section. The persistent and secure storage of user profiles, educational content, financial records, and assessment grades is ensured through these specifications. 

## **17.1 Logical Data Entities** 

The underlying conceptual structure of the system data is defined by several core entities. The interrelations between these entities are strictly configured to maintain referential integrity across the system. 

- **User Entity:** Authentication credentials, role designations (Admin, Teacher, Student), and basic profile information (name, email) are stored within this entity. 

- **Course and Lesson Entities:** The hierarchical organization of educational modules is managed. Instead of physical video file paths, the unique youtube_video_id and cloudinary_asset_url are persistently stored alongside supplementary document paths and descriptive metadata. 

- **Assessment Entity:** The structural configurations for quizzes, including multiplechoice question sets, predefined correct answers, and allocated time limits, are recorded. 

- **Submission and Grading Entity:** Student assessment attempts, specifically selected answers, automatically calculated final scores, and completion timestamps, are captured. 

- **Subscription Entity:** Financial access records and transaction details are securely maintained within this entity. To accommodate both automated gateway transactions and manual receipt verifications, specific data attributes, including the payment_method (constrained to an enumeration of 'MANUAL' or 'PAYHERE'), the external transaction_id (retrieved from the payment gateway), and the payment_status (constrained to an enumeration of 'PENDING', 'SUCCESS', or 'FAILED'), are systematically recorded alongside uploaded receipt image paths and subscription validity periods. 

46 

## **17.2 Data Storage Mechanisms** 

A NoSQL document-oriented database management system (MongoDB) is mandated to be utilized for the structured storage of all educational content, user profiles, assessment data, and transactional records. MongoDB's flexible schema design accommodates the varying structures of different course types, lesson formats, and assessment configurations without requiring rigid table definitions. 

Redis, an in-memory data structure store, is required to be deployed alongside MongoDB to provide: 

- Session state management for authenticated users 

- Temporary storage of One-Time Passwords (OTPs) with automatic expiration 

- Cached leaderboard data and aggregated analytics 

- Real-time subscription status lookups 

External media references (YouTube video IDs and Cloudinary asset URLs) are stored as string fields within MongoDB documents, entirely eliminating the necessity for heavy cloud blob storage of video files. Minimal cloud storage on Microsoft Azure Blob Storage is allocated for handling smaller binary files such as PDF supplementary notes and imagebased payment receipts. 

## **17.3 Data Security and Integrity** 

Strict data protection mechanisms are required to be enforced at the database level to prevent unauthorized access and data breaches. 

- **Cryptographic Hashing:** All user passwords must be securely hashed utilizing modern cryptographic algorithms (e.g., bcrypt) prior to storage; the database storage of plain-text passwords is strictly prohibited. 

- **Access Control:** Direct database access is severely restricted. Modifications and queries are permitted to be executed exclusively through authorized back-end API services or by designated high-level database administrators. 

- **Input Validation:** Strict data typing and sanitization rules must be applied to all incoming data payloads to prevent SQL injection vulnerabilities and preserve overall data consistency. 

47 

## **17.4 Data Retention and Backup** 

To mitigate the risk of catastrophic data loss, automated data preservation strategies must be systematically executed. Complete relational database backups are required to be generated automatically on a daily (24-hour) schedule. Furthermore, these database backup archives must be securely retained in a geographically distinct server location for a minimum operational period of thirty days before automated overwriting or deletion is permitted. 

48 

## **CHAPTER 18** 

## **ALTERNATIVE SOLUTIONS CONSIDERED** 

The various architectural approaches, platform delivery methods, and technical methodologies that were evaluated during the initial design phase of the EDURA Learning Management System are detailed in this section. Furthermore, the justifications for the ultimately selected solutions are provided to demonstrate the rationale behind the system's design. 

## **18.1 Architectural Approach: Monolithic vs. Decoupled RESTful API** 

During the initial planning phase, traditional monolithic architecture was considered due to its perceived simplicity in early-stage development and deployment. However, this approach was ultimately rejected because flexibility is significantly limited by monolithic structures, and future integrations or system scaling are often complicated by tightly coupled codebases. 

To implement this microservice architecture, the system leverages a modern technology stack optimized for scalability and developer productivity. The frontend user interface is built using the Next.js framework, providing server-side rendering capabilities and optimized performance for student-facing web pages. Backend microservices are exclusively implemented in Python, ensuring consistency across service boundaries and leveraging Python's extensive ecosystem for data processing, API development, and integration with machine learning libraries (utilized by the Google Gemini AI assistant). All services are containerized using Docker and orchestrated on the Microsoft Azure cloud platform, with MongoDB serving as the primary database and Redis providing high-speed caching and session management. 

The adoption of microservices architecture in educational platforms has been extensively validated in recent literature. Studies demonstrate that microservices enable independent scalability of system components, reduce deployment time by up to 40%, and significantly improve fault isolation compared to monolithic architectures [14][15][16]. In e-learning contexts specifically, microservices-based LMS implementations have achieved infrastructure cost reductions of 50-70% while maintaining superior performance and availability [17][18]. 

49 

## **18.2 Platform Delivery: Native Mobile Application vs. Responsive Web Application** 

The development of dedicated native mobile applications (specifically for iOS and Android platforms) was extensively evaluated to maximize mobile user engagement. However, this alternative was dismissed due to the strict academic time constraints imposed on the project and the limited capacity of the four-member development team. The simultaneous maintenance of multiple codebases was deemed unfeasible within the allocated project lifecycle. 

Therefore, a fully responsive web-based application was chosen as the primary delivery mechanism. This approach is justified because cross-platform compatibility across desktops, tablets, and smartphones is guaranteed by responsive web design without incurring the overhead of native app development. 

## **18.3 Payment Processing: Automated Gateway vs. Manual Verification vs. Hybrid Approach** 

To process student subscriptions, the exclusive use of a fully automated payment gateway and the exclusive use of manual receipt verifications were initially evaluated as mutually exclusive alternatives. However, a hybrid approach to subscription processing was ultimately selected as the optimal solution. 

To automate transaction processing, provide immediate course access, and significantly reduce the administrative overhead associated with visual verifications, the PayHere payment gateway was integrated into the system. Concurrently, the manual receipt upload functionality was retained as a necessary fallback mechanism. This dual-method approach is justified because an equitable and accessible system is ensured for all students, particularly those who do not have bank accounts, credit cards, or debit cards, while the workflow for system administrators is simultaneously optimized. 

## **18.4 Content Delivery: Local Server Storage vs. Third-Party Media Platforms** 

The storage and streaming of large binary files, particularly extensive pre-recorded video lectures, were initially proposed to be handled directly on the local web server's file system. This method was rejected because server bandwidth and storage capacity are rapidly exhausted by heavy media files, which invariably leads to severe performance degradation during concurrent student access. 

50 

Alternatively, a specialized external media hosting strategy was selected. Primary video lectures are mandated to be uploaded to a private YouTube channel, ensuring that video hosting is offloaded to a highly scalable network and access is strictly restricted to website redirection and embedding. Furthermore, Cloudinary is utilized to manage advanced video streaming capabilities, media quality optimization, and additional asset delivery. This decision is justified because high availability, adaptive bitrate streaming, and the complete preservation of local server bandwidth are inherently provided by these dedicated platforms, ensuring that system performance is not compromised by large media distributions. 

51 

## **CHAPTER 19** 

## **FEASIBILITY STUDY** 

A comprehensive evaluation of the EDURA Learning Management System's viability across technical, economic, operational, and scheduling dimensions is presented in this section. The project's likelihood of success, given the established constraints and chosen technological integrations, is formally assessed. 

## **19.1 Technical Feasibility** 

The project is determined to be technically feasible, although significant technical complexity is introduced by the chosen microservice architecture. 

- **Architecture:** The implementation of independent microservices, an API gateway, and decentralized databases requires advanced containerization (e.g., Docker) and rigorous DevOps practices. However, fault isolation is substantially improved, and independent scaling is enabled by this approach, making it highly suitable for modern web applications. 

- **Media Handling:** The severe technical risks associated with server bandwidth exhaustion and massive storage requirements are completely mitigated by the strategic offloading of video hosting to private YouTube channels and Cloudinary. High-quality, adaptive bitrate streaming is inherently guaranteed by these established third-party APIs. 

- **Payment Integration:** The automated processing of subscriptions is facilitated by the PayHere REST API. The secure handling of webhooks is a standard, welldocumented technical procedure, ensuring that system synchronization can be reliably achieved. 

- **Technology Stack Maturity:** The chosen technology stack (Next.js, Python, MongoDB, Redis, Azure) represents mature, production-ready frameworks and platforms with extensive community support and documentation. Next.js provides built-in optimizations for SEO and performance, Python offers rich libraries for API development (FastAPI, Flask) and AI integration, MongoDB's flexible schema supports rapid development cycles, and Redis is an industry-standard caching solution. The team's proficiency in these technologies has been verified through preliminary prototyping exercises. 

52 

MongoDB's flexible NoSQL architecture has been specifically validated for educational platforms requiring rapid schema evolution and high-volume concurrent access patterns [19]. The combination of microservices with containerization technologies like Docker and Kubernetes has demonstrated significant improvements in deployment efficiency and system resilience for e-learning platforms [20]. 

## **19.2 Economic Feasibility** 

The development and ongoing operation of the EDURA system are deemed highly economically feasible due to strategic architectural choices designed to minimize recurring costs. 

- **Development Costs:** Because the software is being developed as an academic project by the four assigned members of Team ZYNAPTRIX, preliminary external development costs and third-party outsourcing fees are completely eliminated. 

- **Operational and Hosting Costs:** Server infrastructure costs are drastically minimized through a combination of strategic design decisions. The third-party media strategy (YouTube and Cloudinary) eliminates expensive video storage requirements. MongoDB Atlas offers a generous free tier for development and costeffective scaling tiers for production. Redis can be deployed on lightweight Azure Container Instances. Furthermore, Microsoft Azure's pay-as-you-go pricing model and targeted microservice scaling ensure that costs align directly with actual system usage rather than maintaining over-provisioned monolithic infrastructure. 

- **Administrative Savings:** The administrative labor costs previously required for the manual verification of hundreds of payment receipts are significantly reduced by the automated PayHere gateway integration. 

## **19.3 Operational Feasibility** 

The system is evaluated as highly operationally feasible, as the workflows of all primary actors (Students, Teachers, and Administrators) are streamlined by the proposed solutions. 

- **Student Accessibility:** A highly equitable operational environment is ensured by the hybrid payment strategy. Immediate course access is provided to users possessing credit or debit cards via the automated PayHere gateway, while the manual receipt upload mechanism is preserved to ensure that students lacking digital banking capabilities are not excluded from the platform. 

53 

- **Educator Workflow:** The lesson creation process is significantly expedited for the teaching staff. The time-consuming uploading of massive video files over potentially unstable internet connections is replaced by the rapid embedding of pre-existing YouTube and Cloudinary URLs. 

- **Administrative Workflow:** System management is optimized, as routine subscription activations are automated, allowing administrative efforts to be focused exclusively on the subset of students utilizing the manual payment fallback. 

## **19.4 Schedule Feasibility** 

The successful delivery of the EDURA platform is strictly bound by the academic timeline mandated by the Software Engineering Teaching Unit. Despite these strict constraints, the project is considered schedule feasible. 

- **Parallel Development:** The simultaneous, non-blocking development of discrete system modules by the four team members is facilitated by the decoupled nature of the microservice architecture. For instance, the Authentication Service, Course Management Service, and Payment Service can be programmed and tested in parallel, thereby accelerating the overall development lifecycle. 

- **Reduced Implementation Time:** The time previously allocated for the development of complex, custom video streaming algorithms and heavy file-handling logic is reclaimed through the utilization of YouTube and Cloudinary APIs, ensuring that the project deadlines can be confidently met. 

54 

## **CHAPTER 20** 

## **RISK ANALYSIS** 

Potential technical, operational, and external risks by which the successful deployment and continuous operation of the EDURA Learning Management System could be threatened are identified and evaluated in this section. To ensure system resilience and project success, proactive mitigation strategies for each identified vulnerability are formally defined. 

## **20.1 Identified Risks and Mitigation Strategies** 

The primary project risks, categorized by their source and accompanied by their respective mitigation protocols, are detailed in the following table: 

_Table 17: Risk Analysis and Mitigation Strategies_ 

|**Risk Category**|**Risk Description**|**Probability**<br>**/**<br>**Impact**|**Mitigation Strategy**|
|---|---|---|---|
|**Architectural**|**Distributed**<br>**Data**<br>**Inconsistency:**Because<br>the system is decoupled<br>into<br>independent<br>microservices,<br>network<br>latency<br>or<br>partial<br>transaction<br>failures<br>between services may be<br>experienced, leading to<br>inconsistent data states.|Medium / High|Robust<br>inter-service<br>communication<br>protocols,<br>circuit<br>breaker patterns, and<br>eventual<br>consistency<br>models (such as the Saga<br>pattern)<br>must<br>be<br>implemented.<br>Comprehensive logging<br>must be utilized to trace<br>communication failures.|
|**External**<br>**Dependency**|**Third-Party**<br>**Service**<br>**Outages:**Critical system<br>functionalities,<br>specifically<br>video<br>streaming and automated<br>payment<br>processing,<br>could<br>be<br>severely<br>impacted if downtime is|Low / High|Comprehensive<br>error<br>handling and graceful<br>UI degradation must be<br>implemented.<br>If<br>payment webhooks fail,<br>a<br>background<br>reconciliation<br>process<br>must be triggered to|



55 

||experienced<br>by<br>the<br>YouTube, Cloudinary, or<br>PayHere APIs.||automatically poll the<br>PayHere<br>API<br>for<br>pending<br>transaction<br>statuses.|
|---|---|---|---|
|**Security**|**Unauthorized Content**<br>**Distribution:**<br>Private<br>YouTube video links or<br>Cloudinary asset URLs<br>might<br>be<br>maliciously<br>extracted from the source<br>code and shared by active<br>students<br>with<br>unauthorized individuals.|High / High|Domain-level<br>embedding restrictions<br>must be strictly enforced<br>on the YouTube private<br>channel<br>(allowing<br>playback only on the<br>EDURA<br>domain).<br>Furthermore,<br>dynamically generated,<br>time-expiring<br>signed<br>URLs must be utilized<br>for Cloudinary assets.|
|**Operational**|**Administrative**<br>**Bottlenecks:**<br>A<br>significant<br>backlog<br>in<br>subscription<br>activations<br>might be created if a large<br>volume<br>of<br>manual<br>payment<br>receipts<br>is<br>uploaded<br>by<br>students<br>simultaneously,<br>particularly<br>near<br>examination periods.|Medium<br>/<br>Medium|The automated PayHere<br>gateway must be heavily<br>promoted to students as<br>the primary payment<br>method.<br>Additionally,<br>bulk verification tools<br>must be provided within<br>the<br>administrator<br>dashboard to expedite<br>manual reviews.|
|**Technical**|**Technology**<br>**Stack**<br>**Integration**<br>**Complexity:**Integrating<br>Next.js<br>frontend<br>with<br>Python<br>backend<br>microservices, MongoDB|Medium<br>/<br>Medium|Establish<br>clear<br>API<br>contracts<br>using<br>OpenAPI/Swagger<br>specifications.<br>Implement<br>comprehensive|



56 

||data layer, Redis caching,<br>and multiple third-party<br>APIs (PayHere, YouTube,<br>Cloudinary, Gemini AI)<br>may<br>introduce<br>compatibility<br>issues,<br>serialization challenges,<br>or<br>deployment<br>complexities.||integration testing in<br>staging<br>environments<br>that mirror production<br>Azure<br>infrastructure.<br>Utilize<br>Docker<br>Compose<br>for<br>local<br>development to ensure<br>environment<br>parity.<br>Maintain<br>detailed<br>technical documentation<br>for<br>each<br>service<br>interface.|
|---|---|---|---|
|**Schedule**|**Academic**<br>**Deadline**<br>**Overrun:**The project<br>deadlines mandated by<br>the university might not<br>be<br>met<br>by<br>the<br>development team due to<br>the inherent complexity<br>of<br>configuring<br>microservices<br>and<br>integrating<br>multiple<br>external APIs.|Medium / High|Strict<br>agile<br>methodologies must be<br>adhered to by Team<br>ZYNAPTRIX.<br>A<br>Minimum<br>Viable<br>Product<br>(MVP)<br>encompassing only core<br>functionalities must be<br>prioritized<br>and<br>completed prior to the<br>implementation<br>of<br>secondary features (e.g.,<br>gamification).|



## **20.2 Continuous Risk Monitoring** 

The identified risks are not static; therefore, continuous monitoring throughout the software development lifecycle is required. Regular technical reviews and code audits must be conducted by the development team to ensure that the mitigation strategies outlined above are successfully integrated into the system's microservice architecture. 

57 

## **CHAPTER 21** 

## **REFERENCES** 

[1] Pan, Z., Biegley, L., Taylor, A., & Zheng, H. (2024). A Systematic Review of Learning Analytics: Incorporated Instructional Interventions on Learning Management Systems. _Journal of Learning Analytics_ , 11(2), 52-72. https://doi.org/10.18608/jla.2023.8093 

[2] Liliasari, L., & Riza, L. S. (2023). The Impact of Learning Management System (LMS) Usage on Students. _TEM Journal_ , 12(2), 1082-1089. https://doi.org/10.18421/TEM122-54 

[3] Simon, P. D., Jiang, J., & Fryer, L. K. (2024). Measurement of higher education students' and teachers' experiences in learning management systems: A scoping review. _Assessment & Evaluation in Higher Education_ , 49(4), 441-452. https://doi.org/10.1080/02602938.2023.2266154 

[4] Romdhoni, R. D., & Romdhoni, A. (2026). The Effectiveness of Learning Management Systems (LMS) in Enhancing Learning Experiences toward Achieving SDG 4: Quality Education. _Journal of Information System and Education Development_ , 4(1), 39–46. https://doi.org/10.62386/jised.v4i1.210 

[5] Aulianda, N., Wijayati, P. H., Ebner, M., & Schön, S. (2023). Analysis of Learning Management System towards Students' Cognitive Learning Outcome. _International Journal of Emerging Technologies in Learning (IJET)_ , 18(23), 4–26. https://doi.org/10.3991/ijet.v18i23.36443 

[6] Zeng, X. (2024). Exploring the impact of gamification on students' academic performance: A comprehensive meta-analysis of studies from the year 2008 to 2023. _British Journal of Educational Technology_ , 55(4), 1471-1492. https://doi.org/10.1111/bjet.13471 

[7] Nguyen-Viet, B., Nguyen-Duy, C., & Nguyen-Viet, B. (2024). How does gamification affect learning effectiveness? The mediating roles of engagement, satisfaction, and intrinsic motivation. _Interactive Learning Environments_ , 33(3), 2635-2653. https://doi.org/10.1080/10494820.2024.2414356 

[8] Zhang, L., & Wang, Y. (2024). Impact of Gamification on Students' Learning Outcomes and Academic Performance: A Longitudinal Study Comparing Online, Traditional, and 

58 

Gamified Learning. _Education Sciences_ , 14(4), 367. https://doi.org/10.3390/educsci14040367 

[9] Alsabhan, W. (2023). Student Cheating Detection in Higher Education by Implementing Machine Learning and LSTM Techniques. _Sensors_ , 23(8), 4149. https://doi.org/10.3390/s23084149 

[10] Yulita, I.N., Hariz, F.A., Suryana, I., & Prabuwono, A.S. (2023). Educational Innovation Faced with COVID-19: Deep Learning for Online Exam Cheating Detection. _Education Sciences_ , 13(2), 194. https://doi.org/10.3390/educsci13020194 

[11] Hussein, F., Al-Ahmad, A., El-Salhi, S., Alshdaifat, E., & Al-Hami, M. (2022). Advances in Contextual Action Recognition: Automatic Cheating Detection Using Machine Learning Techniques. _Data_ , 7(9), 122. https://doi.org/10.3390/DATA7090122 

[12] Ozdamli, F., Aljarrah, A., Karagozlu, D., & Ababneh, M. (2022). Facial Recognition System to Detect Student Emotions and Cheating in Distance Learning. _Sustainability_ , 14(19), 13230. https://doi.org/10.3390/su141913230 

[13] Market Research Reports. (2024). Global Online Exam Proctoring Market 2023-2029. Cited in: HackerEarth Blog. (2025). Online Assessment Cheating Prevention Technologies. Retrieved February 2025 from https://www.hackerearth.com/blog/ 

[14] Sharma, S. (2025). The Impact of Microservices Architecture on System Scalability. _American Scientific Research Journal for Engineering, Technology, and Sciences_ , 102(1), 140-148. https://asrjetsjournal.org/American_Scientific_Journal/article/view/11677 

[15] Henríquez, C., Valencia, J. D. R., & Torres, G. S. (2025). Architectural Evolution at Netflix: A Case Study on Microservices and the Transformation from Monolithic to Scalable Systems. _Prospectiva_ , 23(1), 1-14. 

[16] Thallapally, N. (2024). Microservices architecture in cloud-native applications: Design patterns and scalability. _International Journal of Science and Research Archive_ , 13(02), 4140-4145. 

[17] Peng, C. F., et al. (2023). Design and Implementation of a Microservices-Based Online Learning Platform. In _Proceedings of the 2023 2nd International Conference on Educational Innovation and Multimedia Technology (EIMT 2023)_ (pp. 455-460). 

59 

[18] eLearning Industry. (2022). Microservices Architecture And Migration in Learning Management Systems. Retrieved from https://elearningindustry.com/migrating-monolithiclearning-management-system-to-microservice-architecture 

[19] Kumar, C. (2024). NoSQL Database Implementation for Learning Management Systems. _International Journal of Novel Research and Development_ , 9(5), 793-801. 

[20] Mynkis Digital Solutions. (2024). Microservices: Building Blocks for Scalable Educational Platforms. Retrieved from https://www.mynkis.com/articles/microservices-foreducational-platforms 

60 

## **CLIENT REQUIREMENT SIGN-OFF** 

The Software Requirements Specification (SRS) document for the EDURA Learning Management System has been thoroughly reviewed, and its contents are formally accepted by the undersigned. 

It is acknowledged by all parties that the functional and non-functional requirements, business rules, structural constraints, and architectural decisions, specifically encompassing the microservice architecture, the integration of third-party media platforms (YouTube and Cloudinary), and the hybrid payment processing mechanism (PayHere), as detailed herein, accurately reflect the agreed-upon project scope. 

It is further understood that any subsequent modifications, additions, or removals to these formally agreed-upon requirements following the execution of this document must be subjected to a formal change control process and may impact the academic project timeline. 

## **Accepted and Approved By:** 

## **1. Client / Project Sponsor** 

Name: Mr. Dimuthu Prabath 

Title: Head of Institute, "ICT - Dimuthu" 

Signature: ___________________________ CO 

Date: 19/03/2026 

## **2. Academic Supervisor (University of Kelaniya)** 

Name: _______________________________ 

Title: _______________________________ 

Signature: ___________________________ 

Date: _______________________________ 

61 

**Appendix C: System Design Specification** 

**EDURA - Learning Management System Software Design Specification (SDS)** 

**By** 

**W.G.N.DANANJAYA SE/2021/047 R.W.V.I.D.RAJAPAKSHA SE/2021/029 P.D.D.RANSIKA SE/2021/034 H.T.MADUSHANKA SE/2021/011** 

**A report submitted in partial fulfillment of the requirements for the degree of Bachelor of Science Honors in Software Engineering (B.Sc. SE)** 

**Software Engineering Teaching Unit** 

**Faculty of Science** 

**University of Kelaniya** 

**Sri Lanka** 

**2026** 

55 

## **VERSION HISTORY** 

|**Version**|**Date**|**Author(s)**|**Changes**|
|---|---|---|---|
|1.0|19/04/2026|Nadun Dananjaya,<br>Imansha Dilshan,<br>Danindu Ransika,<br>Thushan Madhusanka|<br>Initial SDS<br>document creation|



i 

## **TABLE OF CONTENTS** 

LIST OF TABLES ..................................................................................................v LIST OF FIGURES ............................................................................................... vi CHAPTER 1 INTRODUCTION ............................................................................ 26 1.1 Document Purpose ...................................................................................... 26 1.2 System Overview ........................................................................................ 26 1.3 Scope of This Document .............................................................................. 26 CHAPTER 2 ARCHITECTURAL DESIGN ............................................................ 28 2.1 High-Level Architecture: Microservices ......................................................... 28 2.2 Cloud-Native Architecture ............................................................................ 30 2.3 Justification for Architectural Choices ............................................................ 31 2.3.1 Why Microservices? .............................................................................. 31 2.3.2 Why Nginx as API Gateway? .................................................................. 31 2.3.3 Why RabbitMQ for Message Broker? ...................................................... 31 2.3.4 Why Redis for Caching? ........................................................................ 31 2.3.5 Why PostgreSQL Neon? ........................................................................ 32 2.4 Scalability & Maintainability Considerations .................................................. 32 CHAPTER 3 DATABASE DESIGN ....................................................................... 33 3.1 Database Architecture Overview ................................................................... 33 3.2 Entity-Relationship Diagram......................................................................... 33 3.3 Database Normalization Strategy ................................................................... 33 CHAPTER 4 CLASS DIAGRAM .......................................................................... 35 4.1 Class Diagram Overview .............................................................................. 35 4.2 Class Diagram ............................................................................................ 35 CHAPTER 5 SEQUENCE DIAGRAMS ................................................................. 36 5.1 Sequence Diagram Overview ........................................................................ 36 5.2 Sequence Diagrams ..................................................................................... 36 5.2.1 User Authentication and Login Flow ........................................................ 36 5.2.2 Course Creation and Publishing Flow ...................................................... 37 5.2.3 Student Enrollment and Payment Processing Flow ..................................... 38 

ii 

5.2.4 Assessment Taking and Automated Grading Flow ...................................... 39 5.2.5 Progress Tracking and Certificate Generation Flow ....................................... 40 5.2.6 Analytics Report Generation Flow ........................................................... 41 5.2.7 AI Assistant Interaction Flow .................................................................. 42 5.2.8 Content Streaming Flow ........................................................................ 43 CHAPTER 6 UI/UX DESIGN ............................................................................... 44 6.1 Wireframes for Key User Interfaces ............................................................... 44 6.1.1 Authentication Interfaces ........................................................................ 44 6.1.2 Student Dashboard ................................................................................ 45 6.1.3 Course Catalog/Browse Interface ............................................................ 45 6.1.4 Course Content Viewer .......................................................................... 46 6.1.5 Assessment Interface ............................................................................. 47 6.1.6 Progress and Analytics Dashboard ........................................................... 47 6.1.7 Admin Dashboard ................................................................................. 48 6.1.8 Profile and Settings ............................................................................... 49 6.2 User Flow Diagrams .................................................................................... 50 6.3 Accessibility Considerations (WCAG 2.1 Level AA) ........................................ 56 CHAPTER 7 SECURITY DESIGN ........................................................................ 57 7.1 Security Architecture Overview ..................................................................... 57 7.2 Authentication Mechanism ........................................................................... 57 7.2.1 Identity Provider Integration (Asgardeo) ................................................... 57 7.2.2 Token Management ............................................................................... 59 7.2.3 Session Management ............................................................................. 59 7.2.4 Email Verification and OTP .................................................................... 60 7.3 Authorization Levels ................................................................................... 64 7.3.1 Role-Based Access Control (RBAC) ........................................................ 64 7.3.2 Permission Enforcement ........................................................................ 65 7.4 Data Protection Approach ............................................................................. 66 7.4.1 Data Classification ................................................................................ 66 7.4.2 Data Storage Security ............................................................................ 67 7.4.3 Data Transmission Security .................................................................... 67 7.5 Input Validation and Sanitization Strategy ....................................................... 68 

iii 

7.5.1 Client-Side Validation ............................................................................ 68 7.5.2 Server-Side Validation ........................................................................... 69 7.5.3 File Upload Validation ........................................................................... 70 7.6 Encryption Standards ................................................................................... 71 7.6.1 Data at Rest Encryption ......................................................................... 71 7.6.2 Data in Transit Encryption ...................................................................... 71 7.6.3 Encryption Key Management .................................................................. 72 CHAPTER 8 DEPLOYMENT DESIGN ................................................................. 73 8.1 Hosting Plan & Infrastructure ....................................................................... 73 8.2 Hardware & Resource Requirements .............................................................. 73 8.3 Network Diagram ....................................................................................... 74 8.4 Environment Specifications .......................................................................... 75 8.5 CI/CD Pipeline Overview ............................................................................. 75 CHAPTER 9 REFERENCES ................................................................................ 76 

iv 

## **LIST OF TABLES** 

Table 1: Hardware and Resource Requirements ........................................................ 73 

v 

## **LIST OF FIGURES** 

Figure 1: High-Level Microservice Architecture Diagram ................................................. 30 Figure 2: Entity - Relationship Diagram ............................................................................. 33 Figure 3: Class Diagram ...................................................................................................... 35 Figure 4: User Authentication and Login Flow Diagram .................................................... 36 Figure 5: Course Creation and Publishing Flow Diagram .................................................. 37 Figure 6: Student Enrollment and Payment Processing Flow Diagram .............................. 38 Figure 7: Assessment Taking and Automated Grading Flow Diagram ............................... 39 Figure 8: Progress Tracking and Certificate Generation Flow Diagram ............................. 40 Figure 9: Analytics Report Generation Flow Diagram ........................................................ 41 Figure 10: AI Assistant Interaction Flow Diagram .............................................................. 42 Figure 11: Content Streaming Flow .................................................................................... 43 Figure 12: User Sign-in Interface ........................................................................................ 44 Figure 13: User Sign-up Interface ....................................................................................... 44 Figure 14: Student Dashboard Interface .............................................................................. 45 Figure 15: Course Catalog Interface .................................................................................... 45 Figure 16: High-level Course Content Viewer Interface ..................................................... 46 Figure 17: Expanded Course Content Viewer Interface ...................................................... 46 Figure 18: Assessment Interface .......................................................................................... 47 Figure 19: Statistical Dashboard View ................................................................................ 47 Figure 20: Graphical Dashboard View ................................................................................ 48 Figure 21: Admin Dashboard Interface ............................................................................... 48 Figure 22: User Profile Interface ......................................................................................... 49 Figure 23: Student Registration and Onboarding Flow ....................................................... 50 Figure 24: Course Enrollment Flow .................................................................................... 51 Figure 25: Learning Path Flow ............................................................................................ 52 Figure 26: Assessment Flow ................................................................................................ 53 Figure 27: Teacher Course Creation Flow ........................................................................... 54 Figure 28: Admin Payment Verification Flow ..................................................................... 55 Figure 29: Authentication Flow ........................................................................................... 58 Figure 30: Registration Flow ............................................................................................... 61 Figure 31: Password Reset Flow ......................................................................................... 63 Figure 32: Network diagram................................................................................................ 74 

vi 

## **CHAPTER 1 INTRODUCTION** 

## **1.1 Document Purpose** 

The purpose of this System Design Specification (SDS) document is to provide a comprehensive technical design blueprint for the EDURA Learning Management System. This document outlines the architectural decisions, database schema, class structures, interaction flows, user interface specifications, security mechanisms, and deployment strategies that will guide the development team in implementing a robust, scalable, and maintainable educational platform. 

## **1.2 System Overview** 

EDURA is a comprehensive web-based Learning Management System designed specifically for the ICT - Dimuthu educational institute. The system facilitates online education for Advanced Level A/L students by enabling educators to create, manage, and deliver digital courses, assessments, and learning materials. 

The platform employs a microservices architecture to ensure scalability, maintainability, and independent deployment of services. The system is built using Next.js for the frontend with Redux for state management, Python-based microservices for the backend, PostgreSQL Neon for data persistence, Redis for caching, and RabbitMQ for inter-service communication. Authentication is managed through Asgardeo, media files are stored and streamed via Cloudinary, and payments are processed through PayHere gateway with a hybrid approach supporting both automated and manual verification. 

## **1.3 Scope of This Document** 

This document covers the technical design aspects of the EDURA system, including: 

- High-level and detailed architectural design with justification 

- Database schema design with normalization strategies 

- Object-oriented design through class diagrams 

- System behavior through sequence diagrams 

- User interface specifications and accessibility considerations 

- Security architecture includes 

26 

- authentication, authorization, and data protection 

- Deployment architecture on Microsoft Azure with CI/CD pipeline specifications 

27 

## **CHAPTER 2 ARCHITECTURAL DESIGN** 

## **2.1 High-Level Architecture: Microservices** 

The system is decomposed into loosely coupled, independently deployable services, each responsible for a specific business capability. The microservices communicate through asynchronous message queuing using RabbitMQ and synchronous REST APIs where appropriate. 

## **Key Architectural Components:** 

## 1. **API Gateway (Nginx)** 

   - Entry point for all client requests 

   - Request routing to appropriate microservices 

   - Load balancing and rate limiting 

   - SSL/TLS termination 

   - Authentication token validation 

2. **Microservices Layer** 

   - User Service 

   - Authentication Service 

   - Course Service 

   - Content Service 

   - Enrollment Service 

   - Assessment Service 

   - Progress Tracking Service 

   - Payment Service 

   - Notification Service 

   - Analytics Service 

   - Admin Service 

28 

## 3. **Message Broker (RabbitMQ)** 

- Asynchronous inter-service communication 

- Event-driven architecture support 

- Decoupling of services 

- Message persistence and reliability 

## 4. **Cache Layer (Redis)** 

- Session management 

- Frequently accessed data caching 

- Performance optimization 

- Reduced database load 

## 5. **Data Persistence Layer (PostgreSQL Neon)** 

- Distributed database per service pattern 

- Data isolation and independence 

- ACID compliance for transactional operations 

## 6. **External Services** 

- Asgardeo (Identity and Access Management) 

- Cloudinary (Media storage and streaming) 

- PayHere (Payment gateway) 

- Google Gemini AI (Intelligent assistant) 

- Email/SMS Gateway (Notifications) 

29 

_Figure 45: High-Level Microservice Architecture Diagram_ 

## **2.2 Cloud-Native Architecture** 

The system utilizes **Microsoft Azure** to handle infrastructure management. 

- **Container Orchestration: Azure Kubernetes Service (AKS)** manages the lifecycle of the microservices, handling self-healing and service discovery. 

- **Global Content Delivery:** Media and video streaming are offloaded to **Cloudinary’s CDN** to ensure low-latency video playback for students across the country. 

- **Identity as a Service (IDaaS):** Authentication is outsourced to **Asgardeo** , providing enterprise-grade security and OAuth 2.0/OIDC compliance without the overhead of building a custom auth engine. 

- **Serverless Scaling: PostgreSQL Neon** provides a serverless database layer that scales compute resources up or down automatically based on active query load. 

30 

## **2.3 Justification for Architectural Choices** 

## 2.3.1 Why Microservices? 

**Scalability:** Individual services can be scaled independently based on load. For example, during assessment periods, the Assessment Service can be scaled horizontally without affecting other services. 

**Technology Flexibility:** Different services can use optimal technology stacks. While Python is used for backend services, the choice allows for service-specific optimizations. 

**Independent Deployment:** Services can be deployed, updated, and rolled back independently, reducing deployment risk and downtime. 

**Team Autonomy:** Development teams can work on different services simultaneously without coordination overhead. 

**Fault Isolation:** Failure in one service does not cascade to the entire system. Circuit breakers and fallback mechanisms ensure system resilience. 

**Business Alignment:** Each service maps to a specific business capability, making the system easier to understand and maintain. 

- 2.3.2 Why Nginx as API Gateway? 

   - High performance and low resource consumption 

   - Proven load balancing capabilities 

   - Native SSL/TLS termination 

   - Cost-effective compared to commercial alternatives 

- 2.3.3 Why RabbitMQ for Message Broker? 

   - Robust message persistence and delivery guarantees 

   - Support for multiple messaging patterns (pub/sub, point-to-point, request/reply) 

   - Easy integration with Python services 

   - Proven reliability in production environments 

- 2.3.4 Why Redis for Caching? 

   - In-memory data structure store provides exceptional read/write performance 

31 

   - Support for complex data structures (strings, hashes, lists, sets) 

   - Pub/Sub capabilities for real-time features 

   - Native support in Python ecosystem 

- 2.3.5 Why PostgreSQL Neon? 

   - Serverless PostgreSQL with automatic scaling 

   - Separation of storage and compute 

   - Built-in connection pooling and caching 

   - Branching capabilities for development/testing 

## **2.4 Scalability & Maintainability Considerations** 

- **Horizontal Scalability:** All services are **stateless** , allowing AKS to spin up additional pods during high-traffic periods (like A/L exam seasons). 

- **Independent Scaling:** Resources can be allocated specifically to high-load services like "Content Streaming" without over-provisioning the "User Service". 

- **CI/CD Maintainability:** Automated pipelines in **Azure DevOps** allow for continuous testing and "blue-green" or "canary" deployments to minimize downtime. 

- **Observability:** Centralized logging and monitoring via **Azure Monitor** provide real-time health metrics for all microservices. 

32 

## **CHAPTER 3 DATABASE DESIGN** 

## **3.1 Database Architecture Overview** 

The EDURA system employs a **database-per-service pattern** where each microservice maintains its own dedicated database schema. This approach ensures data isolation, independent scaling, and service autonomy. PostgreSQL Neon is utilized as the database management system across all services due to its serverless architecture, automatic scaling capabilities, and PostgreSQL compatibility. 

## **3.2 Entity-Relationship Diagram** 

_Figure 46: Entity - Relationship Diagram_ 

## **3.3 Database Normalization Strategy** 

All database schemas are designed following **Third Normal Form (3NF)** principles [1] to ensure: 

- **Data integrity** : Elimination of redundancy and update anomalies 

- **Consistency** : Single source of truth for each data element 

- **Efficiency** : Optimized storage and query performance 

- **Maintainability** : Easier schema evolution and updates 

33 

## **Normalization Process:** 

1. **First Normal Form (1NF)** : All tables have atomic values and no repeating groups 

2. **Second Normal Form (2NF)** : All non-key attributes are fully functionally dependent on the primary key 

3. **Third Normal Form (3NF)** : All non-key attributes are independent of other nonkey attributes 

## **Denormalization Considerations:** 

Strategic denormalization is applied in specific cases for read-heavy operations: 

- Analytics aggregations stored in materialized views 

- Cached student progress summaries for dashboard performance 

- Composite user information in session cache (Redis) 

34 

## **CHAPTER 4 CLASS DIAGRAM** 

## **4.1 Class Diagram Overview** 

The EDURA system follows object-oriented design principles with clear separation of concerns through layered architecture. Each microservice implements its own class structure following Domain-Driven Design (DDD) patterns [2]. 

## **4.2 Class Diagram** 

_Figure 47: Class Diagram_ 

35 

## **CHAPTER 5 SEQUENCE DIAGRAMS** 

## **5.1 Sequence Diagram Overview** 

Sequence diagrams illustrate the temporal ordering of interactions between system components for specific use cases. The following sequence diagrams are required to be created for the EDURA system. 

## **5.2 Sequence Diagrams** 

## 5.2.1 User Authentication and Login Flow 

_Figure 48: User Authentication and Login Flow Diagram_ 

36 

## 5.2.2 Course Creation and Publishing Flow 

_Figure 49: Course Creation and Publishing Flow Diagram_ 

37 

## 5.2.3 Student Enrollment and Payment Processing Flow 

## _Figure 50: Student Enrollment and Payment Processing Flow Diagram_ 

38 

## 5.2.4 Assessment Taking and Automated Grading Flow 

**==> picture [342 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure 51: Assessment Taking and Automated Grading Flow Diagram<br>**----- End of picture text -----**<br>


39 

## 5.2.5 Progress Tracking and Certificate Generation Flow 

## _Figure 52: Progress Tracking and Certificate Generation Flow Diagram_ 

40 

## 5.2.6 Analytics Report Generation Flow 

## _Figure 53: Analytics Report Generation Flow Diagram_ 

41 

## 5.2.7 AI Assistant Interaction Flow 

_Figure 54: AI Assistant Interaction Flow Diagram_ 

42 

## 5.2.8 Content Streaming Flow 

_Figure 55: Content Streaming Flow_ 

43 

## **CHAPTER 6 UI/UX DESIGN** 

## **6.1 Wireframes for Key User Interfaces** 

## 6.1.1 Authentication Interfaces 

## _Figure 56: User Sign-in Interface_ 

## _Figure 57: User Sign-up Interface_ 

44 

## 6.1.2 Student Dashboard 

_Figure 58: Student Dashboard Interface_ 

## 6.1.3 Course Catalog/Browse Interface 

_Figure 59: Course Catalog Interface_ 

45 

## 6.1.4 Course Content Viewer 

_Figure 60: High-level Course Content Viewer Interface_ 

_Figure 61: Expanded Course Content Viewer Interface_ 

46 

## 6.1.5 Assessment Interface 

_Figure 62: Assessment Interface_ 

## 6.1.6 Progress and Analytics Dashboard 

_Figure 63: Statistical Dashboard View_ 

47 

_Figure 64: Graphical Dashboard View_ 

## 6.1.7 Admin Dashboard 

_Figure 65: Admin Dashboard Interface_ 

48 

## 6.1.8 Profile and Settings 

_Figure 66: User Profile Interface_ 

49 

## **6.2 User Flow Diagrams** 

## 1. Student Registration and Onboarding Flow 

_Figure 67: Student Registration and Onboarding Flow_ 

50 

## 2. Course Enrollment Flow 

_Figure 68: Course Enrollment Flow_ 

51 

## 3. Learning Path Flow 

_Figure 69: Learning Path Flow_ 

52 

## 4. Assessment Flow 

_Figure 70: Assessment Flow_ 

53 

## 5. Teacher Course Creation Flow 

_Figure 71: Teacher Course Creation Flow_ 

54 

## 6. Admin Payment Verification Flow 

_Figure 72: Admin Payment Verification Flow_ 

55 

## **6.3 Accessibility Considerations (WCAG 2.1 Level AA)** 

## **Perceivable:** 

- All images have alt text 

- Videos have captions and transcripts 

- Color is not the only means of conveying information 

- Text contrast ratio of at least 4.5:1 

- Resizable text up to 200% without loss of functionality 

## **Operable:** 

- All functionality available via keyboard 

- No keyboard traps 

- Skip navigation links 

- Clearly visible focus indicators 

- Sufficient time for timed assessments with extension option 

- Pause, stop, hide options for auto-updating content 

## **Understandable:** 

- Clear and consistent navigation 

- Error identification and suggestions 

- Form labels and instructions 

- Predictable behavior 

- Help documentation available 

## **Robust:** 

- Valid HTML semantic markup 

- ARIA labels and roles where appropriate 

- Compatible with assistive technologies 

- Tested with screen readers (NVDA, JAWS) 

56 

## **CHAPTER 7 SECURITY DESIGN** 

## **7.1 Security Architecture Overview** 

The EDURA platform implements a comprehensive, defense-in-depth security strategy across all layers of the application stack. Security is integrated into every component through authentication, authorization, encryption, input validation, and continuous monitoring. 

## **7.2 Authentication Mechanism** 

- 7.2.1 Identity Provider Integration (Asgardeo) 

## **Asgardeo Integration:** 

- Asgardeo serves as the centralized Identity and Access Management (IAM) solution 

- OAuth 2.0 [3] and OpenID Connect (OIDC) [4] protocols for authentication 

- Support for multi-factor authentication (MFA) 

- Centralized user identity management 

- Single Sign-On (SSO) capabilities for future expansion 

## **Authentication Flow:** 

1. User submits credentials to EDURA frontend 

2. Frontend initiates OAuth 2.0 authorization code flow with Asgardeo 

3. Asgardeo validates credentials against its user directory 

4. Upon successful authentication, Asgardeo issues authorization code 

5. Backend exchanges authorization code for access token and refresh token 

6. Access token used for subsequent API requests 

7. Refresh token used to obtain new access tokens upon expiry 

57 

_Figure 73: Authentication Flow_ 

58 

## 7.2.2 Token Management 

## **JSON Web Tokens (JWT):** 

- Access tokens issued as JWTs [5] 

- Token structure: 

   - Header: Algorithm (RS256), Token type 

   - Payload: User ID, Role, Permissions, Issued At, Expiration 

   - Signature: Cryptographic signature using Asgardeo's private key 

- Token expiration: 15 minutes for access tokens 

- Refresh token expiration: 7 days 

- Tokens stored securely: 

   - Access tokens: HttpOnly, Secure cookies or memory (frontend) 

   - Refresh tokens: HttpOnly, Secure cookies with SameSite=Strict 

## **Token Validation:** 

- API Gateway validates JWT signature using Asgardeo's public key 

- Token expiration checked on every request 

- Token blacklisting implemented for logged-out sessions (Redis) 

- Refresh token rotation on each use to prevent replay attacks 

## 7.2.3 Session Management 

## **Session Storage:** 

- Session data stored in Redis with encryption 

- Session ID mapped to user context (user_id, role, permissions) 

- Session timeout: 30 minutes of inactivity 

- Concurrent session limit: 3 active sessions per user 

## **Session Security:** 

- Session IDs generated using cryptographically secure random number generator 

59 

- Session fixation prevention through ID regeneration after login 

- Session hijacking prevention through IP address and user-agent validation (optional strict mode) 

## 7.2.4 Email Verification and OTP 

## **Registration Flow:** 

- Email verification required before account activation 

- Time-limited OTP sent to registered email address 

- OTP validity: 10 minutes 

- OTP format: 6-digit numeric code 

- Maximum OTP generation attempts: 3 per hour 

- Email verification link includes signed token for additional security 

60 

_Figure 74: Registration Flow_ 

61 

## **Password Reset Flow:** 

- Password reset initiated via email 

- OTP sent for identity verification 

- OTP + email combination required to proceed 

- Password reset token valid for 1 hour 

- Single-use tokens invalidated after password reset 

62 

_Figure 75: Password Reset Flow_ 

63 

## **7.3 Authorization Levels** 

## 7.3.1 Role-Based Access Control (RBAC) 

## **Defined Roles:** 

## **Student Role:** 

- Permissions: 

   - View enrolled courses 

   - Access course content (videos, documents) 

   - Take assessments 

   - View own progress and certificates 

   - Upload payment receipts 

   - Interact with AI assistant 

   - Update own profile 

- Restrictions: 

   - Cannot create or modify courses 

   - Cannot access other students' data 

   - Cannot approve payments 

   - Cannot access admin functions 

## **Teacher Role:** 

- Permissions: 

   - All student permissions (for enrolled courses) 

   - Create, update, delete own courses 

   - Create and manage assessments 

   - Upload course content 

   - View enrolled students' progress in own courses 

   - Generate reports for own courses 

64 

   - Respond to student queries 

- Restrictions: 

   - Cannot access other teachers' courses (unless explicitly shared) 

   - Cannot approve payments 

   - Cannot manage users 

   - Cannot access system-wide analytics 

## **Administrator Role:** 

- Permissions: 

   - All teacher permissions 

   - Manage all users (create, update, deactivate, delete) 

   - Manage all courses regardless of creator 

   - Approve/reject manual payment receipts 

   - Access system-wide analytics and reports 

   - Configure system settings 

   - Manage roles and permissions 

   - View audit logs 

   - Access all data across the platform 

- Restrictions: 

`o` No restrictions (full system access) 

## 7.3.2 Permission Enforcement 

## **API Level Authorization:** 

- Every API endpoint protected by authorization middleware 

- JWT payload contains user role and permissions 

- Middleware validates required permissions before processing request 

- Unauthorized requests return 403 Forbidden response 

65 

## **Data Level Authorization:** 

- Row-level security implemented in database queries 

- Users can only access data they own or have permission to view 

- Example: Student can only view their own enrollment records 

- Example: Teacher can only modify their own courses 

## **Resource Ownership Validation:** 

- Object ownership checked before modification operations 

- Example: User can only update their own profile 

- Example: Teacher can only delete their own course content 

## **7.4 Data Protection Approach** 

## 7.4.1 Data Classification 

## **Sensitive Data:** 

- User credentials (passwords, tokens) 

- Personal identifiable information (PII): Names, email, contact numbers, date of birth 

- Payment information: Card details (handled by PayHere, not stored), transaction records 

- Assessment answers and scores 

## **Confidential Data:** 

- Course content (proprietary to instructors) 

- Student progress and performance data 

- System configuration and credentials 

## **Public Data:** 

- Published course listings 

- Public user profiles (if applicable) 

- General platform information 

66 

## 7.4.2 Data Storage Security 

## **Database Encryption:** 

- Data at rest encryption using PostgreSQL Neon's built-in encryption 

- Database backups encrypted with AES-256 

- Encryption keys managed through cloud provider's key management service 

## **Field-Level Encryption:** 

- Sensitive fields encrypted individually: 

   - Payment receipt URLs 

   - Personal notes 

   - Assessment answers (before grading) 

- Encryption algorithm: AES-256-GCM 

- Encryption keys rotated quarterly 

## **Password Security:** 

- Passwords never stored in plaintext 

- Hashing algorithm: bcrypt with salt 

- Work factor: 12 rounds 

- Password complexity requirements enforced: 

   - Minimum 8 characters 

   - At least one uppercase letter 

   - At least one lowercase letter 

   - At least one number 

   - At least one special character 

7.4.3 Data Transmission Security 

## **Transport Layer Security (TLS):** 

- All communication over HTTPS 

67 

- TLS version: 1.2 minimum, 1.3 recommended 

- Strong cipher suites enforced 

- Certificate validation required 

- HTTP Strict Transport Security (HSTS) enabled 

## **API Security:** 

- All API requests require authentication token 

- Request/response payload encryption for sensitive data 

- API rate limiting to prevent abuse 

- CORS policy configured to allow only trusted origins 

## **File Uploads:** 

- File upload size limits enforced 

- File type validation (whitelist approach) 

- Virus scanning on uploaded files 

- Uploaded files stored in isolated storage (Cloudinary) 

- Access to uploaded files requires authentication 

## **7.5 Input Validation and Sanitization Strategy** 

- 7.5.1 Client-Side Validation 

## **Form Validation:** 

- Real-time validation feedback for user inputs 

- Type checking (email format, numeric values, date formats) 

- Length constraints (minimum/maximum characters) 

- Required field validation 

- Custom validators for complex fields (e.g., strong password check) 

## **JavaScript Validation:** 

- Input sanitization before display to prevent XSS 

68 

- HTML encoding of user-generated content 

- Removal of potentially malicious scripts 

**Note:** Client-side validation is for user experience only; all validation is re-enforced serverside. 

## 7.5.2 Server-Side Validation 

## **Input Validation:** 

- All inputs validated against expected data types and formats 

- Length constraints enforced 

- Range validation for numeric inputs 

- Whitelist validation for enumerated values 

- Regular expression validation for patterns (email, phone, etc.) 

## **SQL Injection Prevention [6]:** 

- Parameterized queries used for all database operations 

- ORM (SQLAlchemy) used to abstract database interactions 

- No dynamic SQL query construction with user input 

- Stored procedures used where appropriate 

## **NoSQL Injection Prevention:** 

- Input sanitization before MongoDB queries (if used) 

- Type validation to ensure expected data types 

- Avoid direct user input in query operators 

## **Cross-Site Scripting (XSS) Prevention [6]:** 

- All user-generated content escaped before rendering 

- Content Security Policy (CSP) headers implemented 

- HttpOnly and Secure flags on cookies 

- Sanitization library (e.g., Bleach for Python) used for HTML content 

69 

## **Cross-Site Request Forgery (CSRF) Prevention:** 

- CSRF tokens required for all state-changing operations 

- Token validation on server side 

- SameSite cookie attribute set to prevent CSRF 

- Double-submit cookie pattern for additional protection 

## **Command Injection Prevention:** 

- Avoid executing system commands with user input 

- If necessary, strict whitelisting and escaping 

- Use library functions instead of shell commands where possible 

## 7.5.3 File Upload Validation 

## **File Type Validation:** 

- MIME type checking 

- File extension whitelist (PDF, DOCX, PNG, JPG, MP4, etc.) 

- Magic number validation to prevent extension spoofing 

- Content scanning for malicious code 

## **File Size Limits:** 

- Video files: Maximum 500MB 

- Documents: Maximum 25MB 

- Images: Maximum 5MB 

- Receipt images: Maximum 2MB 

## **Upload Security:** 

- Files uploaded to isolated storage (Cloudinary) 

- Original filenames sanitized 

- Unique identifiers assigned to uploaded files 

- Virus/malware scanning before storage 

70 

- Access to files controlled through signed URLs 

## **7.6 Encryption Standards** 

## 7.6.1 Data at Rest Encryption 

## **Database Encryption:** 

- PostgreSQL Neon transparent data encryption (TDE) 

- Encryption algorithm: AES-256 

- Encryption keys managed by cloud provider's KMS 

## **File Storage Encryption:** 

- Cloudinary storage encryption enabled 

- Encryption at storage provider level 

- Access controlled through IAM policies 

## **Backup Encryption:** 

   - All database backups encrypted using AES-256 

   - Backup encryption keys separate from production keys 

   - Encrypted backups stored in geographically distributed locations 

- 7.6.2 Data in Transit Encryption 

## **TLS Configuration:** 

- TLS 1.2 minimum version 

- TLS 1.3 preferred 

- Strong cipher suites: 

   - TLS_AES_256_GCM_SHA384 

   - TLS_CHACHA20_POLY1305_SHA256 

   - TLS_AES_128_GCM_SHA256 

- Weak ciphers disabled (RC4, DES, MD5) 

- Perfect Forward Secrecy (PFS) enabled 

71 

## **Certificate Management:** 

- SSL/TLS certificates from trusted Certificate Authority 

- Wildcard or multi-domain certificates for subdomains 

- Automated certificate renewal (e.g., Let's Encrypt) 

- Certificate pinning for mobile applications (future) 

## **Inter-Service Communication:** 

   - Microservices communicate over internal network 

   - Mutual TLS (mTLS) for service-to-service authentication 

   - API Gateway enforces TLS for all external traffic 

- 7.6.3 Encryption Key Management 

## **Key Storage:** 

- Encryption keys stored in Azure Key Vault 

- Keys never hardcoded in application code 

- Environment variables used for key references 

- Principle of least privilege for key access 

## **Key Rotation:** 

- Encryption keys rotated quarterly 

- Automated key rotation process 

- Old keys retained for decryption of existing data 

- Re-encryption of data with new keys scheduled 

## **Key Hierarchy:** 

- Master keys for encrypting data encryption keys (DEKs) 

- Data encryption keys for actual data encryption 

- Separate keys for different data classifications 

72 

## **CHAPTER 8 DEPLOYMENT DESIGN** 

## **8.1 Hosting Plan & Infrastructure** 

The platform is hosted on **Microsoft Azure** , utilizing a mix of PaaS (Platform as a Service) and IaaS (Infrastructure as a Service) to manage the microservices. 

- **Azure Kubernetes Service (AKS):** Orchestrates all microservice containers, providing auto-scaling and self-healing capabilities. 

- **PostgreSQL Neon:** A serverless, managed database that scales compute resources independently of storage. 

- **Azure Cache for Redis:** Provides a managed high-performance data store for session management and caching. 

- **Cloudinary:** Serves as the external Media-as-a-Service provider for video streaming and CDN delivery. 

## **8.2 Hardware & Resource Requirements** 

Since the infrastructure is cloud-based, "hardware" refers to the virtual machine (VM) specifications allocated within Azure node pools. 

_Table 18: Hardware and Resource Requirements_ 

|**Component**|**Azure VM Size**|**vCPUs**|**RAM**|**Role**|
|---|---|---|---|---|
|Frontend Nodes|Standard_D4s_v3|4|16 GB|Next.js App hosting|
|Backend Nodes|Standard_D8s_v3|8|32 GB|Microservice containers|
|Data Processing|Standard_E4s_v3|4|32 GB|Analytics & Reports|
|Database (Neon)|Serverless|2-4|8-16 GB|Auto-scaling compute|



73 

**8.3 Network Diagram** 

- ee > 

_Figure 76: Network diagram_ 

74 

## **8.4 Environment Specifications** 

The deployment is split across three distinct environments to maintain code quality and stability. 

- **Development:** A minimal AKS cluster used for active feature integration; it uses a shared database and single-instance Redis. 

- **Staging:** A production-mirror environment used for **User Acceptance Testing (UAT)** and performance benchmarking; it uses anonymized copies of production data. 

- **Production:** A high-availability setup with multi-zone redundancy, geo-replicated backups, and a **99.9% uptime SLA** . 

## **8.5 CI/CD Pipeline Overview** 

EDURA uses **Azure DevOps** to automate the path from code commit to production deployment. 

- **Continuous Integration (CI):** On every commit, the pipeline runs linting (Pylint/ESLint), unit tests (pytest/Jest), and security scans (Snyk/Trivy) before building and pushing Docker images to the **Azure Container Registry (ACR)** . 

- **Continuous Deployment (CD):** * **Staging:** Deployments are triggered automatically upon a merge to the staging branch. 

   - **Production:** Requires manual approval and utilizes a **Canary Deployment** strategy, where traffic is gradually shifted to the new version while monitoring for errors. 

75 

## **CHAPTER 9 REFERENCES** 

[1] E. F. Codd, "A relational model of data for large shared data banks," _Commun. ACM_ , vol. 13, no. 6, pp. 377–387, Jun. 1970. 

[2] E. Evans, _Domain-Driven Design: Tackling Complexity in the Heart of Software_ . Boston, MA, USA: Addison-Wesley, 2003. 

[3] D. Hardt, Ed., "The OAuth 2.0 Authorization Framework," IETF, RFC 6749, Oct. 2012. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc6749 

[4] N. Sakimura, J. Bradley, M. Jones, B. de Medeiros, and C. Mortimore, "OpenID Connect Core 1.0 incorporating errata set 1," OpenID Foundation, Nov. 2014. [Online]. Available: https://openid.net/specs/openid-connect-core-1_0.html 

[5] M. Jones, J. Bradley, and N. Sakimura, "JSON Web Token (JWT)," IETF, RFC 7519, May 2015. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc7519 

[6] OWASP Foundation, "OWASP Application Security Verification Standard (ASVS)," - - - - version 4.0, 2019. [Online]. Available: https://owasp.org/www project application security verification-standard/ 

76 

## **PROOFREADING CERTIFICATION** 

## **SENG 31242 – System Design Project** 

**EDURA –** I hereby certify that I have proofread the final draft of the project report titled **Learning Management System** submitted by the following students and confirm that it is free of grammatical and spelling errors to the best of my knowledge. 

## **Group Members:** 

**Student Name Student No** W.G.N.DANANJAYA SE/2021/047 R.W.V.I.D.RAJAPAKSHA SE/2021/019 P.D.D.RANSIKA SE/2021/034 H.T.MADUSHANKA SE/2021/011 

## **Certifier Details:** 

Name of Certifier - ……………………………………… 

Designation – …………………………………………… 

Signature - ………………………………………… 

Date - ………………………………………… 

56 

