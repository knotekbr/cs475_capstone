<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline predicts imagined motor actions using neural oscillatory pattern classification. The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations.&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import SET”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Set”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here where only data from the last 6 channels are used.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 6-30 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Common Spatial Patterns (CSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. Here we use misclassification rate (MCR)." title="Simple Motor Imagery Prediction with CSP" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(453.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="5dd297c6-3527-44cc-8d9c-e9fd056d281d" version="1.0.1" />
		<node id="1" name="Segmentation" position="(756.0, 275.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="0f5ff239-a53f-4a06-b971-ed4d37913264" version="1.0.2" />
		<node id="2" name="LSL Output" position="(1369.0, 383.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="8ddaae7c-d55c-480e-bce9-0050a663d22a" version="1.4.2" />
		<node id="3" name="Variance" position="(959.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="cde23f44-97da-41be-8cec-9302f9dfa51c" version="1.0.0" />
		<node id="4" name="Logarithm" position="(1064.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="be9bbb74-a32d-4959-b75a-f5c69399b6b6" version="1.0.0" />
		<node id="5" name="Select Range" position="(553.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="87a36776-413b-4b9f-801d-a61a7598937d" version="1.1.0" />
		<node id="6" name="Logistic Regression" position="(1174.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="9029bb0d-142a-4467-bbe9-6ebfaf946316" version="1.1.0" />
		<node id="7" name="FIR Filter" position="(654.0, 275.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="23c6d71a-5a0a-4f08-8394-e2c3101ecfe9" version="1.1.0" />
		<node id="8" name="LSL Input" position="(137.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="2b322603-70a1-471f-ab92-aac73308f79b" version="1.5.1" />
		<node id="9" name="Dejitter Timestamps" position="(243.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="5b592e61-c68d-443a-8f8f-88e17443abf7" version="1.0.0" />
		<node id="10" name="Streaming Bar Plot" position="(1366.0, 280.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="43ad0a2c-2d36-472a-bed5-9a33f1064572" version="1.0.3" />
		<node id="11" name="Accumulate Calibration Data" position="(348.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owaccumulatecalibrationdata.OWAccumulateCalibrationData" title="Accumulate Calibration Data" uuid="eac7661a-841d-4d45-ae30-ea13989bca14" version="1.0.0" />
		<node id="12" name="Source Power Comodulation" position="(859.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.neural.owsourcepowercomodulation.OWSourcePowerComodulation" title="Source Power Comodulation" uuid="f33b15e7-6838-4bc8-b9e8-4e3a5d7f4e1a" version="1.0.0" />
		<node id="13" name="Override Axis" position="(1270.0, 280.0)" project_name="NeuroPype" qualified_name="widgets.neural.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="bdb20acb-3ba2-448d-8401-1c6be90f21e9" version="1.4.2" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="13" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYCwAAAHRyYWluX3Jp
Z2h0cQdLAFgKAAAAdHJhaW5fZG93bnEISwFYCgAAAHRyYWluX2xlZnRxCUsCWAgAAAB0cmFpbl91
cHEKSwNYDQAAAHRyYWluX25ldXRyYWxxC0sEdVgOAAAAbWFwcGluZ19mb3JtYXRxDFgGAAAAY29t
cGF0cQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3Vu
cGlja2xlX3R5cGUKcRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsA
AwAAAAABkgAAAaoAAAL5AAACzwAAAZIAAAGqAAAC+QAAAs8AAAAAAAAAAAeAAAABkgAAAaoAAAL5
AAACz3EUhXEVh3EWUnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgRAAAAc3VwcG9ydF93aWxkY2Fy
ZHNxGYlYCwAAAHVzZV9udW1iZXJzcRqJWAcAAAB2ZXJib3NlcRuJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYBwAAAHNsaWRpbmdx
BlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNzaXAKX3Vu
cGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtDQgHZ0MsA
AwAAAAABugAAAb8AAAMhAAAC1QAAAboAAAG/AAADIQAAAtUAAAAAAAAAAAeAAAABugAAAb8AAAMh
AAAC1XEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFY
DgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETXXEUKEc/4AAAAAAAAEdAEgAA
AAAAAGVYBwAAAHZlcmJvc2VxFYl1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAAA3AAABHQAAAMOAAADDAAAAPsAAARzAAADDQAAAAAAAAAAB4AA
AAMMAAAA+wAABHMAAAMNcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcWD4AAAAo
bWFrZSBzdXJlIHRvIG5ldmVyIHVzZSBzYW1lIHN0cmluZyBtb3JlIHRoYW4gb25jZSBvbiBuZXR3
b3JrKXEdWAUAAABzcmF0ZXEeWA0AAAAodXNlIGRlZmF1bHQpcR9YCwAAAHN0cmVhbV9uYW1lcSBY
DgAAAG9wZW5iY2lfb3V0cHV0cSFYCwAAAHN0cmVhbV90eXBlcSJYBwAAAENvbnRyb2xxI1gTAAAA
dXNlX2RhdGFfdGltZXN0YW1wc3EkiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEliXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwwAAAGnAAAEcwAAAmAAAAMMAAABpwAABHMAAAJgAAAA
AAAAAAAHgAAAAwwAAAGnAAAEcwAAAmBxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgIAAAAbWV0YWRhdGFxA31xBFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgMAAAAUHlRdDUu
UXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCENCAdnQywADAAAAAAMLAAABnwAABHQAAAJLAAADDAAA
Ab4AAARzAAACSgAAAAAAAAAAB4AAAAMMAAABvgAABHMAAAJKcQmFcQqHcQtScQxYDgAAAHNldF9i
cmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADDAAAAaIAAARzAAACiAAAAwwA
AAGiAAAEcwAAAogAAAAAAAAAAAeAAAADDAAAAaIAAARzAAACiHELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gFAAAAMC4uLjdxEFgOAAAAc2V0X2JyZWFrcG9pbnRxEYlYBAAAAHVuaXRxElgHAAAA
aW5kaWNlc3ETdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYCAAA
AGJhbGFuY2VkcQVYCgAAAGNvbmRfZmllbGRxBlgLAAAAVGFyZ2V0VmFsdWVxB1gQAAAAZG9udF9y
ZXNldF9tb2RlbHEIiVgQAAAAZHVhbF9mb3JtdWxhdGlvbnEJiVgPAAAAZmVhdHVyZV9zY2FsaW5n
cQpYBAAAAG5vbmVxC1gMAAAAaW5jbHVkZV9iaWFzcQyIWA8AAABpbml0aWFsaXplX29uY2VxDYlY
CQAAAGwxX3JhdGlvc3EOWA0AAAAodXNlIGRlZmF1bHQpcQ9YCAAAAG1heF9pdGVycRBLZFgIAAAA
bWV0YWRhdGFxEX1xElgKAAAAbXVsdGljbGFzc3ETWAQAAABhdXRvcRRYCQAAAG51bV9mb2xkc3EV
SwVYCAAAAG51bV9qb2JzcRZLAVgNAAAAcHJvYmFiaWxpc3RpY3EXiFgLAAAAcmFuZG9tX3NlZWRx
GE05MFgLAAAAcmVndWxhcml6ZXJxGVgCAAAAbDJxGlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEb
Y3NpcApfdW5waWNrbGVfdHlwZQpxHFgMAAAAUHlRdDUuUXRDb3JlcR1YCgAAAFFCeXRlQXJyYXlx
HkNCAdnQywADAAAAAAKDAAAAdAAAA/QAAALxAAAChAAAAJMAAAPzAAAC8AAAAAAAAAAAB4AAAAKE
AAAAkwAAA/MAAALwcR+FcSCHcSFScSJYDQAAAHNlYXJjaF9tZXRyaWNxI1gIAAAAYWNjdXJhY3lx
JFgOAAAAc2V0X2JyZWFrcG9pbnRxJYlYBgAAAHNvbHZlcnEmWAUAAABsYmZnc3EnWAkAAAB0b2xl
cmFuY2VxKEc/Gjbi6xxDLVgJAAAAdmVyYm9zaXR5cSlLAHUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAADCwAAAUMA
AAR0AAACpgAAAwwAAAFiAAAEcwAAAqUAAAAAAAAAAAeAAAADDAAAAWIAAARzAAACpXEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgWAAAAbmFtZT0nb3BlbmJjaV9tYXJrZXJzJ3EJWAwAAABtYXhfYmxvY2ts
ZW5xCk0ABFgKAAAAbWF4X2J1ZmxlbnELSx5YDAAAAG1heF9jaHVua2xlbnEMSwBYCAAAAG1ldGFk
YXRhcQ19cQ5YDAAAAG5vbWluYWxfcmF0ZXEPWA0AAAAodXNlIGRlZmF1bHQpcRBYCQAAAG9taXRf
ZGVzY3ERiVgPAAAAcHJlYWxsb2NfYnVmZmVycRKIWA4AAABwcm9jX2Nsb2Nrc3luY3ETiFgNAAAA
cHJvY19kZWppdHRlcnEUiVgPAAAAcHJvY19tb25vdG9uaXplcRWJWA8AAABwcm9jX3RocmVhZHNh
ZmVxFolYBQAAAHF1ZXJ5cRdYEgAAAG5hbWU9J29wZW5iY2lfZWVnJ3EYWAcAAAByZWNvdmVycRmI
WBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEaRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRtjc2lwCl91bnBpY2tsZV90eXBlCnEcWAwAAABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVB
cnJheXEeQ0IB2dDLAAMAAAAABLEAAACnAAAGGgAAAtYAAASyAAAAxgAABhkAAALVAAAAAAAAAAAH
gAAABLIAAADGAAAGGQAAAtVxH4VxIIdxIVJxIlgOAAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWAgAAABtZXRhZGF0YXEEfXEFWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NS5RdENvcmVxCFgKAAAAUUJ5
dGVBcnJheXEJQ0IB2dDLAAMAAAAAAwsAAAF8AAAEdAAAAm0AAAMMAAABmwAABHMAAAJsAAAAAAAA
AAAHgAAAAwwAAAGbAAAEcwAAAmxxCoVxC4dxDFJxDVgOAAAAc2V0X2JyZWFrcG9pbnRxDolYDgAA
AHdhcm11cF9zYW1wbGVzcQ9K/////3Uu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWA8AAABhdXRvX2Jhcl9jb2xvcnNxAolYBAAAAGF4
aXNxA1gHAAAAZmVhdHVyZXEEWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNGRkZGRkZxBlgJ
AAAAYmFyX2NvbG9ycQdYAQAAAGJxCFgJAAAAYmFyX3dpZHRocQlHP+zMzMzMzM1YCQAAAGZvbnRf
c2l6ZXEKR0AkAAAAAAAAWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksyTbwCTfQBZVgOAAAAaW5z
dGFuY2VfZmllbGRxDVgNAAAAKHVzZSBkZWZhdWx0KXEOWA4AAABsYWJlbF9yb3RhdGlvbnEPWAoA
AABob3Jpem9udGFscRBYCAAAAG1ldGFkYXRhcRF9cRJYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
E2NzaXAKX3VucGlja2xlX3R5cGUKcRRYDAAAAFB5UXQ1LlF0Q29yZXEVWAoAAABRQnl0ZUFycmF5
cRZDQgHZ0MsAAwAAAAADDAAAAREAAARzAAAC9gAAAwwAAAERAAAEcwAAAvYAAAAAAAAAAAeAAAAD
DAAAAREAAARzAAAC9nEXhXEYh3EZUnEaWA4AAABzZXRfYnJlYWtwb2ludHEbiVgMAAAAc2hvd190
b29sYmFycRyJWAsAAABzdHJlYW1fbmFtZXEdWA0AAAAodXNlIGRlZmF1bHQpcR5YBQAAAHRpdGxl
cR9YDgAAAENsYXNzaWZpY2F0aW9ucSBYEQAAAHVzZV9sYXN0X2luc3RhbmNlcSGIWAcAAAB2ZXJi
b3NlcSKJWAgAAAB5X2xpbWl0c3EjXXEkKEsASwFldS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAwAAABiZWdpbl9tYXJrZXJxAVgLAAAAc3RhcnRfdHJhaW5xAlgRAAAAY2FsaWJyYXRp
b25fZmlyc3RxA4hYDwAAAGNhbl9yZWNhbGlicmF0ZXEEiFgPAAAAZW1pdF9jYWxpYl9kYXRhcQWI
WBEAAABlbWl0X3ByZWRpY3RfZGF0YXEGiFgKAAAAZW5kX21hcmtlcnEHWAkAAABlbmRfdHJhaW5x
CFgLAAAAbWFya2VyX21vZGVxCVgHAAAAbWFya2Vyc3EKWAgAAABtZXRhZGF0YXELfXEMWA0AAABw
cmludF9tYXJrZXJzcQ2JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ5jc2lwCl91bnBpY2tsZV90
eXBlCnEPWAwAAABQeVF0NS5RdENvcmVxEFgKAAAAUUJ5dGVBcnJheXERQ0IB2dDLAAMAAAAAAwwA
AAGVAAAEcwAAAs8AAAMMAAABlQAABHMAAALPAAAAAAAAAAAHgAAAAwwAAAGVAAAEcwAAAs9xEoVx
E4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYBwAAAHZlcmJvc2VxF4l1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAoAAABjb3ZfbGFtYmRhcQFHP1BiTdLxqfxYDwAAAGluaXRpYWxpemVfb25jZXECiFgI
AAAAbWV0YWRhdGFxA31xBFgDAAAAbm9mcQVLBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3Np
cApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNC
AdnQywADAAAAAAMLAAABfAAABHQAAAJtAAADDAAAAZsAAARzAAACbAAAAAAAAAAAB4AAAAMMAAAB
mwAABHMAAAJscQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAwAAAB0YXJnZXRfZmll
bGRxD1gLAAAAVGFyZ2V0VmFsdWVxEHUu
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWAAAAABxBVgIAAAAZGVj
aW1hbHNxBksDWAkAAABpbml0X2RhdGFxB11xCChYBQAAAHJpZ2h0cQlYBAAAAGRvd25xClgEAAAA
bGVmdHELWAIAAAB1cHEMWAcAAABuZXV0cmFscQ1lWAsAAABqb2luX2Zvcm1hdHEOWAUAAAB7bmV3
fXEPWBEAAABrZWVwX290aGVyX2FycmF5c3EQiVgKAAAAa2VlcF9wcm9wc3ERiVgIAAAAbWV0YWRh
dGFxEn1xE1gIAAAAbmV3X2F4aXNxFFgHAAAAZmVhdHVyZXEVWAgAAABvbGRfYXhpc3EWWAcAAABm
ZWF0dXJlcRdYDAAAAG9ubHlfc2lnbmFsc3EYiFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEZY3Np
cApfdW5waWNrbGVfdHlwZQpxGlgMAAAAUHlRdDUuUXRDb3JlcRtYCgAAAFFCeXRlQXJyYXlxHENC
AdnQywADAAAAAAMLAAABFgAABHQAAALTAAADDAAAATUAAARzAAAC0gAAAAAAAAAAB4AAAAMMAAAB
NQAABHMAAALScR2FcR6HcR9ScSBYDgAAAHNldF9icmVha3BvaW50cSGJWAkAAAB2ZXJib3NpdHlx
IksAdS4=
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node4",
            "data",
            "node5",
            "data"
        ],
        [
            "node1",
            "data",
            "node6",
            "data"
        ],
        [
            "node5",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node2",
            "data"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node10",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node1",
            "data"
        ],
        [
            "node7",
            "data",
            "node14",
            "data"
        ],
        [
            "node13",
            "data",
            "node4",
            "data"
        ],
        [
            "node2",
            "data",
            "node13",
            "data"
        ],
        [
            "node14",
            "data",
            "node11",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "train_down": 1,
                        "train_left": 2,
                        "train_neutral": 4,
                        "train_right": 0,
                        "train_up": 3
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "5dd297c6-3527-44cc-8d9c-e9fd056d281d"
        },
        "node10": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 300
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "5b592e61-c68d-443a-8f8f-88e17443abf7"
        },
        "node11": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "auto_bar_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "font_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "43ad0a2c-2d36-472a-bed5-9a33f1064572"
        },
        "node12": {
            "class": "AccumulateCalibrationData",
            "module": "neuropype.nodes.machine_learning.AccumulateCalibrationData",
            "params": {
                "begin_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": "start_train"
                },
                "calibration_first": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "can_recalibrate": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "emit_predict_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "end_marker": {
                    "customized": true,
                    "type": "Port",
                    "value": "end_train"
                },
                "marker_mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "markers"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "eac7661a-841d-4d45-ae30-ea13989bca14"
        },
        "node13": {
            "class": "SourcePowerComodulation",
            "module": "neuropype.nodes.neural.SourcePowerComodulation",
            "params": {
                "cov_lambda": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.001
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "target_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                }
            },
            "uuid": "f33b15e7-6838-4bc8-b9e8-4e3a5d7f4e1a"
        },
        "node14": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "right",
                        "down",
                        "left",
                        "up",
                        "neutral"
                    ]
                },
                "join_format": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "{new}"
                },
                "keep_other_arrays": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "bdb20acb-3ba2-448d-8401-1c6be90f21e9"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "online_epoching": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "sliding"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.5,
                        4.5
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0f5ff239-a53f-4a06-b971-ed4d37913264"
        },
        "node3": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(make sure to never use same string more than once on network)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "openbci_output"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "8ddaae7c-d55c-480e-bce9-0050a663d22a"
        },
        "node4": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "cde23f44-97da-41be-8cec-9302f9dfa51c"
        },
        "node5": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "be9bbb74-a32d-4959-b75a-f5c69399b6b6"
        },
        "node6": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": "0...7"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "87a36776-413b-4b9f-801d-a61a7598937d"
        },
        "node7": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "balanced"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "l1_ratios": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "9029bb0d-142a-4467-bbe9-6ebfaf946316"
        },
        "node8": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        6,
                        7,
                        30,
                        32
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "23c6d71a-5a0a-4f08-8394-e2c3101ecfe9"
        },
        "node9": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "FC5",
                        "FC1",
                        "CP5",
                        "CP1",
                        "CP2",
                        "CP6",
                        "FC2",
                        "FC6"
                    ]
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='openbci_markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='openbci_eeg'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2b322603-70a1-471f-ab92-aac73308f79b"
        }
    },
    "version": 1.1
}</patch>
</scheme>
