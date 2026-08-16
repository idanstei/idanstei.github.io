---
layout: page
title: Thermoacoustics
permalink: /thermoacoustic-imaging/
description: Thermoacoustic imaging for quantitative tissue characterization and accessible molecular imaging, spanning RF excitation, acoustic detection, and clinical translation.
nav: true
nav_order: 3
og_image: /assets/img/taeus_clinical_workflow.png
---

Modern medical imaging is extraordinarily good at showing anatomy. But many diseases are characterized by biochemical and physiological changes before significant anatomical changes become apparent.

Molecular imaging provides access to some of this critical information, but accessibility remains a significant limitation. Technologies such as positron emission tomography (PET) and single-photon emission computed tomography (SPECT) require specialized equipment, facilities, radiotracers, and infrastructure. Even when the information they provide is clinically valuable, frequent or point-of-care acquisition can be difficult.

**I believe thermoacoustic imaging could help address this gap.**

Thermoacoustics combines electromagnetic contrast with acoustic detection, offering the potential to acquire molecular and compositional information using an imaging platform that could retain many of the practical advantages of ultrasound.

---

## What is thermoacoustic imaging?

<div style="text-align: center;">
  <img src="/assets/img/Thermoaocustic_imaging.png"
       alt="Thermoacoustic imaging process diagram"
       style="max-width: 100%; height: auto;">
  <p><em>Thermoacoustic imaging uses RF excitation, electromagnetic absorption, thermoelastic expansion, acoustic detection, and image reconstruction.</em></p>
</div>

Thermoacoustic imaging uses short pulses of radiofrequency (RF) energy to excite tissue. Absorption of electromagnetic energy produces a very small, rapid temperature rise, resulting in thermoelastic expansion and the generation of a broadband acoustic transient.

That transient propagates through tissue, can be detected using ultrasound transducers, and can be reconstructed into an image.

The basic process is:

**RF excitation → electromagnetic absorption → thermoelastic expansion → acoustic transient → ultrasound detection → image**

Unlike conventional ultrasound, where contrast mainly originates from differences in acoustic properties and reflections at tissue boundaries, thermoacoustic contrast originates from the interaction between electromagnetic energy and tissue.

This provides access to information that conventional ultrasound cannot directly measure.

---

## Thermoacoustic and photoacoustic imaging

Thermoacoustic and photoacoustic imaging are closely related. Both rely on electromagnetic absorption followed by thermoelastic generation of broadband acoustic transients.

The primary difference is the source of excitation.

Photoacoustic imaging uses light, typically from a pulsed laser. Thermoacoustic imaging uses RF or microwave electromagnetic energy.

That difference creates an important tradeoff.

Photoacoustic imaging benefits from the rich optical absorption spectrum of biological tissue. Thermoacoustics sacrifices some of that intrinsic contrast, but RF excitation offers several potentially important advantages:

- **Greater penetration depth**
- **Simpler clinical infrastructure**
- **A more practical path toward quantitative imaging**

At RF frequencies, electromagnetic fields vary over centimeter scales and can generally be modeled and compensated for more readily than optical fluence deep within heterogeneous tissue.

**This enables a practical approach to recovering quantitative information about tissue properties, rather than relying solely on qualitative image contrast.**

---

## Why this matters clinically

One of the clearest early clinical applications for thermoacoustics is **liver fat assessment**.

Non-alcoholic fatty liver disease / metabolic dysfunction-associated steatotic liver disease (NAFLD / MASLD) is common, clinically important, and well suited to a quantitative, accessible imaging approach. MRI-PDFF is an excellent reference standard, but access and cost limit how broadly it can be used.

Thermoacoustics offers a different approach. Rather than relying on an acoustic surrogate for fat, it derives contrast from differences in the electromagnetic properties of lean and fatty tissue.

<div style="text-align: center;">
  <img src="/assets/img/taeus_clinical_workflow.png"
       alt="Clinical thermoacoustic imaging workflow showing probe positioning, B-mode ultrasound, and thermoacoustic overlay"
       style="max-width: 100%; height: auto;">
  <p><em>Clinical thermoacoustic imaging workflow: probe positioning, anatomical B-mode ultrasound, and co-registered thermoacoustic signal overlay.</em></p>
