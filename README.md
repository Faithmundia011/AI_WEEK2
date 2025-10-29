**# 🌍 AI for Sustainable Development – SDG 6: Clean Water

### 🧠 *K-Means Clustering for Water Pollution Analysis*

---

## **1. Project Overview**

This project applies **Machine Learning (ML)** to support the **United Nations Sustainable Development Goal 6 (Clean Water and Sanitation)**.
It uses **K-Means Clustering (Unsupervised Learning)** to analyze water quality data and group regions according to their pollution levels.

The system helps environmental agencies and policymakers identify **pollution hotspots**, prioritize interventions, and promote **sustainable water management**.

---

## **2. Objectives**

* Analyze and cluster water quality data using K-Means algorithm.
* Identify regions with **clean**, **moderately polluted**, and **highly polluted** water sources.
* Support **data-driven decision-making** for clean water initiatives.
* Demonstrate how AI contributes to achieving **SDG 6**.

---

## **3. Dataset**

* **Source:** [Kaggle / Open Source Dataset](https://raw.githubusercontent.com/dphi-official/Datasets/master/water_quality.csv)
* **Description:** Contains chemical and physical properties of water samples such as:

  * pH
  * Hardness
  * Solids
  * Chloramines
  * Sulfate
  * Conductivity
  * Organic Carbon
  * Trihalomethanes
  * Turbidity

Each feature contributes to assessing overall water quality and pollution risk.

---

## **4. Tools and Libraries**

| Tool / Library           | Purpose                          |
| ------------------------ | -------------------------------- |
| **Python 3.x**           | Programming language             |
| **Pandas**               | Data handling and cleaning       |
| **NumPy**                | Numerical computations           |
| **Matplotlib / Seaborn** | Data visualization               |
| **Scikit-learn**         | ML model training and clustering |
| **Jupyter Notebook**     | Running the code interactively   |

---

## **5. Model Workflow**

1. **Data Loading:** Load dataset from online source (CSV file).
2. **Data Preprocessing:** Clean missing values and normalize features.
3. **K-Means Clustering:** Group data into clusters based on pollution patterns.
4. **Evaluation:** Use the **Silhouette Score** to measure clustering performance.
5. **Visualization:** Plot clusters using Seaborn to show how water regions differ by pH and turbidity.
6. **Interpretation:** Analyze which clusters correspond to higher pollution levels.

---

## **6. Results**

* The **Elbow Method** identified **3 optimal clusters**.
* Each cluster represents a different pollution level:

  * Cluster 0 → Clean water regions
  * Cluster 1 → Moderate pollution
  * Cluster 2 → High pollution

**Silhouette Score Example:** `0.64`
(A higher score indicates clearer, well-separated clusters.)

**Cluster Summary Output Example:**

```
Cluster Characteristics:
          ph  Hardness   Solids  Turbidity
Cluster
0       7.8     200.3   18000.5     3.4
1       6.5     150.7   12000.8     2.1
2       8.2     220.4   24000.9     5.8
```

---

## **7. Ethical Considerations**

* **Bias:** If data is collected unevenly (e.g., only urban areas), results may not represent rural water conditions.
* **Fairness:** Open datasets ensure transparency and inclusiveness.
* **Sustainability:** Enables proactive management of clean water resources.

---

## **8. Expected Impact**

✅ Early identification of unsafe water sources.
✅ Efficient allocation of sanitation resources.
✅ Data-driven insights to support SDG 6 and public health.
✅ Promotion of environmental awareness and sustainability.

---

## **9. How to Run the Code**

1. Clone or download this repository.
2. Install required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Run the Jupyter Notebook or Python script:

   ```bash
   jupyter notebook water_quality_analysis.ipynb
   ```

   or

   ```bash
   python water_quality_analysis.py
   ```

---

## **10. Author**

**Project By:** *[Faith]*
**Course:** *AI for Sustainable Development (Week 2)*
**Date:** *October 2025*

