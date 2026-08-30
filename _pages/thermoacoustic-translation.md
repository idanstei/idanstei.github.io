---
layout: page
title: Translation Strategy
permalink: /thermoacoustic-translation/
description: "A technology and business analysis of thermoacoustic imaging through three clocks: technical capability, clinical economics, and adoption."
nav: true
nav_order: 4
og_image: /assets/img/taeus_clinical_workflow.png
---

My main [Thermoacoustics]({% link _pages/thermoacoustic-imaging.md %}) page focuses on the physics, clinical evidence, and longer-term potential of the modality.

This page asks a different question:

### What would have to happen for thermoacoustics to become a successful clinical technology and a sustainable business?

A useful way to think about emerging technologies is as **three clocks that do not necessarily advance at the same speed**:

| Clock | Core question |
| --- | --- |
| **Capability** | Can the technology reliably do something clinically valuable? |
| **Economics** | Does that information create enough value to justify the product, procedure, and business model? |
| **Adoption** | Can clinicians, hospitals, regulators, payers, and industry partners realistically incorporate it into practice? |

A technology can be scientifically impressive while still failing commercially if one of these clocks remains far behind the others.

**My current view is that thermoacoustics' capability clock is substantially ahead of its economics and adoption clocks.**

That is encouraging, because the fundamental question is no longer simply whether biological RF contrast exists. But it also means that the choice of the **first commercial application** may matter as much as the underlying imaging technology.

> **The best first application for a new imaging modality is not necessarily the one with the greatest scientific potential. It is the one in which technical capability, clinical economics, and adoption can mature together.**

*This is my personal technology and business analysis based on public information and published research as of August 2026. It does not represent the position of any employer or company.*

---

## Clock 1 — Capability

For many years the central question in thermoacoustics was whether useful RF-induced acoustic signals could be generated and reconstructed from biological tissue.

That question has increasingly been replaced by harder ones:

- Can the signal be quantitative rather than merely visible?
- Can it remain accurate across patients and body habitus?
- Can electromagnetic field variation be modeled or compensated?
- Can the system work with practical RF power, transducers, electronics, and acquisition times?
- Can the result answer a clinically meaningful question reproducibly?

There is now evidence at several levels.

In liver fat assessment, a prospective human feasibility study of 40 subjects reported a correlation of **r = 0.89** between Thermoacoustic Fat Fraction (TAFF) and MRI-PDFF, with a mean absolute error of **3.04 percentage points**. A separate repeatability and reproducibility study reported an ICC of **0.89**.[1]

Label-free thermoacoustic imaging of human forearm blood vessels has also been demonstrated in vivo, with vessels approximately **5.5 mm below the skin** recovered without an injected contrast agent.[2]

For microwave ablation, recent work has used a clinical-scale **2.45 GHz** microwave source and a 512-element acoustic detector to reconstruct thermoacoustic maps of deposited microwave energy with approximately **one-second temporal resolution** in ex vivo liver.[3]

At the molecular-imaging end of the spectrum, targeted hypertonic-saline nanodroplets have already enabled **in vivo RF-acoustic molecular imaging** in an animal model.[4]

These results do not mean that a general-purpose clinical thermoacoustic scanner is mature. They mean something more specific:

> **The modality has crossed the threshold from "interesting physics" to application-dependent translational engineering.**

For each application, the remaining capability questions are now different.

---

## Clock 2 — Economics

A technically successful imaging measurement is not automatically a valuable product.

The customer does not buy "thermoacoustics." The customer buys an answer:

- How much fat is in this liver?
- Did the ablation cover the entire tumor with an adequate margin?
- Is this tissue perfused?
- Is there blood where it should not be?
- Is a molecular target present?

The economic clock therefore depends on four things:

1. **How valuable is the clinical decision?**
2. **What does the customer use today?**
3. **Is thermoacoustics materially better, cheaper, faster, safer, or more accessible?**
4. **Who pays for the measurement?**

This distinction is especially important for liver fat.

