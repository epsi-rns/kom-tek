Polynomial
----------

slug: ai-assisted-predictive-model

-- -- --

# A. Project Title

AI-Assisted Sensor Predictive Models Using Polynomial Regression

## Note on Language Choice:

This report is intentionally written in English to reach a broader audience beyond the local context. Writing in English allows international readers and foreign students to follow the technical discussion without needing to translate concepts, and encourages clear, precise communication of engineering ideas.

-- -- --

# B. Author Complete Name

Epsiarto Rizqi Nurwijayadi

-- -- --

# C. Affiliation

Department of Mechanical Engineering, Faculty of Engineering, Universitas Indonesia.

-- -- --

# D. Abstract (short)

This project develops predictive models for sensor calibration using polynomial regression for two engineering cases: **fuel level (fuel stick)** and **axle load**. The workflow is organized into three stages: building smooth predictive models, refining them into practical Python scripts, and implementing an AI assistant to generate and validate scripts automatically. Guided by computational thinking, the process integrates numerical methods, practical coding, and AI tools into a coherent solution. Key findings include the reliability of polynomial regression, usability of Python scripts, and potential of AI assistance to automate repetitive tasks while enforcing scripting rules. Challenges remain in embedding knowledge and rules within AI context windows and handling unpredictable environments. This project demonstrates a systematic, reproducible approach for sensor calibration, highlighting areas for future work in formalizing AI-assisted rule management and improving robustness for broader deployment.

-- -- --

# D. Abstract (long)

This project develops sensor predictive models using polynomial regression for two engineering cases: **fuel level (fuel stick)** and **axle load**. The work is organized into three stages: **Stage I** builds smooth predictive models, **Stage II** refines them into practical Python scripts for daily use, and **Stage III** implements an AI assistant to generate and validate these scripts automatically. The entire workflow is guided by **computational thinking**, demonstrating how numerical methods, engineering calibration tasks, and AI tools can be integrated into a coherent, real-world solution.

Key findings include the reliability and accuracy of polynomial regression models for real-world sensor data, the usability of Python scripts in routine calibration, and the potential of AI assistance to automate repetitive tasks while enforcing scripting rules. Challenges were identified in embedding knowledge and rules within AI context windows and handling unpredictable environmental factors, particularly in shared AI server setups.

In conclusion, this project demonstrates a systematic approach that combines **numerical methods, practical coding, and AI-assisted automation** under computational thinking, providing a reproducible methodology for sensor calibration. While the AI assistant shows promise for efficiency and flexibility, further work is needed to formalize rule management and extend robustness for broader deployment.

-- -- --

# E. Author Declaration

## I. Deep Awareness (of) I

I live in this world **guided by a higher purpose**, entrusted with the responsibility to act with integrity, diligence, and ethical awareness, contributing positively without becoming a burden to others. To fulfill this trust, I must cultivate mastery in my work and knowledge.

**As a human being** (employee and also students), I strive for personal growth. Moving from skills (execution) to competency (exploration), and further to capability (deep assimilation). Learning is not just understanding how things work, but applying problem-solving in daily practice and continuously reflecting to improve. This project serves as a tool to develop my cognitive capability and capacity through practice and reflection.

## II. Intention of the Project Activity

This project develops predictive models for fuel level and axle load sensors using polynomial regression, combining numerical methods with Python implementation. All aspects, from model development to script refinement and AI-assisted automation, are approached under the computational thinking framework, ensuring systematic problem-solving, flexibility, and practical applicability in sensor calibration.

The aim is not only technical accuracy but also responsible and ethical practice. Respecting data privacy, ensuring reproducibility, supporting peers fairly, and contributing solutions that are practical without creating unnecessary burden for others. By integrating AI-assisted workflows, the project reduces reliance on specialized operators, enabling sustainable, error-resistant sensor calibration and minimizing the need for continuous human intervention.

-- -- --

# F. Introduction

Sensors are critical components in modern engineering systems, providing essential measurements that guide operational decisions in industries such as automotive, energy, and manufacturing. Despite their importance, challenges remain in accurately interpreting sensor outputs, calibrating nonlinear responses, and ensuring reliable predictions under varying conditions.

## III. Initial Thinking (of the Problem)

### Systematic Problem Analysis

