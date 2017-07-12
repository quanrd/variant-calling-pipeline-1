#!/usr/bin/env python

# classes for each steps
class CreateFormatReferenceParams():
	scripts_dir = ''
	reference_dir = ''
	email = ''
	picard = ''
	partition = ''
	dictionary_out = ''
	regex = '.fa'
	fp = 'config'
	dictionary = '.dict'

class CreateAlignmentParams():
	input_dir = ''
	output_dir = ''
	scripts_dir = ''
	analysis_dir = ''
	reference_dir = ''
	bwa = ''
	email = ''
	sleep = ''
	partition = ''
	cpu_fqsam = ''
	fp = 'config'

class CreateQualityParams():
	input_dir = ''
	output_dir = ''
	qcheck_dir = ''
	fp = 'config'

class CreateBAMProcessingParams():
	tmp_dir = ''
	input_dir = ''
	output_dir = ''
	scripts_dir = ''
	analysis_dir = ''
	software_dir = ''
	reference_dir = ''
	jvm = ''
	gatk = ''
	email = ''
	picard = ''
	partition = ''
	cpu_sambam = ''
	fp = 'config'

class CreateMergeBAMParams():
	input_dir = ''
	output_dir = ''
	scripts_dir = ''
	analysis_dir = ''
	reference_dir = ''
	email = ''
	sleep = ''
	bamutil = ''
	samtools = ''
	partition = ''
	cpu_mergebam = ''
	fp = 'config'

class CreateVariantCallingParams():
	tmp_dir = ''
	input_dir = ''
	output_dir = ''
	scripts_dir = ''
	analysis_dir = ''
	software_dir = ''
	reference_dir = ''
	gatk = ''
	bgzip = ''
	email = ''
	sleep = ''
	tabix = ''
	htslib = ''
	samtools = ''
	partition = ''
	cpu_bamvcf = ''
	fp = 'config'
