---
layout: page
title: Thermoacoustics
permalink: /thermoacoustic-imaging/
description: A path toward accessible, quantitative molecular imaging.
nav: true
nav_order: 3
---

Modern medical imaging is extraordinarily good at showing anatomy. But many diseases are characterized by biochemical and physiological changes before significant anatomical changes become apparent.

Molecular imaging provides access to some of this information, but accessibility remains a fundamental limitation. Technologies such as PET and SPECT require specialized equipment, facilities, radiotracers, and infrastructure. Even when the information they provide is clinically valuable, obtaining it frequently or at the point of care can be difficult.

**I believe thermoacoustic imaging could help close that gap.**

The idea is to combine electromagnetic contrast with acoustic detection, creating the potential to obtain molecular and compositional information using an imaging platform that could ultimately retain many of the practical advantages of ultrasound.

---

## What is thermoacoustic imaging?

<div style="text-align: center;">
  <img src="/assets/img/Thermoaocustic_imaging.png"
       alt="Thermoacoustic imaging process diagram"
       style="max-width: 100%; height: auto;">
  <p><em>Overview of thermoacoustic imaging: RF excitation, absorption, thermoelastic expansion, acoustic detection, and image reconstruction.</em></p>
</div>

Thermoacoustic imaging uses short pulses of radiofrequency (RF) energy to excite tissue. Absorption of electromagnetic energy produces a very small, rapid temperature rise, resulting in thermoelastic expansion and the generation of acoustic waves.

Those waves can be detected using ultrasound transducers and reconstructed into an image.

The basic process is:

**RF excitation → electromagnetic absorption → thermoelastic expansion → acoustic wave → ultrasound detection → image**

Unlike conventional ultrasound, where contrast primarily arises from differences in acoustic properties and reflections at tissue boundaries, thermoacoustic contrast originates from the interaction between electromagnetic energy and tissue.

This provides access to information that conventional ultrasound cannot directly measure.

---

## Thermoacoustic and photoacoustic imaging

Thermoacoustic and photoacoustic imaging are closely related. Both rely on electromagnetic absorption followed by thermoelastic generation of acoustic waves.

The primary difference is the source of excitation.

Photoacoustic imaging uses light, typically from a pulsed laser. Thermoacoustic imaging uses RF or microwave electromagnetic energy.

That difference creates an important tradeoff.

Photoacoustic imaging benefits from the extraordinarily rich optical absorption spectrum of biological tissue. Hemoglobin, melanin, lipids, water, and exogenous agents can all provide useful optical contrast.

Thermoacoustics sacrifices some of that rich intrinsic contrast, but RF excitation offers several potentially important advantages.

### Greater penetration depth

RF energy can penetrate tissue substantially deeper than light at wavelengths commonly used for photoacoustic imaging, making thermoacoustics particularly interesting for imaging deep organs and larger patients.

### Simpler clinical infrastructure

Thermoacoustic systems do not require the high-power pulsed lasers used by many photoacoustic systems or the associated laser safety equipment and procedures.

For a technology intended ultimately to become widely accessible, that practical difference matters.

### A path toward quantification

Perhaps the most interesting distinction, however, is the potential for quantitative imaging.

---

## Why quantification matters

In both photoacoustic and thermoacoustic imaging, the measured acoustic signal depends not only on the tissue's absorption properties but also on the amount of electromagnetic energy delivered locally.

To recover a quantitative tissue property, the excitation field must be understood.

With optical excitation, light propagation through deep, heterogeneous tissue is extremely complex. Determining the local optical fluence can consequently become a fundamental challenge for quantitative photoacoustic imaging.

At RF frequencies, electromagnetic wavelengths in tissue are on the order of centimeters rather than the sub-micron wavelengths of light. The electromagnetic field can therefore be modeled and compensated for much more readily.

**This creates a practical path toward recovering quantitative information about tissue properties rather than relying solely on qualitative image contrast.**

That distinction is important.