Sensor calibration is critical for reliable engineering operations, yet it presents several challenges. Nonlinear sensor responses, measurement noise, and limited calibration data can lead to inaccurate predictions, operational inefficiencies, and increased reliance on specialized personnel. Ensuring smooth, accurate predictions that can be applied in daily workflows is essential to maintain system reliability and reduce human error.

### Problem Decomposition

The general challenge of sensor calibration can be broken down into three practical tasks:

* **Predictive Modeling**: Representing nonlinear sensor responses using polynomial regression to generate stable and accurate predictions.

* **Coding Refinement**: Developing robust and reusable Python scripts for routine calibration tasks, reducing the dependency on specialized operators.

* **AI Assistance**: Automating script generation, adaptation, and validation to enforce workflow rules, handle dataset variability, and minimize repetitive manual work.

[image]

By framing AI assistance as a practical solution to recurring challenges—such as repetition, rule enforcement, and error handling—its relevance to the engineering problem is clear.

### Deconstruction to Fundamental Principles

Addressing these tasks relies on principles from numerical methods, algorithm design, and data handling. Polynomial regression forms the mathematical foundation, while careful dataset management ensures reliability, stability, and reproducibility. Root causes of calibration difficulties: sensor nonlinearity, limited data, and reliance on specialized skills, are explicitly targeted by this workflow.

### Contextual Analysis and State-of-the-Art

Calibration datasets typically cover multiple operating conditions for sensors such as fuel level indicators and axle load measurements. Polynomial regression and Python-based implementation are well-established in these contexts. What remains rare is **AI-assisted automation of script generation and validation**, especially within a flexible, rule-guided framework. This project focuses on practical implementation to streamline calibration workflows while maintaining reproducibility, adaptability, and usability under variable datasets.

-- -- --

# G. Methods and Procedures

## IV. Idealization

The project develops a **simplified yet realistic sensor calibration model**, guided by polynomial regression and numerical methods, underpinned by the principles of computational thinking. Key assumptions include:

* **Stable sensor behavior** during measurement,
* **Negligible** noise after standard preprocessing, and
* **Sufficient calibration points** for robust polynomial fitting.

These assumptions are standard in numerical modeling and sensor calibration practice, ensuring **physical realism** and alignment with operational constraints. They are explicitly stated to maintain transparency and clarity in the modeling process, reflecting **conscious awareness of the design intent** (DAI5: Deep Awareness and Intention).

[image]

Even if the formula looks analytical, the coefficients are computed numerically.

[image]

The polynomial regression model and its **Python implementation are already reliable and proven in field applications**. The primary innovation and complexity lie in **automating script generation and validation using AI assistance**, which requires iterative testing, rule enforcement, and adaptability to variable datasets. This aspect demonstrates **creativity, innovation, and alignment with higher objectives**, producing practical solutions that reduce manual workload and enhance reproducibility without unnecessary reliance on specialized operators.

The idealized workflow emphasizes **simplicity, scalability, and elegance**, allowing extension to different sensor types or operational contexts. It embodies **continuous reflection and refinement** (DAI5: Integration & Critical Reflection), ensuring that the project’s computational solutions remain ethically responsible, practically relevant, and aligned with overarching engineering and societal goals.

## V. Instruction (Set)

Outline the step-by-step workflow for the project at a high level:

1. **Define objectives**: select sensors (fuel stick, axle load), desired prediction accuracy, and operational constraints.

2. **Preprocess and analyze data**: clean, normalize, and assess sensor data for stable regression modeling.

3. **Develop predictive models**: apply polynomial regression to approximate sensor-to-true-value relationships, selecting appropriate polynomial degree and solver.

4. **Refine implementation**: create maintainable Python scripts suitable for routine calibration tasks, ensuring all code and parameters are clearly documented for reproducibility.

5. **Integrate AI assistance**: implement an AI assistant to generate, adapt, and validate scripts. This step requires iterative handling, as the AI must navigate embedded rules, dataset variations, and unexpected issues (pop-ups, edge cases). By automating repetitive tasks, this approach reduces reliance on specialized operators, promoting sustainable and efficient workflow practices.

6. **Validate AI workflow**: focus iterations on AI-assisted testing and refinement, rather than the underlying polynomial model or Python code, which are already stable.

Highlight the **iterative nature** of the AI-assisted workflow: rule enforcement, script validation, error handling, and adaptation are repeated until objectives are met, ensuring reliable automation without unnecessary repetition of already-settled tasks. All iterations, rules, and observations are thoroughly documented to maintain transparency, reproducibility, and knowledge sharing.

