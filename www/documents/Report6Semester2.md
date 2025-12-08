# EE/CprE/SE 492 WEEKLY REPORT 06

**Date Range:** 10/31/2025 – 11/13/2025
**Group Number:** sddec25-01
**Project Title:** Semantic Segmentation Optimization
**Client/Advisor:** JR Spidell/Namrata Vaswani

## Team Members/Roles

- **Joseph Metzen** ([GitHub](https://github.com/jjmetzen)) – Kria Board Manager
- **Tyler Schaefer** ([GitHub](https://github.com/TSSchaef)) – ML Algorithm Analyst
- **Conner Ohnesorge** ([GitHub](https://github.com/connerohnesorge)) – ML Integration HWE
- **Aidan Perry** ([GitHub](https://github.com/priedieux)) – Multithreaded Program Developer

---

## Weekly Summary

The team spent the two weeks finishing up the project's documentation and running an important performance analysis. The team checked and made all needed changes to the design document, and one member made sure to move data from the Kria board's SD card for use by future teams. The test comparing the split versus single UNET model inference was a success; it showed the Single Model was much faster than the Split Model (4 Segments), with a total time of 529.39 ms compared to the Split Model's 784.29 ms. We held good meetings with professors and the TA to talk about the final paper and also started planning the final presentation and demo. Now, we are fully focused on making the final presentation and demo, which includes finishing the xfce demo program to show the eye tracking and semantic segmentation model working together live.

### Accomplishments

- **Joseph Metzen:** Transferred data from the SD card on the board to give to others teams for future projects. Looked over the design doc for any errors or corrections to make.

- **Tyler Schaefer:** Worked on design doc changes

- **Conner Ohnesorge:** Finished analysis program comparing the split vs the single UNET model inference.

- **Aidan Perry:** Worked on design document changes, as well as helped with analysis comparison. Met with TA to discuss design document changes.

### Pending Issues

_n/a_

---

## Individual Contributions

| Team Members | Individual Contributions | Hours this week | Hours Cumulative |
|--------------|--------------------------|-----------------|------------------|
| Joseph Metzen | Transferred data from SD card to other future teams working with the project. Also looked over the design doc for any errors or corrections to make. | 8 | 35 |
| Tyler Schaefer | Verifying information in the design doc | 7 | 34 |
| Conner Ohnesorge | Met with class professors about the completion situation.<br><br>Met with TA for final design doc analysis/reflection.<br><br>Finished analysis program comparing the split vs the single UNET model inference.<br><br>**Reported metrics:**<br><br>**Single Model Performance:**<br>- Mean Total Latency: 529.39 ms (± 0.26)<br>- Mean DPU Time: 474.32 ms (± 0.05)<br>- Mean Preprocess: 27.43 ms (± 0.23)<br>- Mean Postprocess: 27.64 ms (± 0.08)<br>- Memory Usage: 45.00 MB<br><br>**Split Model (4 Segments) Performance** (Note the obvious decrease in performance):<br>- Mean Total Latency: 784.29 ms (± 3.39)<br>- Mean DPU Time: 729.00 ms (± 3.38)<br>- Mean Preprocess: 27.64 ms (± 0.18)<br>- Mean Postprocess: 27.64 ms (± 0.04)<br>- Memory Usage: 111.01 MB | 8 | 39 |
| Aidan Perry | Verify and change information in the design document, familiarize myself with overleaf (software used for design document), met with TA for documentation, theorycrafting for final presentation and demo. | 7 | 33 |

---

## Plans for the Upcoming Weeks

- **Joseph Metzen:** Work on final presentation and demo for poster.

- **Tyler Schaefer:** Continue working on materials for the end of the project/presentation

- **Conner Ohnesorge:** Finish demo program which should run xfce for a live demo of the eye tracking and the semantic segmentation model working.

- **Aidan Perry:** Continue working on final presentation, as well as demo for poster.

---

## Tags

#weekly-report #semester2 #report6 #semantic-segmentation #ml-optimization #kria-board #unet #performance-analysis #split-model #single-model #demo #final-presentation

## Related Documents

- [[Report5Semester2]]
- [[DesignDocSemester1]]