MRI-PDFF is an excellent quantitative reference, but it is not the only competitor. FibroScan has an established point-of-care workflow and U.S. reimbursement infrastructure, including coding guidance around CPT 76981.[5] Conventional ultrasound is also moving rapidly toward quantitative liver-fat assessment. GE HealthCare's UGAP and newer UGFF approaches use attenuation and other quantitative ultrasound parameters, with UGAP evaluated in a multicenter cohort of more than 1,000 patients.[6]

Therefore, the business case for thermoacoustic liver fat cannot simply be:

**"It is cheaper and more accessible than MRI."**

It must become something closer to:

**"It provides a clinically important quantitative measurement that is sufficiently more accurate, robust, accessible, workflow-compatible, or useful for longitudinal monitoring than the alternatives available at the same point of care."**

That is a much higher bar — but it is also the right bar.

---

## Clock 3 — Adoption

Clinical adoption is its own engineering problem.

Even a technically superior and economically attractive technology can stall if it asks the healthcare system to change too much at once.

Adoption depends on issues such as:

- regulatory pathway and evidence requirements;
- reimbursement or inclusion within an already-paid procedure;
- physician training and confidence;
- acquisition time and workflow;
- compatibility with existing imaging systems;
- infection-control and patient-contact requirements;
- service and maintenance;
- integration into reporting and hospital IT;
- clinical guidelines and professional-society acceptance;
- and the amount of new capital equipment a customer must purchase.

This is one reason I believe **ultrasound integration is strategically important**.

Rather than asking a clinician to learn an entirely new imaging modality from scratch, a combined workflow can use:

**Ultrasound → anatomy, localization, and procedural guidance**

**Thermoacoustics → compositional, dielectric, vascular, or RF-energy information**

The closer thermoacoustics can attach itself to a workflow that already exists, the faster the adoption clock can move.

The same logic is even stronger for microwave ablation: the patient is already undergoing an image-guided procedure, a high-power microwave generator is already present, and the clinician already needs information about the treatment zone.

## The business is a chain of adoption decisions

For a new medical-imaging technology, there is rarely one customer and one decision. Several groups have to say yes, often for different reasons.

| Stakeholder | What they need to believe |
| --- | --- |
| **Clinician / operator** | The information is useful, trustworthy, and does not make the workflow harder |
| **Patient** | The examination or procedure is safe, tolerable, and provides meaningful benefit |
| **Department / hospital** | The system fits staffing, space, throughput, service, and capital constraints |
| **Payer / health system** | The measurement improves outcomes or reduces downstream cost enough to justify payment |
| **Regulator** | The claimed use is supported by appropriate safety and performance evidence |
| **Commercial partner / OEM** | The capability strengthens an existing platform or procedure enough to justify integration |
| **Investor / manufacturer** | The market is large enough, margins are credible, and the path to scale is financeable |

The product fails if any critical link in that chain remains unresolved. That is why the same underlying TA physics can produce very different commercial prospects in liver diagnostics, interventional oncology, vascular imaging, and molecular imaging.

---

## The application clocks are different

There is no single maturity level for "thermoacoustics." Each application has its own three clocks.

The scores below are **qualitative assessments**, not market-size estimates or clinical claims. A score of 5 means that the relevant clock is comparatively mature; a score of 1 means that it remains largely conceptual.

| Application | Capability | Economics | Adoption | Current business interpretation |
| --- | :---: | :---: | :---: | --- |
| **Fatty liver / MASLD** | **5/5** | **3/5** | **3/5** | Most technically de-risked TA application, but it must differentiate against FibroScan and quantitative ultrasound |
| **Microwave-ablation monitoring** | **3.5/5** | **4.5/5** | **4/5** | Potentially the strongest three-clock convergence because TA can attach directly to an existing RF therapy workflow |
| **Deep vascular / perfusion imaging** | **2.5/5** | **4/5 potential** | **2.5/5** | Large opportunity only if a specific deep-tissue problem is found where current vascular imaging is inadequate |
| **Burn depth / tissue viability** | **2/5** | **3.5/5** | **3/5** | Attractive point-of-care geometry and decision problem; application-specific TA validation remains early |
| **Intracranial hemorrhage** | **2/5** | **5/5 potential** | **2/5** | Very high clinical value, but the skull and prehospital performance requirements make this a moonshot |
| **Targeted molecular imaging** | **2/5** | **2/5** | **1/5** | Long-term platform destination; device and contrast-agent ecosystems would have to mature together |

