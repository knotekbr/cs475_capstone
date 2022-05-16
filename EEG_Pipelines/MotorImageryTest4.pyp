<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline is used to classify four types of motion (and a neutral state) in order to translate a user's physical commands into game inputs. The pipeline can be divided into 4 sections:&#10;&#10;1. Data Acquisition&#10;&#10;2. Data Preprocessing&#10;&#10;3. Classification&#10;&#10;4. Output" title="MindGames Motor Classification" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(608.0, 189.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="77e2824d-aae7-49cd-821b-8384c4bc94e8" version="1.0.1" />
		<node id="1" name="Segmentation" position="(705.0, 341.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="c78e6614-c5c8-4e2a-8864-0ad884b14799" version="1.0.2" />
		<node id="2" name="Select Range" position="(706.0, 189.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="f20a244b-e8aa-4b1c-8ecc-a6bf959118e2" version="1.1.0" />
		<node id="3" name="FIR Filter" position="(610.0, 341.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="c0579ac6-e84e-423a-a597-d08045e4c247" version="1.1.0" />
		<node id="4" name="LSL Input" position="(193.0, 197.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="4b7f4e28-6586-44af-afb1-9f7cc4134749" version="1.5.1" />
		<node id="5" name="Dejitter Timestamps" position="(292.0, 197.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="22675cdf-a43d-4ef2-b087-8647716d7339" version="1.0.0" />
		<node id="6" name="Streaming Bar Plot" position="(1293.0, 450.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="47f547d6-e067-42d9-906a-06f9df542ae7" version="1.0.3" />
		<node id="7" name="Override Axis" position="(1194.0, 450.0)" project_name="NeuroPype" qualified_name="widgets.neural.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="87191825-668f-4281-a574-9d9e14852366" version="1.4.2" />
		<node id="8" name="Inject Calibration Data" position="(505.0, 189.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="62bd1b48-72ee-46e1-b185-98a0d413145b" version="1.0.0" />
		<node id="9" name="Import XDF" position="(192.0, 101.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="5158cdf5-6c4c-4a5e-b10e-db7e63b4c363" version="1.2.1" />
		<node id="10" name="Moving Average" position="(1080.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owmovingaverage.OWMovingAverage" title="Moving Average" uuid="06062a70-04a5-4905-8119-27bcbd1d93cf" version="1.1.0" />
		<node id="11" name="Source Power Comodulation" position="(612.0, 483.0)" project_name="NeuroPype" qualified_name="widgets.neural.owsourcepowercomodulation.OWSourcePowerComodulation" title="Source Power Comodulation" uuid="83785fdc-d2a8-42d0-9d76-c15ee79c8c1d" version="1.0.0" />
		<node id="12" name="Variance" position="(714.0, 483.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="7bb355dd-346b-4f58-961d-caea5c1934ca" version="1.0.0" />
		<node id="13" name="Logistic Regression" position="(972.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="5106aeff-0d7a-4e52-87b1-d27452d022e5" version="1.1.0" />
		<node id="14" name="Logarithm" position="(811.0, 483.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="5d65a6f4-89db-42b4-bb6b-9fce5af1f3db" version="1.0.0" />
		<node id="15" name="LSL Output" position="(1187.0, 341.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="9aa9b04a-6b4b-4bda-b849-84ac53e47f4f" version="1.4.2" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="4" sink_channel="Streaming Data" sink_node_id="8" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="6" sink_channel="Calib Data" sink_node_id="8" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="10" />
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
AwAAAAABugAAAb8AAAMhAAAC/AAAAboAAAG/AAADIQAAAvwAAAAAAAAAAAeAAAABugAAAb8AAAMh
AAAC/HEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1bHQpcRFY
DgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETXXEUKEc/4AAAAAAAAEsCZVgH
AAAAdmVyYm9zZXEViXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADCwAAAYMAAAR0AAACpgAAAwwA
AAGiAAAEcwAAAqUAAAAAAAAAAAeAAAADDAAAAaIAAARzAAACpXELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gFAAAAMC4uLjdxEFgOAAAAc2V0X2JyZWFrcG9pbnRxEYlYBAAAAHVuaXRxElgHAAAA
aW5kaWNlc3ETdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAACIwAAAVwA
AAOMAAAC6QAAAiQAAAF7AAADiwAAAugAAAAAAAAAAAeAAAACJAAAAXsAAAOLAAAC6HEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQz
MnEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgAAAAAcQlYDAAAAG1heF9ibG9ja2xlbnEKTQAEWAoAAABtYXhfYnVmbGVu
cQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9y
YXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21pdF9kZXNjcRGJWA8AAABwcmVhbGxvY19i
dWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0AAABwcm9jX2Rlaml0dGVycRSJWA8AAABw
cm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFkc2FmZXEWiVgFAAAAcXVlcnlxF1gSAAAA
bmFtZT0nb3BlbmJjaV9lZWcncRhYBwAAAHJlY292ZXJxGYhYFAAAAHJlc29sdmVfbWluaW11bV90
aW1lcRpHP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxG2NzaXAKX3VucGlja2xlX3R5
cGUKcRxYDAAAAFB5UXQ1LlF0Q29yZXEdWAoAAABRQnl0ZUFycmF5cR5DQgHZ0MsAAwAAAAACqwAA
AJ0AAAQUAAADFgAAAqwAAAC8AAAEEwAAAxUAAAAAAAAAAAeAAAACrAAAALwAAAQTAAADFXEfhXEg
h3EhUnEiWA4AAABzZXRfYnJlYWtwb2ludHEjiXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWAgAAABtZXRhZGF0YXEEfXEFWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NS5RdENvcmVxCFgKAAAAUUJ5
dGVBcnJheXEJQ0IB2dDLAAMAAAAAAwsAAAF8AAAEdAAAAn8AAAMMAAABmwAABHMAAAJ+AAAAAAAA
AAAHgAAAAwwAAAGbAAAEcwAAAn5xCoVxC4dxDFJxDVgOAAAAc2V0X2JyZWFrcG9pbnRxDolYDgAA
AHdhcm11cF9zYW1wbGVzcQ9K/////3Uu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWA8AAABhdXRvX2Jhcl9jb2xvcnNxAolYBAAAAGF4
aXNxA1gHAAAAZmVhdHVyZXEEWBAAAABiYWNrZ3JvdW5kX2NvbG9ycQVYBwAAACNGRkZGRkZxBlgJ
AAAAYmFyX2NvbG9ycQdYAQAAAGJxCFgJAAAAYmFyX3dpZHRocQlHP+zMzMzMzM1YCQAAAGZvbnRf
c2l6ZXEKR0AkAAAAAAAAWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksyTbwCTfQBZVgOAAAAaW5z
dGFuY2VfZmllbGRxDVgNAAAAKHVzZSBkZWZhdWx0KXEOWA4AAABsYWJlbF9yb3RhdGlvbnEPWAoA
AABob3Jpem9udGFscRBYCAAAAG1ldGFkYXRhcRF9cRJYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
E2NzaXAKX3VucGlja2xlX3R5cGUKcRRYDAAAAFB5UXQ1LlF0Q29yZXEVWAoAAABRQnl0ZUFycmF5
cRZDQgHZ0MsAAwAAAAADCwAAAPIAAAR0AAADJQAAAwwAAAERAAAEcwAAAyQAAAAAAAAAAAeAAAAD
DAAAAREAAARzAAADJHEXhXEYh3EZUnEaWA4AAABzZXRfYnJlYWtwb2ludHEbiVgMAAAAc2hvd190
b29sYmFycRyJWAsAAABzdHJlYW1fbmFtZXEdWA0AAAAodXNlIGRlZmF1bHQpcR5YBQAAAHRpdGxl
cR9YDgAAAENsYXNzaWZpY2F0aW9ucSBYEQAAAHVzZV9sYXN0X2luc3RhbmNlcSGIWAcAAAB2ZXJi
b3NlcSKJWAgAAAB5X2xpbWl0c3EjXXEkKEsASwFldS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWAAAAABxBVgIAAAAZGVj
aW1hbHNxBksDWAkAAABpbml0X2RhdGFxB11xCChYBQAAAHJpZ2h0cQlYBAAAAGRvd25xClgEAAAA
bGVmdHELWAIAAAB1cHEMWAcAAABuZXV0cmFscQ1lWAsAAABqb2luX2Zvcm1hdHEOWAUAAAB7bmV3
fXEPWBEAAABrZWVwX290aGVyX2FycmF5c3EQiVgKAAAAa2VlcF9wcm9wc3ERiVgIAAAAbWV0YWRh
dGFxEn1xE1gIAAAAbmV3X2F4aXNxFFgHAAAAZmVhdHVyZXEVWAgAAABvbGRfYXhpc3EWWAcAAABm
ZWF0dXJlcRdYDAAAAG9ubHlfc2lnbmFsc3EYiFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEZY3Np
cApfdW5waWNrbGVfdHlwZQpxGlgMAAAAUHlRdDUuUXRDb3JlcRtYCgAAAFFCeXRlQXJyYXlxHENC
AdnQywADAAAAAAMLAAABFgAABHQAAAL7AAADDAAAATUAAARzAAAC+gAAAAAAAAAAB4AAAAMMAAAB
NQAABHMAAAL6cR2FcR6HcR9ScSBYDgAAAHNldF9icmVha3BvaW50cSGJWAkAAAB2ZXJib3NpdHlx
IksAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAMLAAABkQAABHQAAAJMAAADDAAA
AbAAAARzAAACSwAAAAAAAAAAB4AAAAMMAAABsAAABHMAAAJLcQiFcQmHcQpScQtYDgAAAHNldF9i
cmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWFIAAABDOi9Vc2Vycy9rbm90ZS9Eb2N1bWVudHMvV29ya3NwYWNlL2NzNDc1
X2NhcHN0b25lL0VFR19SZWNvcmRpbmdzL0JyYW5kb25fZmluYWwueGRmcQhYEwAAAGhhbmRsZV9j
bG9ja19yZXNldHNxCYhYEQAAAGhhbmRsZV9jbG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVy
X3JlbW92YWxxC4hYDgAAAG1heF9tYXJrZXJfbGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgIAAAA
bWV0YWRhdGFxDn1xD1gSAAAAcmVvcmRlcl90aW1lc3RhbXBzcRCJWA4AAAByZXRhaW5fc3RyZWFt
c3ERaA1YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAA
AFB5UXQ1LlF0Q29yZXEUWAoAAABRQnl0ZUFycmF5cRVDQgHZ0MsAAwAAAAADCwAAAOEAAAR0AAAC
9QAAAwwAAAEHAAAEcwAAAvQAAAAAAAAAAAeAAAADDAAAAQcAAARzAAAC9HEWhXEXh3EYUnEZWA4A
AABzZXRfYnJlYWtwb2ludHEaiVgLAAAAdXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1l
c3EciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgLAAAAaWdub3JlX25hbnNxA4lYCAAAAG1ldGFk
YXRhcQR9cQVYBQAAAG9yZGVycQZHP+AAAAAAAABYCgAAAG9yZGVyX3VuaXRxB1gHAAAAc2Vjb25k
c3EIWAsAAABvdXRwdXRfbmFuc3EJiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEKY3NpcApfdW5w
aWNrbGVfdHlwZQpxC1gMAAAAUHlRdDUuUXRDb3JlcQxYCgAAAFFCeXRlQXJyYXlxDUNCAdnQywAD
AAAAAAMLAAABZwAABHQAAAKCAAADDAAAAYYAAARzAAACgQAAAAAAAAAAB4AAAAMMAAABhgAABHMA
AAKBcQ6FcQ+HcRBScRFYDgAAAHNldF9icmVha3BvaW50cRKJdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAoAAABjb3ZfbGFtYmRhcQFHP1BiTdLxqfxYDwAAAGluaXRpYWxpemVfb25jZXECiFgI
AAAAbWV0YWRhdGFxA31xBFgDAAAAbm9mcQVLBVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3Np
cApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNC
AdnQywADAAAAAAMEAAABbAAABHsAAAKCAAADBQAAAZIAAAR6AAACgQAAAAAAAAAAB4AAAAMFAAAB
kgAABHoAAAKBcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAwAAAB0YXJnZXRfZmll
bGRxD1gLAAAAVGFyZ2V0VmFsdWVxEHUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwsAAAGAAAAEdAAAAmkAAAMMAAABnwAABHMAAAJoAAAA
AAAAAAAHgAAAAwwAAAGfAAAEcwAAAmhxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYDQAA
ACh1c2UgZGVmYXVsdClxBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABk
b250X3Jlc2V0X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWA8AAABmZWF0dXJlX3Nj
YWxpbmdxClgEAAAAbm9uZXELWAwAAABpbmNsdWRlX2JpYXNxDIhYDwAAAGluaXRpYWxpemVfb25j
ZXENiFgJAAAAbDFfcmF0aW9zcQ5oBVgIAAAAbWF4X2l0ZXJxD0tkWAgAAABtZXRhZGF0YXEQfXER
WAoAAABtdWx0aWNsYXNzcRJYBAAAAGF1dG9xE1gJAAAAbnVtX2ZvbGRzcRRLCFgIAAAAbnVtX2pv
YnNxFUsBWA0AAABwcm9iYWJpbGlzdGljcRaIWAsAAAByYW5kb21fc2VlZHEXTTkwWAsAAAByZWd1
bGFyaXplcnEYWAIAAABsMnEZWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRpjc2lwCl91bnBpY2ts
ZV90eXBlCnEbWAwAAABQeVF0NS5RdENvcmVxHFgKAAAAUUJ5dGVBcnJheXEdQ0IB2dDLAAMAAAAA
AucAAACTAAAEmAAAA2sAAALoAAAAuQAABJcAAANqAAAAAAAAAAAHgAAAAugAAAC5AAAElwAAA2px
HoVxH4dxIFJxIVgNAAAAc2VhcmNoX21ldHJpY3EiWAgAAABhY2N1cmFjeXEjWA4AAABzZXRfYnJl
YWtwb2ludHEkiVgGAAAAc29sdmVycSVYBAAAAGF1dG9xJlgJAAAAdG9sZXJhbmNlcSdHPxo24usc
Qy1YCQAAAHZlcmJvc2l0eXEoSwB1Lg==
</properties>
		<properties format="literal" node_id="14">{'base': '(use default)', 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAAMLAAAAwgAABHQAAAMnAAADDAAAAOEAAARzAAADJgAAAAAAAAAAB4AA
AAMMAAAA4QAABHMAAAMmcRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiVgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcaAlYBQAA
AHNyYXRlcR1YDQAAACh1c2UgZGVmYXVsdClxHlgLAAAAc3RyZWFtX25hbWVxH1gOAAAAb3BlbmJj
aV9wYXJzZWRxIFgLAAAAc3RyZWFtX3R5cGVxIVgHAAAAQ29udHJvbHEiWBMAAAB1c2VfZGF0YV90
aW1lc3RhbXBzcSOIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSSJdS4=
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
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node8",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node9",
            "streaming_data"
        ],
        [
            "node9",
            "data",
            "node1",
            "data"
        ],
        [
            "node10",
            "data",
            "node9",
            "calib_data"
        ],
        [
            "node4",
            "data",
            "node2",
            "data"
        ],
        [
            "node12",
            "data",
            "node13",
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
            "node15",
            "data"
        ],
        [
            "node15",
            "data",
            "node14",
            "data"
        ],
        [
            "node14",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node16",
            "data"
        ],
        [
            "node11",
            "data",
            "node8",
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
            "uuid": "77e2824d-aae7-49cd-821b-8384c4bc94e8"
        },
        "node10": {
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
                    "value": "C:/Users/knote/Documents/Workspace/cs475_capstone/EEG_Recordings/Brandon_final.xdf"
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
            "uuid": "5158cdf5-6c4c-4a5e-b10e-db7e63b4c363"
        },
        "node11": {
            "class": "MovingAverage",
            "module": "neuropype.nodes.signal_processing.MovingAverage",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "order": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "order_unit": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "seconds"
                },
                "output_nans": {
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
            "uuid": "06062a70-04a5-4905-8119-27bcbd1d93cf"
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
            "uuid": "83785fdc-d2a8-42d0-9d76-c15ee79c8c1d"
        },
        "node13": {
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
            "uuid": "7bb355dd-346b-4f58-961d-caea5c1934ca"
        },
        "node14": {
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
                    "customized": false,
                    "type": "Port",
                    "value": null
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
                    "value": 8
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
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
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
            "uuid": "5106aeff-0d7a-4e52-87b1-d27452d022e5"
        },
        "node15": {
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
            "uuid": "5d65a6f4-89db-42b4-bb6b-9fce5af1f3db"
        },
        "node16": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "openbci_parsed"
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
            "uuid": "9aa9b04a-6b4b-4bda-b849-84ac53e47f4f"
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
            "uuid": "c78e6614-c5c8-4e2a-8864-0ad884b14799"
        },
        "node3": {
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
            "uuid": "f20a244b-e8aa-4b1c-8ecc-a6bf959118e2"
        },
        "node4": {
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
            "uuid": "c0579ac6-e84e-423a-a597-d08045e4c247"
        },
        "node5": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "C3",
                        "C4",
                        "T5",
                        "T6",
                        "O1",
                        "O2"
                    ]
                },
                "data_dtype": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "float32"
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
            "uuid": "4b7f4e28-6586-44af-afb1-9f7cc4134749"
        },
        "node6": {
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
            "uuid": "22675cdf-a43d-4ef2-b087-8647716d7339"
        },
        "node7": {
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
            "uuid": "47f547d6-e067-42d9-906a-06f9df542ae7"
        },
        "node8": {
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
            "uuid": "87191825-668f-4281-a574-9d9e14852366"
        },
        "node9": {
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
            "uuid": "62bd1b48-72ee-46e1-b185-98a0d413145b"
        }
    },
    "version": 1.1
}</patch>
</scheme>
