from yargy.relations.constructors import Relation

class new_gender_relation(Relation):
	label = 'gender_new'

	def __call__(self, form, other):
		if form.grams.number.plural and other.grams.number.plural:
			return True

		fem_types = ("ул", "пл", "наб")
		male_types = ("пр", "пр-кт", "пр-т", "пр-зд", "пр-д", \
					  "пер", "б-р", "б", "бул", "бр", "рн", "р-н", \
					  "мрн", "мкр", "р-он", "р")
		neut_types = ("ш",)
		(form_male, form_female, form_neutral,
		 form_bi, form_general) = form.grams.gender
		(other_male, other_female, other_neutral,
		 other_bi, other_general) = other.grams.gender
		if form.normalized in fem_types:
			form_female = True
		if other.normalized in fem_types:
			other_female = True
		if form.normalized in male_types:
			form_male = True
		if other.normalized in male_types:
			other_male = True
		if form.normalized in neut_types:
			form_neutral = True
		if other.normalized in neut_types:
			other_neutral = True
		return (
				(form_male and other_male)
				or (form_female and other_female)
				or (form_neutral and other_neutral)
				or (form_bi and (other_male or other_female))
				or (other_bi and (form_male or form_female))
				or form_general
				or other_general)


gender = new_gender_relation()