This ranking produces an important distinction.

### Fatty liver is the most technically mature application.

### Microwave-ablation monitoring may be the most attractive *commercial wedge*.

Those are not the same question.

---

## Application 1 — Quantitative liver fat

### Why it is attractive

Liver fat has already provided the strongest human evidence that thermoacoustics can generate a quantitative tissue-composition biomarker.

The underlying value proposition is also clear: provide an accessible, noninvasive estimate of liver fat that is more practical for repeated use than MRI-PDFF.

Potential customers include:

- hepatology and metabolic-disease practices;
- obesity and bariatric programs;
- high-end primary care;
- pharmaceutical companies and CROs running metabolic-disease trials;
- and eventually broader clinical environments in which longitudinal liver-fat monitoring influences treatment.

### The business challenge

The competitive landscape is becoming more difficult, not less.

FibroScan already combines point-of-care use, an established evidence base, and reimbursement infrastructure.[5] Major ultrasound companies are incorporating quantitative liver-fat tools directly into diagnostic ultrasound platforms.[6]

Therefore, thermoacoustics probably needs to win on a **specific clinical or operational advantage**, not simply on novelty.

Examples of questions worth testing include:

- Does it remain accurate in patients where ultrasound-based attenuation measurements become less reliable?
- Does it better track *changes* in liver fat over time?
- Can it provide MRI-like quantitative information at substantially lower cost and complexity?
- Can it combine liver-fat measurement with conventional ultrasound anatomy in a single workflow?
- Can it improve subject selection or response monitoring in metabolic-drug trials?

The first commercially meaningful liver-fat study should therefore not only ask, **"Does TA correlate with MRI-PDFF?"**

It should increasingly ask:

> **"In which patient or workflow does TA change the clinical or economic decision compared with what the customer can already buy?"**

---

## Application 2 — Microwave-ablation monitoring

This is the application that moves up most sharply when the three clocks are considered together.

Microwave ablation is already an established therapy for tumors such as unresectable liver lesions. Commercial systems such as Medtronic's Emprint use a **2.45 GHz, high-power microwave generator**, and procedures are already guided using ultrasound, CT, or MRI.[7]

The unmet problem is not generating microwave energy.

It is knowing, during the procedure, **where that energy actually went and whether the intended treatment margin was achieved**.

Current commercial systems use predicted ablation-zone information, and adjunctive tools are emerging. For example, the FDA-cleared BioTraceIO Precision system provides adjunctive mapping related to liver ablation zones using ultrasound and imaging information.[8]

That is strategically important because it demonstrates that **ablation-zone assessment is already a product category**, not merely a research curiosity.

Thermoacoustics could potentially offer a different source of information: direct spatial sensitivity to microwave energy deposition and treatment-induced changes. Recent research has demonstrated TA imaging during 2.45 GHz microwave ablation using powers comparable to clinical systems, with one-second temporal resolution in ex vivo liver.[3]

### Why the economics may be favorable

The buyer already pays for an ablation procedure.

The microwave generator already exists.

The clinician already uses imaging guidance.

The clinical value of avoiding an incomplete treatment or inadequate margin is immediately understandable.

This creates several possible business models:

**OEM integration**  
TA becomes a monitoring capability built into an existing microwave-ablation platform.

**Premium generator / imaging module**  
TA is sold as an additional system capability associated with the procedure.

**Closed-loop treatment system**  
Longer term, TA-derived energy maps inform adaptive control of microwave power or treatment duration.

