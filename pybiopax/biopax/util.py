__all__ = ['UtilityClass', 'Evidence', 'Provenance',
           'EntityFeature', 'ModificationFeature', 'FragmentFeature',
           'BindingFeature', 'KPrime', 'BioSource',
           'ExperimentalForm', 'SequenceLocation', 'SequenceInterval',
           'SequenceSite', 'PathwayStep', 'Xref', 'PublicationXref',
           'UnificationXref', 'RelationshipXref', 'EntityReference',
           'ProteinReference', 'RnaReference', 'DnaReference',
           'SmallMoleculeReference', 'RnaRegionReference',
           'DnaRegionReference', 'SequenceEntityReference',
           'ChemicalStructure', 'Stoichiometry', 'ControlledVocabulary',
           'CellularLocationVocabulary', 'EntityReferenceTypeVocabulary',
           'EvidenceCodeVocabulary', 'ExperimentalFormVocabulary',
           'InteractionVocabulary', 'PhenotypeVocabulary',
           'RelationshipTypeVocabulary', 'SequenceModificationVocabulary',
           'SequenceRegionVocabulary', 'TissueVocabulary', 'CellVocabulary']

from .base import BioPaxObject


class UtilityClass(BioPaxObject):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)


class Evidence(UtilityClass):
    def __init__(self,
                 confidence=None,
                 evidence_code=None,
                 experimental_form=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.confidence = confidence
        self.evidence_code = evidence_code
        self.experimental_form = experimental_form


class Provenance(UtilityClass):
    def __init__(self,
                 standard_name=None,
                 display_name=None,
                 all_names=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.standard_name = standard_name
        self.display_name = display_name
        self.all_names = all_names


class EntityFeature(UtilityClass):
    list_types = ['evidence']

    def __init__(self,
                 evidence=None,
                 owner_entity_reference=None,
                 feature_of=None,
                 not_feature_of=None,
                 feature_location=None,
                 member_feature=None,
                 feature_location_type=None,
                 member_feature_of=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.evidence = evidence
        self.owner_entity_reference = owner_entity_reference
        self.feature_of = feature_of
        self.not_feature_of = not_feature_of
        self.feature_location = feature_location
        self.member_feature = member_feature
        self.feature_location_type = feature_location_type
        self.member_feature_of = member_feature_of


class ModificationFeature(EntityFeature):
    def __init__(self,
                 modification_type=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.modification_type = modification_type


class FragmentFeature(EntityFeature):
    pass


class BindingFeature(EntityFeature):
    def __init__(self,
                 binds_to=None,
                 intramolecular=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.binds_to = binds_to
        self.intramolecular = intramolecular


class KPrime(UtilityClass):
    def __init__(self, k_prime, **kwargs):
        super().__init__(**kwargs)
        self.k_prime = k_prime


class BioSource(UtilityClass):
    def __init__(self,
                 cell_type=None,
                 tissue=None,
                 standard_name=None,
                 display_name=None,
                 all_names=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.cell_type = cell_type
        self.tissue = tissue
        self.standard_name = standard_name
        self.display_name = display_name
        self.all_names = all_names


class ExperimentalForm(UtilityClass):
    def __init__(self,
                 experimental_form_entity=None,
                 experimental_form_description=None,
                 experimental_feature=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.experimental_form_entity = experimental_form_entity
        self.experimental_form_description = experimental_form_description
        self.experimental_form_feature = experimental_feature


class SequenceLocation(UtilityClass):
    def __init__(self,
                 region_type=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.region_type = region_type


class SequenceInterval(SequenceLocation):
    def __init__(self,
                 sequence_interval_begin=None,
                 sequence_interval_end=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.sequence_interval_begin = sequence_interval_begin
        self.sequence_interval_end = sequence_interval_end


class SequenceSite(SequenceLocation):
    def __init__(self,
                 position_status=None,
                 sequence_position=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.position_status = position_status
        self.sequence_position = sequence_position


class PathwayStep(UtilityClass):
    list_types = ['evidence']

    def __init__(self,
                 step_process=None,
                 next_step=None,
                 next_step_of=None,
                 pathway_order_of=None,
                 evidence=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.step_process = step_process
        self.next_step = next_step
        self.next_step_of = next_step_of
        self.pathway_order_of = pathway_order_of
        self.evidence = evidence


class Xref(UtilityClass):
    def __init__(self,
                 db=None,
                 id=None,
                 db_version=None,
                 id_version=None,
                 xref_of=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.db = db
        self.db_version = db_version
        self.id_version = id_version
        self.id = id
        self.xref_of = xref_of


class PublicationXref(Xref):
    def __init__(self,
                 title=None,
                 url=None,
                 source=None,
                 author=None,
                 year=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.url = url
        self.source = source
        self.author = author
        self.year = year


class UnificationXref(Xref):
    pass


class RelationshipXref(Xref):
    def __init__(self,
                 relationship_type=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.relationship_type = relationship_type


class Score(UtilityClass):
    pass


class EntityReference(UtilityClass):
    list_types = ['evidence', 'entity_feature']

    def __init__(self,
                 entity_feature=None,
                 entity_reference_of=None,
                 evidence=None,
                 entity_reference_type=None,
                 member_entity_reference=None,
                 owner_entity_reference=None,
                 xref=None,
                 standard_name=None,
                 display_name=None,
                 all_names=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.entity_feature = entity_feature
        self.entity_reference_of = entity_reference_of
        self.evidence = evidence
        self.entity_reference_type = entity_reference_type
        self.member_entity_reference = member_entity_reference
        self.owner_entity_reference = owner_entity_reference
        # TODO: is xref in the right location here?
        self.xref = xref
        self.standard_name = standard_name
        self.display_name = display_name
        self.all_names = all_names


class SequenceEntityReference(EntityReference):
    def __init__(self,
                 organism=None,
                 sequence=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.organism = organism
        self.sequence = sequence


class RnaReference(EntityReference):
    pass


class RnaRegionReference(EntityReference):
    pass


class ProteinReference(SequenceEntityReference):
    pass


class SmallMoleculeReference(EntityReference):
    def __init__(self,
                 structure=None,
                 chemical_formula=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.structure = structure
        self.chemical_formula = chemical_formula


class DnaReference(EntityReference):
    pass


class DnaRegionReference(EntityReference):
    pass


class ChemicalStructure(UtilityClass):
    def __init__(self,
                 structure_format=None,
                 structure_data=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.structure_format = structure_format
        self.structure_data = structure_data


class Stoichiometry(UtilityClass):
    def __init__(self,
                 stoichiometric_coefficient=None,
                 physical_entity=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.stoichiometric_coefficient = stoichiometric_coefficient
        self.physical_entity = physical_entity


class ControlledVocabulary(UtilityClass):
    def __init__(self, term=None, **kwargs):
        super().__init__(**kwargs)
        self.term = term


class ExperimentalFormVocabulary(ControlledVocabulary):
    pass


class RelationshipTypeVocabulary(ControlledVocabulary):
    pass


class CellularLocationVocabulary(ControlledVocabulary):
    pass


class EntityReferenceTypeVocabulary(ControlledVocabulary):
    pass


class PhenotypeVocabulary(ControlledVocabulary):
    pass


class TissueVocabulary(ControlledVocabulary):
    pass


class EvidenceCodeVocabulary(ControlledVocabulary):
    pass


class SequenceModificationVocabulary(ControlledVocabulary):
    pass


class SequenceRegionVocabulary(ControlledVocabulary):
    pass


class InteractionVocabulary(ControlledVocabulary):
    pass


class CellVocabulary(ControlledVocabulary):
    pass