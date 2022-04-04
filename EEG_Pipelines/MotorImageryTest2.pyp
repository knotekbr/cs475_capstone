<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline predicts imagined motor actions using neural oscillatory pattern classification. The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations.&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import SET”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Set”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here where only data from the last 6 channels are used.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 6-30 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Common Spatial Patterns (CSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. Here we use misclassification rate (MCR)." title="Simple Motor Imagery Prediction with CSP" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(453.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="a6b7f793-cc95-43ca-925a-0e7979089783" version="1.0.1" />
		<node id="1" name="Segmentation" position="(756.0, 275.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="38847143-17e5-4c74-adc9-96d0da8b4acd" version="1.0.2" />
		<node id="2" name="LSL Output" position="(1369.0, 383.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="f587762a-5798-4d63-a8e8-bed31e98ea0e" version="1.4.2" />
		<node id="3" name="Variance" position="(959.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="4ff414cf-0fdb-42e5-b1e5-f5b9993cbf51" version="1.0.0" />
		<node id="4" name="Logarithm" position="(1064.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="611668d1-2524-43df-8e38-23fc13628c90" version="1.0.0" />
		<node id="5" name="Select Range" position="(553.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="5be9403f-4416-4a42-8265-34474a46db58" version="1.1.0" />
		<node id="6" name="Logistic Regression" position="(1067.0, 126.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="1ef8c7ca-cbdc-41e6-ba71-d51ebb7ac630" version="1.1.0" />
		<node id="7" name="FIR Filter" position="(589.0, 320.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="8f086ef1-9180-4d30-b7ec-e189baf0e65b" version="1.1.0" />
		<node id="8" name="LSL Input" position="(137.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="d2847ccb-5c40-412c-aac6-554b1b24be30" version="1.5.1" />
		<node id="9" name="Dejitter Timestamps" position="(243.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="06d33181-c3d3-4c87-8294-f57f4d666168" version="1.0.0" />
		<node id="10" name="Streaming Bar Plot" position="(1366.0, 280.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="77ad20bc-e43b-4e68-8b2e-0f6019ccbda3" version="1.0.3" />
		<node id="11" name="Source Power Comodulation" position="(859.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.neural.owsourcepowercomodulation.OWSourcePowerComodulation" title="Source Power Comodulation" uuid="0d5457b9-33e4-4f34-9dc8-caba6ad8b8d6" version="1.0.0" />
		<node id="12" name="Override Axis" position="(1270.0, 280.0)" project_name="NeuroPype" qualified_name="widgets.neural.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="9d29bdf4-8092-412f-8890-d8e7ec463110" version="1.4.2" />
		<node id="13" name="Inject Calibration Data" position="(344.0, 207.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="ff39f9da-c909-423e-9828-8c985d0035ef" version="1.0.0" />
		<node id="14" name="Import XDF" position="(224.0, 83.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="26a40544-fd9c-4509-9783-c104847dfdc8" version="1.2.1" />
		<node id="15" name="Print To Console" position="(1279.0, 432.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="d0009cf5-2821-4bbb-8aa3-c8525b7dd1e2" version="1.1.0" />
		<node id="16" name="Linear Discriminant Analysis" position="(1162.0, 313.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="99f6ddc2-ba47-46d6-8578-7f6506487a8d" version="1.1.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="7" sink_channel="Streaming Data" sink_node_id="13" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="9" sink_channel="Calib Data" sink_node_id="13" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="7" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKIWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYCwAAAHRyYWluX3Jp
Z2h0cQdLAFgKAAAAdHJhaW5fZG93bnEISwFYCgAAAHRyYWluX2xlZnRxCUsCWAgAAAB0cmFpbl91
cHEKSwNYDQAAAHRyYWluX25ldXRyYWxxC0sEdVgOAAAAbWFwcGluZ19mb3JtYXRxDFgGAAAAY29t
cGF0cQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3Vu
cGlja2xlX3R5cGUKcRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsA
AwAAAAABkQAAAYsAAAL6AAAC+AAAAZIAAAGqAAAC+QAAAvcAAAAAAAAAAAeAAAABkgAAAaoAAAL5
AAAC93EUhXEVh3EWUnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgRAAAAc3VwcG9ydF93aWxkY2Fy
ZHNxGYlYCwAAAHVzZV9udW1iZXJzcRqJWAcAAAB2ZXJib3NlcRuJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYBwAAAHNsaWRpbmdx
BlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNzaXAKX3Vu
cGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtDQgHZ0MsA
AwAAAAABuQAAAaAAAAMiAAAC/QAAAboAAAG/AAADIQAAAvwAAAAAAAAAAAeAAAABugAAAb8AAAMh
AAAC/HEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFY
DgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETXXEUKEc/4AAAAAAAAEsCZVgH
AAAAdmVyYm9zZXEViXUu
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
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwsAAAGBAAAEdAAAAnkAAAMMAAABpwAABHMAAAJ4AAAA
AAAAAAAHgAAAAwwAAAGnAAAEcwAAAnhxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
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
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADCwAAAXwAAAR0AAACpgAAAwwA
AAGiAAAEcwAAAqUAAAAAAAAAAAeAAAADDAAAAaIAAARzAAACpXELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gFAAAAMC4uLjdxEFgOAAAAc2V0X2JyZWFrcG9pbnRxEYlYBAAAAHVuaXRxElgHAAAA
aW5kaWNlc3ETdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYCAAA
AGJhbGFuY2VkcQVYCgAAAGNvbmRfZmllbGRxBlgLAAAAVGFyZ2V0VmFsdWVxB1gQAAAAZG9udF9y
ZXNldF9tb2RlbHEIiVgQAAAAZHVhbF9mb3JtdWxhdGlvbnEJiVgPAAAAZmVhdHVyZV9zY2FsaW5n
cQpYBAAAAG5vbmVxC1gMAAAAaW5jbHVkZV9iaWFzcQyIWA8AAABpbml0aWFsaXplX29uY2VxDYhY
CQAAAGwxX3JhdGlvc3EOWA0AAAAodXNlIGRlZmF1bHQpcQ9YCAAAAG1heF9pdGVycRBLZFgIAAAA
bWV0YWRhdGFxEX1xElgKAAAAbXVsdGljbGFzc3ETWAQAAABhdXRvcRRYCQAAAG51bV9mb2xkc3EV
SwZYCAAAAG51bV9qb2JzcRZLAVgNAAAAcHJvYmFiaWxpc3RpY3EXiFgLAAAAcmFuZG9tX3NlZWRx
GE05MFgLAAAAcmVndWxhcml6ZXJxGVgCAAAAbDJxGlgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEb
Y3NpcApfdW5waWNrbGVfdHlwZQpxHFgMAAAAUHlRdDUuUXRDb3JlcR1YCgAAAFFCeXRlQXJyYXlx
HkNCAdnQywADAAAAAAKDAAAAdAAAA/QAAANFAAAChAAAAJMAAAPzAAADRAAAAAAAAAAAB4AAAAKE
AAAAkwAAA/MAAANEcR+FcSCHcSFScSJYDQAAAHNlYXJjaF9tZXRyaWNxI1gIAAAAYWNjdXJhY3lx
JFgOAAAAc2V0X2JyZWFrcG9pbnRxJYlYBgAAAHNvbHZlcnEmWAUAAABsYmZnc3EnWAkAAAB0b2xl
cmFuY2VxKEc/Gjbi6xxDLVgJAAAAdmVyYm9zaXR5cSlLAHUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAACjQAAAaEA
AAP2AAADNQAAAo4AAAHHAAAD9QAAAzQAAAAAAAAAAAeAAAACjgAAAccAAAP1AAADNHEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gSAAAA
bmFtZT0nb3BlbmJjaV9lZWcncRhYBwAAAHJlY292ZXJxGYhYFAAAAHJlc29sdmVfbWluaW11bV90
aW1lcRpHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2NzaXAKX3VucGlja2xlX3R5
cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5DQgHZ0MsAAwAAAAAEsQAA
AKAAAAYaAAADIAAABLIAAADGAAAGGQAAAx8AAAAAAAAAAAeAAAAEsgAAAMYAAAYZAAADH3EfhXEg
h3EhUnEiWA4AAABzZXRfYnJlYWtwb2ludHEjiXUu
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
		<properties format="pickle" node_id="11">gAN9cQAoWAoAAABjb3ZfbGFtYmRhcQFHP1BiTdLxqfxYDwAAAGluaXRpYWxpemVfb25jZXECiFgI
AAAAbWV0YWRhdGFxA31xBFgDAAAAbm9mcQVLBVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3Np
cApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNC
AdnQywADAAAAAAMLAAABfAAABHQAAAKLAAADDAAAAZsAAARzAAACigAAAAAAAAAAB4AAAAMMAAAB
mwAABHMAAAKKcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAwAAAB0YXJnZXRfZmll
bGRxD1gLAAAAVGFyZ2V0VmFsdWVxEHUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
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
		<properties format="pickle" node_id="13">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAMLAAABigAABHQAAAJMAAADDAAA
AbAAAARzAAACSwAAAAAAAAAAB4AAAAMMAAABsAAABHMAAAJLcQiFcQmHcQpScQtYDgAAAHNldF9i
cmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWFAAAABDOi9Vc2Vycy9rbm90ZS9Eb2N1bWVudHMvV29ya3NwYWNlL2NzNDc1
X2NhcHN0b25lL0VFR19SZWNvcmRpbmdzL0JyYW5kb25fMjUwLnhkZnEIWBMAAABoYW5kbGVfY2xv
Y2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9y
ZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YCAAAAG1l
dGFkYXRhcQ59cQ9YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EQiVgOAAAAcmV0YWluX3N0cmVhbXNx
EWgNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRJjc2lwCl91bnBpY2tsZV90eXBlCnETWAwAAABQ
eVF0NS5RdENvcmVxFFgKAAAAUUJ5dGVBcnJheXEVQ0IB2dDLAAMAAAAAAwsAAADoAAAEdAAAAvUA
AAMMAAABBwAABHMAAAL0AAAAAAAAAAAHgAAAAwwAAAEHAAAEcwAAAvRxFoVxF4dxGFJxGVgOAAAA
c2V0X2JyZWFrcG9pbnRxGolYCwAAAHVzZV9jYWNoaW5ncRuJWA8AAAB1c2Vfc3RyZWFtbmFtZXNx
HIlYBwAAAHZlcmJvc2VxHYl1Lg==
</properties>
		<properties format="literal" node_id="15">{'metadata': {}, 'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_props': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgKAAAAY29uZF9m
aWVsZHEDWAsAAABUYXJnZXRWYWx1ZXEEWBgAAABkaW1lbnNpb25hbGl0eV9yZWR1Y3Rpb25xBWgC
WBAAAABkb250X3Jlc2V0X21vZGVscQaJWBQAAABmZWF0dXJlX3NlbF9ncm91cF9vcHEHWAMAAABt
YXhxCFgWAAAAZmVhdHVyZV9zZWxfZ3JvdXBfc2l6ZXEJSwFYEQAAAGZlYXR1cmVfc2VsZWN0aW9u
cQpYBAAAAG5vbmVxC1gPAAAAaHViZXJfdGhyZXNob2xkcQxLAFgPAAAAaW5pdGlhbGl6ZV9vbmNl
cQ2IWBIAAABtYXhfZmVhdHVyZV9zZWxlY3RxDmgCWAgAAABtZXRhZGF0YXEPfXEQWAkAAABudW1f
Zm9sZHNxEUsFWAgAAABudW1fam9ic3ESSwFYDQAAAHByb2JhYmlsaXN0aWNxE4hYDAAAAHJvYnVz
dF9nYW1tYXEUXXEVKEsBRz/0AAAAAAAARz/4AAAAAAAASwJHQAQAAAAAAABLBUsKSxRLKEtQS6Bl
WBgAAAByb2J1c3RfbWF4X2NvbnRhbWluYXRpb25xFmgCWA0AAAByb2J1c3RfbWV0aG9kcRdYBAAA
AG5vbmVxGFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEZY3NpcApfdW5waWNrbGVfdHlwZQpxGlgM
AAAAUHlRdDUuUXRDb3JlcRtYCgAAAFFCeXRlQXJyYXlxHENCAdnQywADAAAAAALnAAAAmAAABJgA
AANRAAAC6AAAALcAAASXAAADUAAAAAAAAAAAB4AAAALoAAAAtwAABJcAAANQcR2FcR6HcR9ScSBY
DQAAAHNlYXJjaF9tZXRyaWNxIVgIAAAAYWNjdXJhY3lxIlgOAAAAc2V0X2JyZWFrcG9pbnRxI4lY
CQAAAHNocmlua2FnZXEkWAQAAABhdXRvcSVYBgAAAHNvbHZlcnEmWAUAAABlaWdlbnEnWAkAAAB0
b2xlcmFuY2VxKEc/Gjbi6xxDLVgJAAAAdmVyYm9zaXR5cSlLAHUu
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
            "node6",
            "data",
            "node8",
            "data"
        ],
        [
            "node9",
            "data",
            "node10",
            "data"
        ],
        [
            "node12",
            "data",
            "node4",
            "data"
        ],
        [
            "node2",
            "data",
            "node12",
            "data"
        ],
        [
            "node13",
            "data",
            "node11",
            "data"
        ],
        [
            "node10",
            "data",
            "node14",
            "streaming_data"
        ],
        [
            "node14",
            "data",
            "node1",
            "data"
        ],
        [
            "node15",
            "data",
            "node14",
            "calib_data"
        ],
        [
            "node5",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node13",
            "data"
        ],
        [
            "node17",
            "data",
            "node16",
            "data"
        ],
        [
            "node8",
            "data",
            "node2",
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "a6b7f793-cc95-43ca-925a-0e7979089783"
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
            "uuid": "06d33181-c3d3-4c87-8294-f57f4d666168"
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
            "uuid": "77ad20bc-e43b-4e68-8b2e-0f6019ccbda3"
        },
        "node12": {
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
                    "value": 5
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
            "uuid": "0d5457b9-33e4-4f34-9dc8-caba6ad8b8d6"
        },
        "node13": {
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
            "uuid": "9d29bdf4-8092-412f-8890-d8e7ec463110"
        },
        "node14": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
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
            "uuid": "ff39f9da-c909-423e-9828-8c985d0035ef"
        },
        "node15": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/knote/Documents/Workspace/cs475_capstone/EEG_Recordings/Brandon_250.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
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
            "uuid": "26a40544-fd9c-4509-9783-c104847dfdc8"
        },
        "node16": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d0009cf5-2821-4bbb-8aa3-c8525b7dd1e2"
        },
        "node17": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dimensionality_reduction": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_sel_group_op": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "max"
                },
                "feature_sel_group_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "feature_selection": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "huber_threshold": {
                    "customized": false,
                    "type": "Port",
                    "value": 0
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_feature_select": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
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
                "robust_gamma": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        1,
                        1.25,
                        1.5,
                        2,
                        2.5,
                        5,
                        10,
                        20,
                        40,
                        80,
                        160
                    ]
                },
                "robust_max_contamination": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "robust_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
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
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
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
            "uuid": "99f6ddc2-ba47-46d6-8578-7f6506487a8d"
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
                        2
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "38847143-17e5-4c74-adc9-96d0da8b4acd"
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
            "uuid": "f587762a-5798-4d63-a8e8-bed31e98ea0e"
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
            "uuid": "4ff414cf-0fdb-42e5-b1e5-f5b9993cbf51"
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
            "uuid": "611668d1-2524-43df-8e38-23fc13628c90"
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
            "uuid": "5be9403f-4416-4a42-8265-34474a46db58"
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
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
                    "customized": true,
                    "type": "IntPort",
                    "value": 6
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
            "uuid": "1ef8c7ca-cbdc-41e6-ba71-d51ebb7ac630"
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
            "uuid": "8f086ef1-9180-4d30-b7ec-e189baf0e65b"
        },
        "node9": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
            "uuid": "d2847ccb-5c40-412c-aac6-554b1b24be30"
        }
    },
    "version": 1.1
}</patch>
</scheme>