All three approaches may have less adoption friction than asking a hospital to create an entirely new diagnostic workflow.

The major problem is Clock 1: the most compelling recent work is still preclinical. Before this becomes a commercial thesis, TA would need to demonstrate robust in-vivo and eventually human prediction of clinically relevant ablation boundaries or margins.

But if that capability is established, **the other two clocks are already unusually well positioned**.

---

## Application 3 — Vascular and perfusion imaging

Blood is an appealing endogenous RF contrast source.

Human label-free TA vessel imaging has been demonstrated, but the published example recovered superficial forearm vessels approximately 5.5 mm below the skin.[2]

That is scientifically meaningful, but it is not yet a business case.

Doppler ultrasound, CTA, MRA, and catheter angiography already solve many vascular problems extremely well.

So "thermoacoustic angiography" is too broad.

The commercial question is:

> **What clinically important vascular information is difficult to obtain with existing modalities, but becomes practical if RF absorption can be localized acoustically at depth?**

Potential directions include:

- deep perfusion assessment;
- occult hemorrhage;
- tissue or organ viability;
- bedside monitoring where CT or MRI is impractical;
- vascular assessment in patients or anatomical regions poorly served by conventional ultrasound;
- and, at a more experimental level, dynamic tracking of a conductivity-enhancing bolus.

The saline concept is especially interesting because it introduces a time dimension:

**baseline image → conductivity perturbation → spatial and temporal tracking**

In principle, that could create information about perfusion, obstruction, or leakage.

But I would currently classify this as a **research hypothesis**, not a clinical claim. A convincing business case requires first identifying the narrow vascular use case where the new information is valuable enough to displace or complement established imaging.

---

## Application 4 — Intracranial hemorrhage

This is the highest-risk, highest-upside application in the current list.

Preclinical work has demonstrated detection of intracerebral hemorrhage in large live animals, with blood producing substantially stronger thermoacoustic signals than brain tissue.[9]

The potential clinical value is obvious: a portable method capable of detecting or localizing hemorrhage before CT could matter in ambulances, rural emergency departments, military medicine, sports medicine, and other settings where time-to-imaging is long.

That gives the application an extremely strong **economic-value clock**.

But the capability and adoption clocks are much further behind.

A useful product would have to perform reliably through the skull, across anatomy, rapidly, with very high sensitivity and specificity, in an environment where false reassurance could be dangerous.

This is therefore not the application I would choose to establish thermoacoustics commercially.

It is the application I would keep pursuing if the platform becomes mature enough to attack harder problems.

---

## Application 5 — Molecular thermoacoustic imaging

Molecular imaging is the longest-term objective that interests me most.

Targeted saline nanodroplets have already demonstrated that molecular specificity can be incorporated into RF-acoustic imaging in vivo.[4]

But this application has a severe **two-sided adoption problem**:

A molecular agent is difficult to justify without an installed imaging platform.

An imaging platform is difficult to build around an agent that does not yet have a clinical development pathway.

The business burden therefore includes both:

**device development**  
and  
**contrast-agent development**

with separate manufacturing, regulatory, clinical, and reimbursement challenges.

This is why I continue to believe that molecular thermoacoustic imaging should be viewed as the **destination rather than the first commercial wedge**.

A successful endogenous-contrast application can create:

**installed systems → clinical familiarity → manufacturing scale → regulatory experience → research access → incentive to develop targeted agents**

That sequence can move the molecular-imaging clocks far more effectively than attempting to develop the device and molecular-agent ecosystems simultaneously from zero.

---

## The product architecture matters

The business model is not independent of the hardware architecture.

I see four plausible commercialization paths.

