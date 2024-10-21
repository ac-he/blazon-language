#!/usr/bin/env python3

# WARNING: CAVEAT UTILITOR
#
#  This file was automatically generated by TatSu.
#
#     https://pypi.python.org/pypi/tatsu/
#
#  Any changes you make to it will be overwritten the next time
#  the file is generated.

# ruff: noqa: C405, COM812, I001, F401, PLR1702, PLC2801, SIM117

import sys
from pathlib import Path

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu
from tatsu.parsing import leftrec, nomemo, isname
from tatsu.infos import ParserConfig
from tatsu.util import re, generic_main


KEYWORDS: set[str] = set()


class BlazonBuffer(Buffer):
    def __init__(self, text, /, config: ParserConfig | None = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace='[ ]+',
            nameguard=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
            comments_re=None,
            eol_comments_re=None,
            keywords=KEYWORDS,
            start='start',
        )
        config = config.replace(**settings)

        super().__init__(text, config=config)


class BlazonParser(Parser):
    def __init__(self, /, config: ParserConfig | None = None, **settings):
        config = ParserConfig.new(
            config,
            owner=self,
            whitespace='[ ]+',
            nameguard=None,
            ignorecase=False,
            namechars='',
            parseinfo=False,
            comments_re=None,
            eol_comments_re=None,
            keywords=KEYWORDS,
            start='start',
        )
        config = config.replace(**settings)

        super().__init__(config=config)

    @tatsumasu()
    def _start_(self):
        with self._group():

            def block0():
                self._blazon_()
            self._closure(block0)
        self.name_last_node('blazons')
        self._check_eof()
        self._define(['blazons'], [])

    @tatsumasu()
    def _blazon_(self):
        self._division_()
        self._token('.')
        with self._group():
            with self._choice():
                with self._option():
                    self._pattern('[\\n]+')
                with self._option():
                    self._check_eof()
                self._error(
                    'expecting one of: '
                    '[\\n]+'
                )

    @tatsumasu()
    def _division_(self):
        with self._choice():
            with self._option():
                self._per_bend_()
            with self._option():
                self._per_bend_sinister_()
            with self._option():
                self._per_chevron_()
            with self._option():
                self._per_cross_()
            with self._option():
                self._per_fess_()
            with self._option():
                self._per_pale_()
            with self._option():
                self._per_pall_()
            with self._option():
                self._per_saltire_()
            with self._option():
                self._per_nothing_()
            self._error(
                'expecting one of: '
                "'Argent' 'Azure' 'Gules' 'Or' 'Per'"
                "'Purpure' 'Quarterly' 'Sable' 'Vert'"
                '<per_bend> <per_bend_sinister>'
                '<per_chevron> <per_cross> <per_fess>'
                '<per_nothing> <per_pale> <per_pall>'
                '<per_saltire> <tincture_cap>'
            )

    @tatsumasu()
    def _tincture_(self):
        with self._choice():
            with self._option():
                self._token('or')
            with self._option():
                self._token('argent')
            with self._option():
                self._token('azure')
            with self._option():
                self._token('gules')
            with self._option():
                self._token('purpure')
            with self._option():
                self._token('sable')
            with self._option():
                self._token('vert')
            self._error(
                'expecting one of: '
                "'argent' 'azure' 'gules' 'or' 'purpure'"
                "'sable' 'vert'"
            )

    @tatsumasu()
    def _tincture_cap_(self):
        with self._choice():
            with self._option():
                self._token('Or')
            with self._option():
                self._token('Argent')
            with self._option():
                self._token('Azure')
            with self._option():
                self._token('Gules')
            with self._option():
                self._token('Purpure')
            with self._option():
                self._token('Sable')
            with self._option():
                self._token('Vert')
            self._error(
                'expecting one of: '
                "'Argent' 'Azure' 'Gules' 'Or' 'Purpure'"
                "'Sable' 'Vert'"
            )

    @tatsumasu()
    def _quantity_plural_(self):
        with self._choice():
            with self._option():
                self._token('two')
            with self._option():
                self._token('three')
            self._error(
                'expecting one of: '
                "'three' 'two'"
            )

    @tatsumasu()
    def _quantity_singular_(self):
        with self._choice():
            with self._option():
                self._quantity_one_()
            with self._option():
                self._quantity_a_()
            self._error(
                'expecting one of: '
                "'a' 'an' 'one' <quantity_a>"
                '<quantity_one>'
            )

    @tatsumasu()
    def _quantity_one_(self):
        self._token('one')

    @tatsumasu()
    def _quantity_a_(self):
        with self._choice():
            with self._option():
                self._token('a')
            with self._option():
                self._token('an')
            self._error(
                'expecting one of: '
                "'a' 'an'"
            )

    @tatsumasu()
    def _charge_pattern_(self):
        with self._choice():
            with self._option():
                self._token('gyronny')
            with self._option():
                self._token('lozengy')
            with self._option():
                self._token('chequy')
            with self._option():
                self._token('fusily')
            self._error(
                'expecting one of: '
                "'chequy' 'fusily' 'gyronny' 'lozengy'"
            )

    @tatsumasu()
    def _tq_charge_pattern_(self):
        with self._group():
            self._charge_pattern_()
        self.name_last_node('charge')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'tincture'], [])

    @tatsumasu()
    def _charge_tincturable_singular_(self):
        with self._choice():
            with self._option():
                self._token('roundel')
            with self._option():
                self._token('crescent')
            with self._option():
                self._token('billet')
            with self._option():
                self._token('mullet')
            with self._option():
                self._token('caltrap')
            with self._option():
                self._token('martlet')
            with self._option():
                self._token('cross')
                self._token('pate')
            with self._option():
                self._token('annulet')
            with self._option():
                self._token('fusil')
            with self._option():
                self._token('fleur-de-lis')
            with self._option():
                self._token('lozenge')
            with self._option():
                self._token('rose')
            with self._option():
                self._token('mascle')
            with self._option():
                self._token('cross')
                self._token('moline')
            with self._option():
                self._token('rustre')
            with self._option():
                self._token('octofoil')
            with self._option():
                self._token('escutcheon')
            self._error(
                'expecting one of: '
                "'annulet' 'billet' 'caltrap' 'crescent'"
                "'cross' 'escutcheon' 'fleur-de-lis'"
                "'fusil' 'lozenge' 'martlet' 'mascle'"
                "'mullet' 'octofoil' 'rose' 'roundel'"
                "'rustre'"
            )

    @tatsumasu()
    def _charge_tincturable_plural_(self):
        with self._choice():
            with self._option():
                self._token('roundels')
            with self._option():
                self._token('crescents')
            with self._option():
                self._token('billets')
            with self._option():
                self._token('mullets')
            with self._option():
                self._token('caltraps')
            with self._option():
                self._token('martlets')
            with self._option():
                self._token('crosses')
                self._token('pate')
            with self._option():
                self._token('annulets')
            with self._option():
                self._token('fusils')
            with self._option():
                self._token('fleurs-de-lis')
            with self._option():
                self._token('lozenges')
            with self._option():
                self._token('roses')
            with self._option():
                self._token('mascles')
            with self._option():
                self._token('crosses')
                self._token('moline')
            with self._option():
                self._token('rustres')
            with self._option():
                self._token('octofoils')
            with self._option():
                self._token('escutcheons')
            self._error(
                'expecting one of: '
                "'annulets' 'billets' 'caltraps'"
                "'crescents' 'crosses' 'escutcheons'"
                "'fleurs-de-lis' 'fusils' 'lozenges'"
                "'martlets' 'mascles' 'mullets'"
                "'octofoils' 'roses' 'roundels' 'rustres'"
            )

    @tatsumasu()
    def _tq_charge_tincturable_singular_(self):
        with self._group():
            self._quantity_singular_()
        self.name_last_node('quantity')
        with self._group():
            self._charge_tincturable_singular_()
        self.name_last_node('charge')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'quantity', 'tincture'], [])

    @tatsumasu()
    def _tq_charge_tincturable_plural_(self):
        with self._group():
            self._quantity_plural_()
        self.name_last_node('quantity')
        with self._group():
            self._charge_tincturable_plural_()
        self.name_last_node('charge')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'quantity', 'tincture'], [])

    @tatsumasu()
    def _tq_charge_tincturable_(self):
        with self._choice():
            with self._option():
                self._tq_charge_tincturable_singular_()
            with self._option():
                self._tq_charge_tincturable_plural_()
            self._error(
                'expecting one of: '
                "'a' 'an' 'one' 'three' 'two'"
                '<quantity_a> <quantity_one>'
                '<quantity_plural> <quantity_singular>'
                '<tq_charge_tincturable_plural>'
                '<tq_charge_tincturable_singular>'
            )

    @tatsumasu()
    def _charge_large_(self):
        with self._choice():
            with self._option():
                self._token('gorge')
            with self._option():
                self._token('fret')
            self._error(
                'expecting one of: '
                "'fret' 'gorge'"
            )

    @tatsumasu()
    def _tq_charge_large_(self):
        with self._group():
            self._quantity_a_()
        self.name_last_node('quantity')
        with self._group():
            self._charge_large_()
        self.name_last_node('charge')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'quantity', 'tincture'], [])

    @tatsumasu()
    def _charge_label_(self):
        self._token('a')
        self._token('label')
        self._token('of')

    @tatsumasu()
    def _tq_label_singular_(self):
        self._quantity_one_()
        self._token('point')

    @tatsumasu()
    def _tq_label_plural_(self):
        self._quantity_plural_()
        self._token('points')

    @tatsumasu()
    def _tq_label_(self):
        with self._choice():
            with self._option():
                self._tq_label_singular_()
            with self._option():
                self._tq_label_plural_()
            self._error(
                'expecting one of: '
                "'one' 'three' 'two' <quantity_one>"
                '<quantity_plural> <tq_label_plural>'
                '<tq_label_singular>'
            )

    @tatsumasu()
    def _tq_charge_label_(self):
        with self._group():
            self._charge_label_()
        self.name_last_node('charge')
        with self._group():
            self._tq_label_()
        self.name_last_node('quantity')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'quantity', 'tincture'], [])

    @tatsumasu()
    def _charge_auto_singular_(self):
        with self._choice():
            with self._option():
                self._token('lion')
                self._token('rampant')
            with self._option():
                self._token('lion')
                self._token('passant')
            with self._option():
                self._token('crown')
            with self._option():
                self._token('scallop')
            with self._option():
                self._token('phoenix')
            with self._option():
                self._token('anchor')
            with self._option():
                self._token('bee')
            with self._option():
                self._token('castle')
            with self._option():
                self._token('dragon')
            with self._option():
                self._token('eagle')
            with self._option():
                self._token('dolphin')
            with self._option():
                self._token('griffin')
            with self._option():
                self._token('harp')
            with self._option():
                self._token('comet')
            with self._option():
                self._token('clarion')
            with self._option():
                self._token('set of keys saltirewise')
            with self._option():
                self._token('lamp')
            with self._option():
                self._token('moon in her plenitude')
            with self._option():
                self._token('sun in his splendor')
            with self._option():
                self._token('owl')
            with self._option():
                self._token('portcullis')
            with self._option():
                self._token('quatrefoil')
            with self._option():
                self._token('raven')
            with self._option():
                self._token('ship')
            with self._option():
                self._token('thistle')
            with self._option():
                self._token('unicorn')
            with self._option():
                self._token('wheel')
            with self._option():
                self._token('wolf')
            with self._option():
                self._token('sword')
            with self._option():
                self._token('yale')
            with self._option():
                self._token('zilant')
            self._error(
                'expecting one of: '
                "'anchor' 'bee' 'castle' 'clarion'"
                "'comet' 'crown' 'dolphin' 'dragon'"
                "'eagle' 'griffin' 'harp' 'lamp' 'lion'"
                "'moon in her plenitude' 'owl' 'phoenix'"
                "'portcullis' 'quatrefoil' 'raven'"
                "'scallop' 'set of keys saltirewise'"
                "'ship' 'sun in his splendor' 'sword'"
                "'thistle' 'unicorn' 'wheel' 'wolf'"
                "'yale' 'zilant'"
            )

    @tatsumasu()
    def _charge_auto_plural_(self):
        with self._choice():
            with self._option():
                self._token('lions')
                self._token('rampant')
            with self._option():
                self._token('lions')
                self._token('passant')
            with self._option():
                self._token('crowns')
            with self._option():
                self._token('scallops')
            with self._option():
                self._token('phoenixes')
            with self._option():
                self._token('anchors')
            with self._option():
                self._token('bees')
            with self._option():
                self._token('castles')
            with self._option():
                self._token('dragons')
            with self._option():
                self._token('eagles')
            with self._option():
                self._token('dolphins')
            with self._option():
                self._token('griffins')
            with self._option():
                self._token('harps')
            with self._option():
                self._token('comets')
            with self._option():
                self._token('clarions')
            with self._option():
                self._token('sets of keys saltirewise')
            with self._option():
                self._token('lamps')
            with self._option():
                self._token('moons in their plenitude')
            with self._option():
                self._token('suns in their splendor')
            with self._option():
                self._token('owls')
            with self._option():
                self._token('portcullises')
            with self._option():
                self._token('quatrefoils')
            with self._option():
                self._token('ravens')
            with self._option():
                self._token('ships')
            with self._option():
                self._token('thistles')
            with self._option():
                self._token('unicorns')
            with self._option():
                self._token('wheels')
            with self._option():
                self._token('wolves')
            with self._option():
                self._token('swords')
            with self._option():
                self._token('yales')
            with self._option():
                self._token('zilants')
            self._error(
                'expecting one of: '
                "'anchors' 'bees' 'castles' 'clarions'"
                "'comets' 'crowns' 'dolphins' 'dragons'"
                "'eagles' 'griffins' 'harps' 'lamps'"
                "'lions' 'moons in their plenitude'"
                "'owls' 'phoenixes' 'portcullises'"
                "'quatrefoils' 'ravens' 'scallops' 'sets"
                "of keys saltirewise' 'ships' 'suns in"
                "their splendor' 'swords' 'thistles'"
                "'unicorns' 'wheels' 'wolves' 'yales'"
                "'zilants'"
            )

    @tatsumasu()
    def _tq_charge_auto_singular_(self):
        with self._group():
            self._quantity_singular_()
        self.name_last_node('quantity')
        with self._group():
            self._charge_auto_singular_()
        self.name_last_node('charge')
        self._define(['charge', 'quantity'], [])

    @tatsumasu()
    def _tq_charge_auto_plural_(self):
        with self._group():
            self._quantity_plural_()
        self.name_last_node('quantity')
        with self._group():
            self._charge_auto_plural_()
        self.name_last_node('charge')
        self._define(['charge', 'quantity'], [])

    @tatsumasu()
    def _tq_charge_auto_(self):
        with self._choice():
            with self._option():
                self._tq_charge_auto_singular_()
            with self._option():
                self._tq_charge_auto_plural_()
            self._error(
                'expecting one of: '
                "'a' 'an' 'one' 'three' 'two'"
                '<quantity_a> <quantity_one>'
                '<quantity_plural> <quantity_singular>'
                '<tq_charge_auto_plural>'
                '<tq_charge_auto_singular>'
            )

    @tatsumasu()
    def _tq_charge_quarterly_(self):
        with self._group():
            self._token('quarterly')
            self._token('of')
            self._token('eight')
        self.name_last_node('charge')
        self._token(':')
        with self._group():
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
            self._token(',')
            self._tincture_()
        self.name_last_node('tincture')
        self._define(['charge', 'tincture'], [])

    @tatsumasu()
    def _charge_phrase_(self):
        with self._choice():
            with self._option():
                self._tq_charge_pattern_()
            with self._option():
                self._tq_charge_auto_()
            with self._option():
                self._tq_charge_tincturable_()
            with self._option():
                self._tq_charge_large_()
            with self._option():
                self._tq_charge_label_()
            with self._option():
                self._tq_charge_quarterly_()
            self._error(
                'expecting one of: '
                "'a' 'an' 'chequy' 'fusily' 'gyronny'"
                "'lozengy' 'one' 'quarterly' 'three'"
                "'two' <charge_label> <charge_pattern>"
                '<quantity_a> <quantity_one>'
                '<quantity_plural> <quantity_singular>'
                '<tq_charge_auto> <tq_charge_auto_plural>'
                '<tq_charge_auto_singular>'
                '<tq_charge_label> <tq_charge_large>'
                '<tq_charge_pattern>'
                '<tq_charge_quarterly>'
                '<tq_charge_tincturable>'
                '<tq_charge_tincturable_plural>'
                '<tq_charge_tincturable_singular>'
            )

    @tatsumasu()
    def _per_bend_(self):
        self._token('Per')
        self._token('bend')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        with self._optional():
            self._token('in')
            self._token('chief')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('chief')
            self._token(',')
            self._define(['chief'], [])
        self._token('in')
        self._token('base')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('base')
        self._define(['base', 'chief', 'tincture'], [])

    @tatsumasu()
    def _per_bend_sinister_(self):
        self._token('Per')
        self._token('bend')
        self._token('sinister')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        with self._optional():
            self._token('in')
            self._token('chief')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('chief')
            self._token(',')
            self._define(['chief'], [])
        self._token('in')
        self._token('base')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('base')
        self._define(['base', 'chief', 'tincture'], [])

    @tatsumasu()
    def _per_chevron_(self):
        self._token('Per')
        self._token('chevron')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        self._token('in')
        self._token('chief')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('chief')
        with self._optional():
            self._token(',')
            self._token('in')
            self._token('base')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('base')
            self._define(['base'], [])
        self._define(['base', 'chief', 'tincture'], [])

    @tatsumasu()
    def _per_cross_(self):
        self._token('Quarterly')
        self._token(';')
        self._token('I.')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        with self._optional():
            self._token(',')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('charge')
            self._define(['charge'], [])
        self._token(',')
        self._token('II.')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('charge')
        self._token(',')
        self._token('III.')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('charge')
        self._token(',')
        self._token('IV.')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('charge')
        self._define(['charge', 'tincture'], [])

    @tatsumasu()
    def _per_fess_(self):
        self._token('Per')
        self._token('fess')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        self._token('in')
        self._token('chief')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('chief')
        self._token(',')
        self._token('in')
        self._token('base')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('base')
        with self._optional():
            self._token(';')
            self._token('in')
            self._token('the')
            self._token('center')
            with self._group():
                with self._choice():
                    with self._option():
                        with self._group():
                            self._token('on')
                            self._token('an')
                            self._token('escutcheon')
                            with self._group():
                                self._tincture_()
                            self.name_last_node('tincture')
                            with self._group():
                                self._charge_phrase_()
                            self.name_last_node('escutcheon')
                            self._define(['escutcheon', 'tincture'], [])
                    with self._option():
                        with self._group():
                            self._token('an')
                            self._token('escutcheon')
                            with self._group():
                                self._tincture_()
                            self.name_last_node('tincture')
                            self._define(['tincture'], [])
                    self._error(
                        'expecting one of: '
                        "'an' 'on'"
                    )
            self._define(['escutcheon', 'tincture'], [])
        self._define(['base', 'chief', 'escutcheon', 'tincture'], [])

    @tatsumasu()
    def _per_pale_(self):
        self._token('Per')
        self._token('pale')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        self._token('to')
        self._token('dexter')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('dexter')
        self._token(',')
        self._token('to')
        self._token('sinister')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('sinister')
        self._define(['dexter', 'sinister', 'tincture'], [])

    @tatsumasu()
    def _per_pall_(self):
        self._token('Per')
        self._token('pall')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        with self._optional():
            self._token('in')
            self._token('chief')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('chief')
            self._token(',')
            self._define(['chief'], [])
        self._token('to')
        self._token('dexter')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('dexter')
        self._token(',')
        self._token('to')
        self._token('sinister')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('sinister')
        self._define(['chief', 'dexter', 'sinister', 'tincture'], [])

    @tatsumasu()
    def _per_saltire_(self):
        self._token('Per')
        self._token('saltire')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(',')
        self._token('and')
        with self._group():
            self._tincture_()
        self.name_last_node('tincture')
        self._token(';')
        with self._optional():
            self._token('in')
            self._token('chief')
            with self._group():
                self._charge_phrase_()
            self.name_last_node('chief')
            self._token(',')
            self._define(['chief'], [])
        self._token('to')
        self._token('dexter')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('dexter')
        self._token(',')
        self._token('to')
        self._token('sinister')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('sinister')
        self._token(',')
        self._token('in')
        self._token('base')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('base')
        self._define(['base', 'chief', 'dexter', 'sinister', 'tincture'], [])

    @tatsumasu()
    def _per_nothing_(self):
        with self._group():
            self._tincture_cap_()
        self.name_last_node('field_tincture')
        self._token(',')
        with self._group():
            self._charge_phrase_()
        self.name_last_node('charge')
        self._define(['charge', 'field_tincture'], [])


def main(filename, **kwargs):
    if not filename or filename == '-':
        text = sys.stdin.read()
    else:
        text = Path(filename).read_text()
    parser = BlazonParser()
    return parser.parse(
        text,
        filename=filename,
        **kwargs,
    )


if __name__ == '__main__':
    import json
    from tatsu.util import asjson

    ast = generic_main(main, BlazonParser, name='Blazon')
    data = asjson(ast)
    print(json.dumps(data, indent=2))