A qualitative image can show that two regions of tissue are different. A quantitative measurement can potentially characterize the magnitude of that difference, compare it between examinations, and track it over time.

That turns an imaging contrast mechanism into a potential quantitative biomarker.

---

## Demonstrating quantitative thermoacoustic imaging in humans

At ENDRA Life Sciences, my focus shifted from exploring what thermoacoustics could potentially measure to a different challenge: could we turn it into a practical quantitative clinical device?

We developed the TAEUS Liver system to estimate liver fat fraction using differences in RF absorption associated with tissue composition. Rather than relying on an acoustic surrogate for fat, the thermoacoustic measurement derives contrast from differences in the electromagnetic properties of lean and fatty tissue.

In a prospective clinical feasibility study of 40 subjects, Thermoacoustic Fat Fraction (TAFF) showed a correlation of **r = 0.89** with MRI-PDFF, with a mean absolute error of **3.04 percentage points**. Nearly **90% of subjects were within 5 percentage points** of the MRI-PDFF reference measurement.

For me, the significance of that work extends beyond liver fat. It demonstrated that thermoacoustics could move beyond producing an interesting image and toward providing a repeatable, quantitative measurement in human subjects.

<div style="text-align: center;">
  <img src="/assets/img/Diagnossi_paper_Figure_4.png"
       alt="Clinical evaluation of Thermoacoustic Fat Fraction (TAFF) against MRI-PDFF: Bland–Altman agreement, error distribution, and Deming regression."
       style="max-width: 100%; height: auto;">
  <p><em>Overview of thermoacoustic imaging: RF excitation, absorption, thermoelastic expansion, acoustic detection, and image reconstruction.</em></p>
</div>


---

## From tissue composition to molecular imaging

Thermoacoustic imaging is sometimes considered to have relatively limited biological contrast compared with optical photoacoustics.

I believe that view overlooks an important distinction between what the technology can do today and what a mature thermoacoustic imaging platform could eventually enable.

Intrinsic RF absorption can already provide information related to tissue composition. But thermoacoustic contrast is not limited to the natural electromagnetic properties of tissue.

## A personal connection to this work

My interest in thermoacoustic molecular imaging is also connected to an earlier part of my career.

At Stanford Radiology, I worked under Dr. Sanjiv Sam Gambhir, whose group was deeply involved in developing new approaches to molecular imaging. As a group leader, I advised Yun-Sheng Chen, who later led work on targeted radiofrequency-acoustic molecular imaging using saline nanodroplets.

That research eventually demonstrated **targeted RF-acoustic molecular imaging in living subjects**. GRPR-targeted nanodroplets produced substantially stronger RF-acoustic signals in GRPR-positive prostate tumors than in the comparison groups, demonstrating that molecular targeting could be incorporated into an RF-acoustic imaging approach.

Later, while serving as Applied Science Leader at ENDRA Life Sciences, I provided both Yun-Sheng Chen and Olumide "Ollie" Ogunlade access to TAEUS systems so they could continue their research in thermoacoustic imaging.

For me, this creates a direct connection between two sides of the problem: developing the imaging instrument and exploring the molecular contrast that the instrument could eventually support.

## Beyond endogenous contrast

Thermoacoustic imaging already provides endogenous contrast based on differences in tissue electromagnetic properties. At ENDRA, we exploited that contrast to quantify liver fat, where differences in water, electrolyte, and lipid composition produce measurable differences in RF absorption.

But the potential does not stop with intrinsic tissue contrast.

Earlier work on thermoacoustic contrast agents investigated materials including gadolinium compounds, iron oxide particles, carbon nanotubes, and electrolytes. Those studies showed an important result: simply choosing a material that sounds like a conventional imaging contrast agent is not enough. What matters is how the agent changes electromagnetic absorption.

In particular, work by Ogunlade and Beard showed that ionic conductivity can provide strong thermoacoustic contrast and identified simple electrolytes such as saline as particularly promising.

That idea was subsequently taken much further.