| Product model | Advantage | Main disadvantage | Strategic fit |
| --- | --- | --- | --- |
| **Standalone TA diagnostic system** | Full control of product and workflow | Highest capital, training, regulatory, sales, and reimbursement burden | Best only if TA solves a problem no existing platform can address |
| **Ultrasound + TA platform** | Familiar anatomy and workflow; complementary information | Requires careful system integration and a clear reason to add TA | Strong for liver, vascular, and broader platform development |
| **Therapy-integrated TA** | Attaches to an existing procedure, energy source, buyer, and clinical need | Dependent on therapy-device partners and application-specific validation | Particularly attractive for microwave ablation |
| **Research / molecular-imaging platform** | Lower initial clinical-adoption burden and can seed an ecosystem | Smaller near-term market and still requires a compelling research community | Strong bridge toward future contrast agents |

This leads to a broader business lesson:

> **A new modality does not necessarily need to enter medicine as a new standalone modality.**

It may be much easier for thermoacoustics to enter as a **capability inside a workflow that clinicians already understand**.

That can change the adoption clock dramatically.

## Where defensibility would come from

A durable thermoacoustic business would need more than ownership of the basic imaging concept. The strongest competitive moat would probably be **system-level and application-specific**:

- RF delivery and field control that remain predictable across real patients;
- transducer and acquisition architectures optimized for combined ultrasound and TA;
- reconstruction, calibration, and quantitative models validated against clinical reference standards;
- proprietary clinical datasets that define where the measurement works and where it does not;
- application-specific regulatory claims and reimbursement evidence;
- workflow integration with the platform or procedure clinicians already use;
- manufacturing, RF safety, service, and cost structures that are difficult to reproduce from an academic prototype.

In other words, **the moat is not merely the signal. It is the validated system that turns the signal into a decision.**

That distinction matters strategically. A startup may need to own the critical quantitative know-how while partnering for ultrasound, therapy hardware, distribution, or contrast-agent development rather than attempting to recreate every part of the value chain.

---

## A commercial wedge should pass seven tests

When I evaluate a first application, I would ask seven questions.

1. **Is the clinical problem important enough that somebody already spends money trying to solve it?**
2. **Does TA provide information that is difficult to obtain with the current standard of care?**
3. **Does the information change a decision, rather than merely produce an interesting image?**
4. **Can the measurement be made reliably with a practical clinical system?**
5. **Can it fit into an existing workflow or procedure?**
6. **Is there a realistic regulatory and payment path?**
7. **Does success create an installed platform that enables additional TA applications?**

The last criterion matters because thermoacoustics has the characteristics of a **platform technology**, but the first customer is unlikely to buy a platform vision.

The first customer needs a narrow, concrete answer.

> **Sell the clinical answer first. Build the platform underneath it.**

---

## My current strategic ranking

If the objective is **technical de-risking**, I would rank the applications:

**1. Liver fat**  
**2. Microwave-ablation monitoring**  
**3. Vascular/perfusion imaging**  
**4. Burn/tissue viability**  
**5. Intracranial hemorrhage**  
**6. Molecular imaging**

If the objective is instead **which application could synchronize the three clocks fastest**, my ranking changes:

**1. Microwave-ablation monitoring**  
**2. Liver fat**  
**3. A yet-to-be-defined deep vascular/perfusion indication**  
**4. Burn/tissue viability**  
**5. Intracranial hemorrhage**  
**6. Molecular imaging**

That does not mean microwave ablation is more technically mature than liver fat. It is not.

It means that a first product is a **business-system problem**, not only an imaging-physics problem.

---

## What I would test next

If I were allocating development resources purely to learn which business path is strongest, I would run three parallel experiments.

### 1. Liver: test differentiation, not only accuracy

Benchmark TA prospectively against MRI-PDFF **and** leading point-of-care alternatives, with particular attention to the patients and longitudinal-use cases where current methods struggle.

The question becomes:

**Where does TA create incremental clinical value?**

### 2. Ablation: test whether TA can predict the treatment boundary that matters clinically

Move from elegant energy-deposition images toward a direct endpoint:

**Can the TA-derived map predict the final ablation zone or minimum treatment margin early enough to change the procedure?**