</div>

That transition matters to me: the technology begins to look less like a laboratory experiment and more like a practical imaging system.

---

## Demonstrating quantitative thermoacoustic imaging in humans

At ENDRA Life Sciences, my focus shifted from exploring what thermoacoustics could measure to a different challenge: could we turn it into a practical, quantitative clinical device?

We developed the TAEUS Liver system to estimate the liver fat fraction by exploiting differences in RF absorption associated with tissue composition.

In a prospective clinical feasibility study of 40 subjects, Thermoacoustic Fat Fraction (TAFF) showed a correlation **r = 0.89** with MRI-PDFF, with a mean absolute error of **3.04 percentage points**. Nearly **90% of subjects were within 5 percentage points** of the MRI-PDFF reference measurement.

A subsequent company-reported multi-site evaluation expanded the dataset to 64 subjects across sites in the United States and Canada. The same underlying estimation algorithm was used at an independent external site without site-specific tuning, and the combined cohort maintained a correlation of **r = 0.90** with MRI-PDFF. These later results were reported in an ENDRA company white paper and have not yet undergone peer review.

For me, the significance of this work extends beyond liver fat assessment. It demonstrated that thermoacoustics can progress from generating visually interesting images to providing repeatable, quantitative measurements in human subjects.

<div style="text-align: center;">
  <img src="/assets/img/Diagnossi_paper_Figure_4.png"
       alt="Clinical evaluation of Thermoacoustic Fat Fraction (TAFF) against MRI-PDFF: Bland–Altman agreement, error distribution, and Deming regression"
       style="max-width: 100%; height: auto;">
  <p><em>Clinical evaluation of Thermoacoustic Fat Fraction (TAFF) against MRI-PDFF: Bland–Altman agreement, error distribution, and Deming regression.</em></p>
</div>

---

## From tissue composition to molecular imaging

Thermoacoustic imaging has less rich intrinsic biological contrast than optical photoacoustics. But that is different from saying that thermoacoustic contrast is restricted to the natural electromagnetic properties of tissue.

Intrinsic RF absorption can already provide quantitative information about tissue composition. Exogenous agents can add another layer of specificity.

---

## A personal connection to this work

My interest in thermoacoustic molecular imaging is also connected to an earlier part of my career.

At Stanford Radiology, I worked under Dr. Sanjiv Sam Gambhir, whose group was deeply involved in developing new approaches to molecular imaging. As a group leader, I advised Yun-Sheng Chen, who later led work on targeted radiofrequency-acoustic molecular imaging using saline nanodroplets.

That research eventually demonstrated **in vivo RF-acoustic molecular imaging of prostate cancer**. GRPR-targeted nanodroplets produced substantially stronger RF-acoustic signals in GRPR-positive prostate tumors than in the comparison groups, demonstrating that molecular targeting could be incorporated into an RF-acoustic imaging approach.

Later, while serving as Applied Science Leader at ENDRA Life Sciences, I provided both Yun-Sheng Chen and Olumide “Ollie” Ogunlade access to TAEUS systems so they could continue their research in thermoacoustic imaging.

For me, this creates a direct connection between two sides of the problem: developing the imaging instrument and exploring the molecular contrast that the instrument could eventually support.

<div style="text-align: center;">
  <img src="/assets/img/stanford_targeted_molecular_imaging.png"
       alt="Targeted RF-acoustic molecular imaging using saline nanodroplets"
       style="max-width: 100%; height: auto;">
  <p><em>Targeted RF-acoustic molecular imaging: saline-loaded nanodroplet contrast agent, RF-acoustic imaging platform, and in vivo targeted tumor contrast. Adapted from Chen et al., <i>Nature Nanotechnology</i> (2021).</em></p>
</div>

---

## Beyond endogenous contrast

Thermoacoustic imaging already provides endogenous contrast based on differences in tissue electromagnetic properties. At ENDRA, we exploited that contrast to quantify liver fat, where differences in water, electrolyte, and lipid composition produce measurable differences in RF absorption.

However, the potential extends beyond intrinsic tissue contrast.

Earlier work on thermoacoustic contrast agents investigated materials including gadolinium compounds, iron oxide particles, carbon nanotubes, and electrolytes. Those studies showed an important result: what matters is not simply whether a material resembles a conventional contrast agent, but how it changes electromagnetic absorption.

