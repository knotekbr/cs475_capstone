<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline is used to classify four types of motion (and a neutral state) in order to translate a user's physical commands into game inputs. The pipeline can be divided into 4 sections:&#10;&#10;1. Data Acquisition&#10;&#10;2. Data Preprocessing&#10;&#10;3. Classification&#10;&#10;4. Output" title="MindGames Motor Classification" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(453.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="a0f45c75-a100-44c8-991a-f328e7c97db5" version="1.0.1" />
		<node id="1" name="Segmentation" position="(657.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="4cc3c7fe-bd6b-40bd-8773-ffee00f7ebea" version="1.0.2" />
		<node id="2" name="Variance" position="(866.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="b66c9759-8f71-4321-a370-e445e00ff902" version="1.0.0" />
		<node id="3" name="Logarithm" position="(969.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="091ab53f-6555-4599-a264-02da915161b2" version="1.0.0" />
		<node id="4" name="Select Range" position="(553.0, 204.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="dbc3a6de-d9ff-4630-80fc-a9128d3d6971" version="1.1.0" />
		<node id="5" name="FIR Filter" position="(457.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="7f00e191-bb7a-4146-a860-6466ba710999" version="1.1.0" />
		<node id="6" name="LSL Input" position="(33.0, 215.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="fcd2c644-1466-44ad-80bb-9e042c168f52" version="1.5.1" />
		<node id="7" name="Dejitter Timestamps" position="(132.0, 215.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="eb26ef7a-9300-43b1-8c4d-ea034169af45" version="1.0.0" />
		<node id="8" name="Streaming Bar Plot" position="(1258.0, 287.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="349b23ce-1446-4965-a76e-07600b6dfe62" version="1.0.3" />
		<node id="9" name="Source Power Comodulation" position="(762.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.neural.owsourcepowercomodulation.OWSourcePowerComodulation" title="Source Power Comodulation" uuid="6a76c16c-3b47-4ed6-b95d-e72e7906a171" version="1.0.0" />
		<node id="10" name="Override Axis" position="(1159.0, 287.0)" project_name="NeuroPype" qualified_name="widgets.neural.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="db89c238-da61-482e-9631-25254e1999f0" version="1.4.2" />
		<node id="11" name="Inject Calibration Data" position="(344.0, 207.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="51a7e931-7129-44d3-917f-3a805a045689" version="1.0.0" />
		<node id="12" name="Import XDF" position="(32.0, 119.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="bdda7119-a8c3-4042-9189-e3ae822ede8a" version="1.2.1" />
		<node id="13" name="Artifact Removal" position="(555.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" title="Artifact Removal" uuid="9cabb996-56e0-4513-85d5-62ddaf8d27c9" version="2.4.1" />
		<node id="14" name="Print To Console" position="(1263.0, 416.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="260c20a3-4a44-4d97-9778-6cdd45f9c36c" version="1.1.0" />
		<node id="15" name="Linear Discriminant Analysis" position="(1067.0, 349.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="5b13d9dd-bbba-4b27-b9c4-683d3ced66bf" version="1.1.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="7" sink_channel="Streaming Data" sink_node_id="11" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="9" sink_channel="Calib Data" sink_node_id="11" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="15" />
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
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWAgAAABtZXRhZGF0YXEFfXEGWBMAAABzYXZlZFdpZGdl
dEdlb21ldHJ5cQdjc2lwCl91bnBpY2tsZV90eXBlCnEIWAwAAABQeVF0NS5RdENvcmVxCVgKAAAA
UUJ5dGVBcnJheXEKQ0IB2dDLAAMAAAAAAwsAAAGIAAAEdAAAAnkAAAMMAAABpwAABHMAAAJ4AAAA
AAAAAAAHgAAAAwwAAAGnAAAEcwAAAnhxC4VxDIdxDVJxDlgOAAAAc2V0X2JyZWFrcG9pbnRxD4l1
Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgIAAAAbWV0YWRhdGFxA31xBFgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlwZQpxBlgMAAAAUHlRdDUu
UXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCENCAdnQywADAAAAAAMLAAABnwAABHQAAAJLAAADDAAA
Ab4AAARzAAACSgAAAAAAAAAAB4AAAAMMAAABvgAABHMAAAJKcQmFcQqHcQtScQxYDgAAAHNldF9i
cmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBQAAAHNwYWNlcQRYCAAAAG1ldGFkYXRhcQV9cQZY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxB2NzaXAKX3VucGlja2xlX3R5cGUKcQhYDAAAAFB5UXQ1
LlF0Q29yZXEJWAoAAABRQnl0ZUFycmF5cQpDQgHZ0MsAAwAAAAADCwAAAXwAAAR0AAACpgAAAwwA
AAGiAAAEcwAAAqUAAAAAAAAAAAeAAAADDAAAAaIAAARzAAACpXELhXEMh3ENUnEOWAkAAABzZWxl
Y3Rpb25xD1gFAAAAMC4uLjdxEFgOAAAAc2V0X2JyZWFrcG9pbnRxEYlYBAAAAHVuaXRxElgHAAAA
aW5kaWNlc3ETdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAACjQAAAaEA
AAP2AAADNQAAAo4AAAHHAAAD9QAAAzQAAAAAAAAAAAeAAAACjgAAAccAAAP1AAADNHEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
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
		<properties format="pickle" node_id="7">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWAgAAABtZXRhZGF0YXEEfXEFWBMAAABzYXZlZFdpZGdldEdl