-- -- --

# H. Results and Discussion

This project demonstrates the use of polynomial regression models for fuel level and axle load sensors, refined in Python and supported by an AI assistant using RAG knowledge. The AI workflow presents unique challenges and insights:

## Performance Metrics

* Focused on polynomial coefficients to isolate and observe AI behavior with an atomic set of scripting objectives.

* Two qualitative measures were defined:
  1. How well the AI obeys the scripting template.
  2. How flexible the AI is when facing dataset variability.

* The hardest parts of implementation were creating **reliable knowledge** and **embedding rules** within the AI's limited context window, followed by handling **unpredictable environmental challenges**.

## Comparison with Traditional Approaches

* Traditional calibration relies on manual scripting and regression updates, which are slow but predictable. This require operator with python scripting skill.

* The AI-assisted workflow reduces human intervention but requires intensive rule tweaking and remains limited to pre-defined templates.

## Insights and Practical Implications

* AI assistance shows significant potential, offering a lower-cost solution for home or small-scale industrial use.

* Proper integration and safe deployment are not yet established; the system is **not ready for production** and should be used cautiously.

This project demonstrates the practical application of AI for automating repetitive tasks and highlights areas for future research in AI-assisted calibration.

## Limitations

* The AI assistant performed well in a **clean local environment**.

* Performance failed on shared AI servers due to RAG knowledge contamination, illustrating the sensitivity of the approach to environmental factors.

* The scope was deliberately limited to polynomial coefficients; broader statistical properties were excluded to maintain focus on AI behavior.

-- -- --

# I. Conclusion, Closing Remarks, Recommendations

This project demonstrates a structured workflow for sensor predictive modeling using polynomial regression, Python implementation, and AI-assisted script generation, guided throughout by **computational thinking principles**: decomposition, pattern recognition, abstraction, and algorithm design. The integration of these principles enabled the development of reliable predictive models, practical Python scripts, and a functional AI assistant capable of following scripting rules and adapting to dataset variability.

## Key contributions include:

Providing a clear methodology for applying polynomial regression to real-world sensor calibration tasks.

Demonstrating the potential of AI assistance to automate repetitive tasks, enforce rules, and improve efficiency, while highlighting current limitations in shared or unpredictable environments.

For **future work**, formalizing AI-assisted rules and improving RAG knowledge management could enhance reliability and flexibility, enabling wider applicability in both industrial and small-scale settings. The project shows that combining numerical methods, practical implementation, and AI tools under computational thinking provides a systematic and replicable approach for sensor calibration and automation.

-- -- --

# J. Acknowledgments

I would like to express my gratitude to all who indirectly supported this work, including mentors, educators, and peers whose guidance, discussions, and encouragement provided motivation throughout the project. While this work is largely independent, the insights and inspiration drawn from the broader academic and technical community were invaluable in shaping the methodology and outcomes presented here.

-- -- --

# K. References

Epsi. (2020, March 1). Trend overview [Blog post]. Retrieved from https://epsi.bitbucket.io/statistics/2020/03/01/trend-overview/

Epsi. (n.d.). Python code for trend analysis. GitHub repository. Retrieved from https://github.com/epsi-rns/codecase/tree/master/python/trend

Wikipedia contributors. (n.d.). Vandermonde matrix. In Wikipedia. Retrieved December 10, 2025, from https://en.wikipedia.org/wiki/Vandermonde_matrix

-- -- --

# L. Appendix

This section includes detailed calculations, simulation data, diagrams, and additional charts that support the main text:

* Polynomial Regression Coefficients: Full tables of fitted coefficients for fuel stick and axle load sensors.

* Python Script Snapshots: Selected code snippets demonstrating key steps in preprocessing, regression modeling, and AI-assisted automation.

* AI Workflow Diagrams: Flowcharts illustrating AI knowledge embedding, rule enforcement, and iterative testing procedures.

* Calibration Data Visualizations: Graphs showing sensor readings, predicted values, residuals, and error distributions.

* Supplementary Notes: Any additional calculations, assumptions, or observations relevant to reproducibility and verification.

Note: All diagrams and tables are numbered (e.g., Table L1, Figure L1) and referenced in the main text as needed.

-- -- --