If yes, the economic and adoption arguments become much stronger.

### 3. Vascular: search for the application before optimizing the platform

Measure blood-to-background contrast, useful depth, spatial resolution, and robustness across 434 MHz, 915 MHz, and 2.45 GHz — but do it around specific clinical questions.

The objective should not be to prove that TA can image blood.

It should be to identify a vascular decision for which **TA has an unfair physical advantage**.

---

## The larger opportunity

The history of medical imaging contains many technically impressive technologies that never became important clinical businesses.

The ones that did succeed usually solved a valuable problem, fit a real workflow, and created enough economic value for somebody to adopt them.

That is the lens through which I now view thermoacoustics.

The physics is increasingly credible.

The clinical evidence is beginning to emerge.

The next challenge is to find the application in which **capability, economics, and adoption can advance together**.

If that first application succeeds, thermoacoustics can become more than a single-purpose device. It can become an installed platform for quantitative composition imaging, vascular and perfusion measurements, therapy monitoring, and eventually molecularly targeted imaging.

**The long-term vision is a platform.  
The near-term job is to earn the right to build it.**

[← Return to the science, clinical evidence, and long-term vision for thermoacoustic imaging](/thermoacoustic-imaging/)

---

## References

1. Cho JH, Bull CM, Thornton M, Gao J, Rubin JM, Steinberg I.  
   **[Thermoacoustic Ultrasound Assessment of Liver Steatosis—A Novel Approach for MASLD Diagnosis.](https://doi.org/10.3390/diagnostics16050804)**  
   _Diagnostics_. 2026;16:804.

2. Zheng Z, Huang L, Jiang H.  
   **[Label-free thermoacoustic imaging of human blood vessels in vivo.](https://doi.org/10.1063/1.5054652)**  
   _Applied Physics Letters_. 2018;113:253702.

3. Garrett DC, Aborahama Y, Xu J, Ku G, Wang LV.  
   **[Microwave Ablation Monitoring Using Thermoacoustic and Ultrasound Tomography.](https://doi.org/10.1109/JMW.2025.3612329)**  
   _IEEE Journal of Microwaves_. 2026;6(2):531–539.

4. Chen Y-S, Zhao Y, Beinat C, et al.  
   **[Ultra-high-frequency radio-frequency acoustic molecular imaging with saline nanodroplets in living subjects.](https://doi.org/10.1038/s41565-021-00869-5)**  
   _Nature Nanotechnology_. 2021;16:717–724.

5. Echosens.  
   **[Appropriate Coding and Billing for FibroScan.](https://www.echosens.com/en-us/appropriate-coding-and-billing-for-fibroscan/)**  
   2026.

6. GE HealthCare.  
   **[Ultrasound-Guided Fat Fraction (UGFF): From UGAP to quantitative liver-fat estimation.](https://www.gehealthcare.com/-/jssmedia/gehc/us/images/products/ultrasound/logiq/redesign-2026/whitepaper-ugff-liver-giu-logiq-family-r5-jb35927xx.pdf?rev=-1)**  
   2026.

7. Medtronic.  
   **[Emprint HP Ablation System with Thermosphere Technology.](https://www.medtronic.com/en-us/healthcare-professionals/products/surgical-energy/ablation/microwave-ablation/generators/emprint-hp-ablation-generator-thermosphere-technology.html)**  
   See also Medtronic system documentation identifying the HP generator as a 150 W, 2.45 GHz source.

8. U.S. Food and Drug Administration.  
   **[BioTraceIO Precision — 510(k) K243084.](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243084.pdf)**  
   2025.

9. Li J, Wu Z, Peng C, Song L, Luo Y.  
    **[Microwave-induced thermoacoustic imaging for the early detection of canine intracerebral hemorrhage.](https://doi.org/10.3389/fphys.2022.1067948)**  
    _Frontiers in Physiology_. 2022;13:1067948.

10. **[Three-clock framework that inspired this analysis.](https://youtu.be/KJxfSIvv920)**