b21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NS5RdENvcmVxCFgKAAAAUUJ5
dGVBcnJheXEJQ0IB2dDLAAMAAAAAAwsAAAF8AAAEdAAAAm0AAAMMAAABmwAABHMAAAJsAAAAAAAA
AAAHgAAAAwwAAAGbAAAEcwAAAmxxCoVxC4dxDFJxDVgOAAAAc2V0X2JyZWFrcG9pbnRxDolYDgAA
AHdhcm11cF9zYW1wbGVzcQ9K/////3Uu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWA8AAABhdXRvX2Jhcl9jb2xvcnNxAolYBAAAAGF4
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
		<properties format="pickle" node_id="9">gAN9cQAoWAoAAABjb3ZfbGFtYmRhcQFHP1BiTdLxqfxYDwAAAGluaXRpYWxpemVfb25jZXECiFgI
AAAAbWV0YWRhdGFxA31xBFgDAAAAbm9mcQVLBVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3Np
cApfdW5waWNrbGVfdHlwZQpxB1gMAAAAUHlRdDUuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUNC
AdnQywADAAAAAAMLAAABfAAABHQAAAKLAAADDAAAAZsAAARzAAACigAAAAAAAAAAB4AAAAMMAAAB
mwAABHMAAAKKcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAwAAAB0YXJnZXRfZmll
bGRxD1gLAAAAVGFyZ2V0VmFsdWVxEHUu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
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
		<properties format="pickle" node_id="11">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAMLAAABigAABHQAAAJMAAADDAAA
AbAAAARzAAACSwAAAAAAAAAAB4AAAAMMAAABsAAABHMAAAJLcQiFcQmHcQpScQtYDgAAAHNldF9i
cmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
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
		<properties format="pickle" node_id="13">gAN9cQAoWAEAAABhcQFYDQAAACh1c2UgZGVmYXVsdClxAlgBAAAAYnEDaAJYCgAAAGJsb2NrX3Np