In particular, work by Ogunlade and Beard showed that ionic conductivity can provide strong thermoacoustic contrast and identified simple electrolytes such as saline as particularly promising.

Chen and colleagues subsequently encapsulated hypertonic saline within biocompatible nanodroplets and functionalized the particles for molecular targeting. Using GRPR-targeted nanodroplets, they demonstrated **in vivo RF-acoustic molecular imaging of prostate cancer**.

These results are significant because they demonstrate that molecular specificity is not solely a hypothetical future extension of thermoacoustic imaging; it has already been experimentally validated.

---

## First, we need the imaging platform

There is a practical chicken-and-egg problem. Developing molecular probes is difficult and expensive, and there is limited incentive to build an ecosystem of thermoacoustic-specific contrast agents if researchers and clinicians do not yet have access to practical thermoacoustic imaging systems.

So the first step is the instrument.

Build a practical system. Make it reliable. Make it quantitative. Put it in the hands of researchers and clinicians.

Once the platform is in place, researchers can explore new applications. Clinicians can identify new biological questions it might answer. Chemists and molecular-imaging researchers have a reason to develop new probes and contrast agents around it.

The imaging system can become the foundation for a broader ecosystem rather than the endpoint of a single application.

**That is the opportunity I want to continue working on.**

---

## What needs to happen next?

Thermoacoustic imaging has been studied for decades, and many of its core physical principles are well established.

The current challenge is clinical translation.

A practical quantitative thermoacoustic platform requires progress across multiple disciplines:

- RF excitation and electromagnetic field control
- acoustic detection and transducer design
- reconstruction, modeling, and quantitative calibration
- system architecture and integration
- verification and validation
- clinical application development and clinical validation
- manufacturability and cost reduction
- regulatory and product-development strategy
- clinical workflow and usability
- and, eventually, targeted contrast agents and molecular probes

These challenges are interdependent and must be addressed together as a unified system.

The intersection of physics, engineering, clinical translation, and product development is precisely what makes thermoacoustic imaging compelling to me.

---

## The longer-term vision

My interest in thermoacoustic imaging ultimately comes from a broader goal:

### What if molecular imaging could become as accessible as ultrasound?

Ultrasound succeeded not only because of the information it provides, but because of where and how it can be used. It is safe, comparatively inexpensive, increasingly portable, and available throughout medicine.

Molecular imaging provides a fundamentally different kind of information, but today it generally lacks that level of accessibility.

Quantitative thermoacoustic imaging offers a promising approach to narrowing this gap.

The first step is the device.

The longer-term opportunity is a platform capable of delivering quantitative tissue information and, eventually, supporting increasingly specific molecular contrast.

**My goal is to help make that platform real.**

---

## Interested in this problem?

If you are working on thermoacoustic imaging, molecular imaging, RF or acoustic imaging, contrast-agent development, or another technology aimed at making advanced medical imaging more accessible, I would be very interested in hearing from you.

[Get in touch](mailto:idanstei@gmail.com)

## Selected references

1. Cho JH, Bull CM, Thornton M, Gao J, Rubin JM, Steinberg I.  
   **[Thermoacoustic Ultrasound Assessment of Liver Steatosis—A Novel Approach for MASLD Diagnosis.](https://doi.org/10.3390/diagnostics16050804)**  
   *Diagnostics*. 2026;16:804.

2. Chen Y-S, Zhao Y, Beinat C, et al.  
   **[Ultra-High-Frequency-Radio-Frequency-Acoustic Molecular Imaging with Saline Nanodroplets in Living Subjects.](https://doi.org/10.1038/s41565-021-00869-5)**  
   *Nature Nanotechnology*. 2021;16:717–724.

3. Ogunlade O, Beard P.  
   **[Exogenous contrast agents for thermoacoustic imaging: An investigation into the underlying sources of contrast.](https://doi.org/10.1118/1.4903277)**  
   *Medical Physics*. 2015;42(1):170–181.

4. ENDRA Life Sciences.  
   **Multi-Site Validation of the TAEUS Liver Device Against MRI-PDFF.**  
   Company white paper, 2026.