Chen and colleagues encapsulated hypertonic saline within biocompatible nanodroplets and functionalized the particles for molecular targeting. Using GRPR-targeted nanodroplets, they demonstrated **in-vivo RF-acoustic molecular imaging of prostate cancer**.

This is important to me because it demonstrates that molecular specificity is not merely a hypothetical future extension of thermoacoustic imaging. It has already been demonstrated experimentally.

The question is how to translate that possibility into a practical imaging platform.

**Quantitative endogenous tissue characterization combined with exogenous molecular contrast on the same imaging platform.**

But there is a practical chicken-and-egg problem.

There is little incentive to invest heavily in new thermoacoustic-specific molecular probes when researchers and clinicians do not yet have broad access to thermoacoustic imaging systems.

That is why I believe the sequence matters.

---

## First, we need the imaging platform.

Developing molecular probes is difficult and expensive. There is limited incentive to build an ecosystem of thermoacoustic-specific contrast agents if researchers and clinicians do not have access to practical thermoacoustic imaging systems.

So the first step is the instrument.

Build a practical system. Make it reliable. Make it quantitative. Put it in the hands of researchers and clinicians.

Once the platform exists, researchers can explore new applications. Clinicians can identify new biological questions it might answer. Chemists and molecular-imaging researchers have a reason to develop new probes and contrast agents around it.

The imaging system can become the foundation for an ecosystem rather than the endpoint of a single application.

**That is the opportunity I want to continue working on.**

---

## What needs to happen next?

Thermoacoustic imaging has been studied for decades, and many of its underlying physical principles are well established.

The challenge now is translation.

A practical quantitative thermoacoustic platform requires progress across multiple disciplines:

- RF excitation and electromagnetic field control
- acoustic detection and transducer design
- image reconstruction and signal processing
- electromagnetic modeling and field compensation
- system calibration and quantitative measurement
- hardware and system architecture
- clinical application development and validation
- manufacturability and product development
- and, eventually, targeted contrast agents and molecular probes

These are not independent problems. They have to work together as a system.

That intersection of physics, engineering, clinical translation, and product development is exactly what makes thermoacoustic imaging so interesting to me.

---

## The longer-term vision

My interest in thermoacoustic imaging ultimately comes from a broader goal:

### What if molecular imaging could become as accessible as ultrasound?

Ultrasound succeeded not only because of the information it provides, but because of where and how it can be used. It is safe, comparatively inexpensive, increasingly portable, and available throughout medicine.

Molecular imaging provides a fundamentally different kind of information, but today it generally lacks that level of accessibility.

I believe quantitative thermoacoustic imaging offers a compelling path toward narrowing that gap.

The first step is the device.

The longer-term opportunity is a platform capable of providing quantitative tissue information and, eventually, supporting increasingly specific molecular contrast.

**My goal is to help make that platform real.**

---

## Interested in this problem?

If you are working on thermoacoustic imaging, molecular imaging, RF or acoustic imaging, contrast-agent development, or another technology aimed at making advanced medical imaging more accessible, I would be very interested in hearing from you.

[Get in touch](mailto:idanstei@gmail.com)

## Selected references

1. Cho JH, Bull CM, Thornton M, Gao J, Rubin JM, Steinberg I.  
   **Thermoacoustic Ultrasound Assessment of Liver Steatosis—A Novel Approach for MASLD Diagnosis.**  
   *Diagnostics*. 2026;16:804.

2. Chen Y-S, Zhao Y, Beinat C, et al.  
   **Ultra-High-Frequency-Radio-Frequency-Acoustic Molecular Imaging with Saline Nanodroplets in Living Subjects.**  
   *Nature Nanotechnology*. 2021;16:717–724.

3. Ogunlade O, Beard P.  
   **Exogenous contrast agents for thermoacoustic imaging: An investigation into the underlying sources of contrast.**  
   *Medical Physics*. 2015;42(1):170–181.

4. ENDRA Life Sciences.  
   **Multi-Site Validation of the TAEUS Liver Device Against MRI-PDFF.**  
   White paper, 2026.