emVxBGgCWA0AAABjYWxpYl9zZWNvbmRzcQVLLVgGAAAAY3V0b2ZmcQZHQB4AAAAAAABYDwAAAGVt
aXRfY2FsaWJfZGF0YXEHiFgHAAAAaW5pdF9vbnEIXXEJWAkAAABsb29rYWhlYWRxCmgCWBAAAABt
YXhfYmFkX2NoYW5uZWxzcQtHP8mZmZmZmZpYCAAAAG1heF9kaW1zcQxLAFgUAAAAbWF4X2Ryb3Bv
dXRfZnJhY3Rpb25xDUc/uZmZmZmZmlgHAAAAbWF4X21lbXEOTQABWAgAAABtZXRhZGF0YXEPfXEQ
WBIAAABtaW5fY2xlYW5fZnJhY3Rpb25xEUc/0AAAAAAAAFgVAAAAbWluX3JlcXVpcmVkX2NoYW5u
ZWxzcRJLAlgNAAAAcHJlc2VydmVfYmFuZHETaAJYCgAAAHJpZW1hbm5pYW5xFIhYEwAAAHNhdmVk
V2lkZ2V0R2VvbWV0cnlxFWNzaXAKX3VucGlja2xlX3R5cGUKcRZYDAAAAFB5UXQ1LlF0Q29yZXEX
WAoAAABRQnl0ZUFycmF5cRhDQgHZ0MsAAwAAAAADBQAAAGUAAAR7AAADhAAAAwYAAACEAAAEegAA
A4MAAAAAAAAAAAeAAAADBgAAAIQAAAR6AAADg3EZhXEah3EbUnEcWA4AAABzZXRfYnJlYWtwb2lu
dHEdiVgNAAAAc3RkZGV2X2N1dG9mZnEeSxRYCQAAAHN0ZXBfc2l6ZXEfRz/JmZmZmZmaWBAAAAB1
c2VfY2xlYW5fd2luZG93cSCIWAoAAAB1c2VfbGVnYWN5cSGIWBYAAAB3aW5kb3dfbGVuX2NsZWFu
d2luZG93cSJHP+AAAAAAAABYDQAAAHdpbmRvd19sZW5ndGhxI0c/4AAAAAAAAFgOAAAAd2luZG93
X292ZXJsYXBxJEc/5R64UeuFH1gaAAAAd2luZG93X292ZXJsYXBfY2xlYW53aW5kb3dxJUc/5R64
UeuFH1gRAAAAenNjb3JlX3RocmVzaG9sZHNxJl1xJyhK+////0sHZXUu
</properties>
		<properties format="literal" node_id="14">{'metadata': {}, 'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_props': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYCAAAAGJhbGFuY2VkcQJYCgAAAGNvbmRfZmllbGRx
A1gLAAAAVGFyZ2V0VmFsdWVxBFgYAAAAZGltZW5zaW9uYWxpdHlfcmVkdWN0aW9ucQVYDQAAACh1
c2UgZGVmYXVsdClxBlgQAAAAZG9udF9yZXNldF9tb2RlbHEHiVgUAAAAZmVhdHVyZV9zZWxfZ3Jv
dXBfb3BxCFgDAAAAbWF4cQlYFgAAAGZlYXR1cmVfc2VsX2dyb3VwX3NpemVxCksBWBEAAABmZWF0
dXJlX3NlbGVjdGlvbnELWAQAAABub25lcQxYDwAAAGh1YmVyX3RocmVzaG9sZHENSwBYDwAAAGlu
aXRpYWxpemVfb25jZXEOiFgSAAAAbWF4X2ZlYXR1cmVfc2VsZWN0cQ9oBlgIAAAAbWV0YWRhdGFx
EH1xEVgJAAAAbnVtX2ZvbGRzcRJLBVgIAAAAbnVtX2pvYnNxE0sBWA0AAABwcm9iYWJpbGlzdGlj
cRSIWAwAAAByb2J1c3RfZ2FtbWFxFV1xFihLAUc/9AAAAAAAAEc/+AAAAAAAAEsCR0AEAAAAAAAA
SwVLCksUSyhLUEugZVgYAAAAcm9idXN0X21heF9jb250YW1pbmF0aW9ucRdoBlgNAAAAcm9idXN0
X21ldGhvZHEYWAQAAABub25lcRlYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxGmNzaXAKX3VucGlj
a2xlX3R5cGUKcRtYDAAAAFB5UXQ1LlF0Q29yZXEcWAoAAABRQnl0ZUFycmF5cR1DQgHZ0MsAAwAA
AAAC6AAAALcAAASXAAADUAAAAugAAAC3AAAElwAAA1AAAAAAAAAAAAeAAAAC6AAAALcAAASXAAAD
UHEehXEfh3EgUnEhWA0AAABzZWFyY2hfbWV0cmljcSJYCAAAAGFjY3VyYWN5cSNYDgAAAHNldF9i
cmVha3BvaW50cSSJWAkAAABzaHJpbmthZ2VxJVgEAAAAYXV0b3EmWAYAAABzb2x2ZXJxJ1gFAAAA
ZWlnZW5xKFgJAAAAdG9sZXJhbmNlcSlHPxo24uscQy1YCQAAAHZlcmJvc2l0eXEqSwB1Lg==
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
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node1",
            "data",
            "node5",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node7",
            "data",
            "node8",
            "data"
        ],
        [
            "node10",
            "data",
            "node3",
            "data"
        ],
        [
            "node2",
            "data",
            "node10",
            "data"
        ],
        [
            "node11",
            "data",
            "node9",
            "data"
        ],
        [
            "node8",
            "data",
            "node12",
            "streaming_data"
        ],
        [
            "node12",
            "data",
            "node1",
            "data"
        ],
        [
            "node13",
            "data",
            "node12",
            "calib_data"
        ],
        [
            "node6",
            "data",
            "node14",
            "data"
        ],
        [
            "node14",
            "data",
            "node2",
            "data"
        ],
        [
            "node4",
            "data",
            "node16",
            "data"
        ],
        [
            "node16",
            "data",
            "node11",
            "data"
        ],
        [
            "node16",
            "data",
            "node15",
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
            "uuid": "a0f45c75-a100-44c8-991a-f328e7c97db5"
        },
        "node10": {
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
            "uuid": "6a76c16c-3b47-4ed6-b95d-e72e7906a171"
        },
        "node11": {
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
            "uuid": "db89c238-da61-482e-9631-25254e1999f0"
        },
        "node12": {
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
            "uuid": "51a7e931-7129-44d3-917f-3a805a045689"
        },
        "node13": {
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
            "uuid": "bdda7119-a8c3-4042-9189-e3ae822ede8a"
        },
        "node14": {
            "class": "ArtifactRemoval",
            "module": "neuropype.nodes.neural.ArtifactRemoval",
            "params": {
                "a": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "b": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "block_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "calib_seconds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 45
                },
                "cutoff": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 7.5
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "lookahead": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "max_dims": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "max_dropout_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "max_mem": {
                    "customized": false,
                    "type": "Port",
                    "value": 256
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "min_clean_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.25
                },
                "min_required_channels": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 2
                },
                "preserve_band": {
                    "customized": false,
                    "type": "DictPort",
                    "value": null
                },
                "riemannian": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stddev_cutoff": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "step_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_legacy": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "window_overlap_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -5,
                        7
                    ]
                }
            },
            "uuid": "9cabb996-56e0-4513-85d5-62ddaf8d27c9"
        },
        "node15": {
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
            "uuid": "260c20a3-4a44-4d97-9778-6cdd45f9c36c"
        },
        "node16": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
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
            "uuid": "5b13d9dd-bbba-4b27-b9c4-683d3ced66bf"
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
            "uuid": "4cc3c7fe-bd6b-40bd-8773-ffee00f7ebea"
        },
        "node3": {
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
            "uuid": "b66c9759-8f71-4321-a370-e445e00ff902"
        },
        "node4": {
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
            "uuid": "091ab53f-6555-4599-a264-02da915161b2"
        },
        "node5": {
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
            "uuid": "dbc3a6de-d9ff-4630-80fc-a9128d3d6971"
        },
        "node6": {
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
            "uuid": "7f00e191-bb7a-4146-a860-6466ba710999"
        },
        "node7": {
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
            "uuid": "fcd2c644-1466-44ad-80bb-9e042c168f52"
        },
        "node8": {
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
            "uuid": "eb26ef7a-9300-43b1-8c4d-ea034169af45"
        },
        "node9": {
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
            "uuid": "349b23ce-1446-4965-a76e-07600b6dfe62"
        }
    },
    "version": 1.1
}</patch>
</scheme>
