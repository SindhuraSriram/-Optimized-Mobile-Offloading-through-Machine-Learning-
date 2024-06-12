# -Optimized-Mobile-Offloading-through-Machine-Learning

**Project Title:** A Machine Learning Based Approach for Computation Offloading in Mobile Edge Computing

**Authors:** S. Sindhura, V. Sindhu, R. Ezhilarasie  
**Affiliation:** School of Computing, SASTRA Deemed University, Thanjavur

**Abstract:**
This study explores the feasibility of using machine learning techniques to optimize computation offloading in Mobile Edge Computing (MEC). Mobile devices, despite technological advancements, remain resource-constrained. Offloading computations to nearby peer servers, which have better resources compared to local devices and are closer than cloud servers, can enhance performance. By considering constraints like execution time, CPU load, and bandwidth, a machine learning algorithm predicts whether computations should be done locally or offloaded to a peer server.

**Key Concepts:**
- **Offloading:** Transferring computational tasks from resource-limited mobile devices to more capable servers.
- **Peer Server:** An intermediary server with better resources than local devices but is closer and less congested than cloud servers.
- **Machine Learning:** Used to predict and decide where to execute tasks for optimal performance.
- **Constraints:** Key factors include Million Instructions Per Second (MIPS), bandwidth, execution time, cost, and power consumption.

**Methodology:**
1. **Time Efficient Model:** Uses MIPS and bandwidth to predict execution time and identify optimal configurations for minimal execution time.
2. **Energy Efficient Model:** Considers power consumption per unit time and execution time to find configurations that minimize energy use.
3. **Cost Efficient Model:** Calculates cost per unit time combined with execution time to determine the most cost-efficient configuration.

**Results:**
By leveraging machine learning, the study found that offloading computations to peer servers could significantly enhance resource utilization and performance, leading to reduced execution times, energy consumption, and costs.

**Conclusion:**
The proposed machine learning-based framework for computation offloading in MEC demonstrates improved performance and efficiency. Future work could include additional constraints for further optimization.

**Keywords:** Offloading, peer server, CPU load, machine learning, computation, cloud
