"""empty message

Revision ID: 44a003e0c556
Revises: b3623a352bec
Create Date: 2021-03-25 11:18:20.188942

"""
from alembic import op
import sqlalchemy as sa
import csv
from app.models import ObceORP


# revision identifiers, used by Alembic.
revision = '44a003e0c556'
down_revision = 'ce339c4a95d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ockovani_lide_profese',
    sa.Column('datum', sa.Date(), nullable=False),
    sa.Column('vakcina', sa.Unicode(), nullable=False),
    sa.Column('kraj_nuts_kod', sa.Unicode(), nullable=True),
    sa.Column('zarizeni_kod', sa.Unicode(), nullable=False),
    sa.Column('poradi_davky', sa.Integer(), nullable=False),
    sa.Column('vekova_skupina', sa.Unicode(), nullable=False),
    sa.Column('kraj_bydl_nuts', sa.Unicode(), nullable=False),
    sa.Column('indikace_zdravotnik', sa.Boolean(), nullable=False),
    sa.Column('indikace_socialni_sluzby', sa.Boolean(), nullable=False),
    sa.Column('indikace_ostatni', sa.Boolean(), nullable=False),
    sa.Column('indikace_pedagog', sa.Boolean(), nullable=False),
    sa.Column('indikace_skolstvi_ostatni', sa.Boolean(), nullable=False),
    sa.Column('pocet', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('datum', 'vakcina', 'zarizeni_kod', 'poradi_davky', 'vekova_skupina', 'kraj_bydl_nuts', 'indikace_zdravotnik', 'indikace_socialni_sluzby', 'indikace_ostatni', 'indikace_pedagog', 'indikace_skolstvi_ostatni')
    )
    op.create_table('obce_orp',
    sa.Column('kod_obce_orp', sa.Unicode(), nullable=False),
    sa.Column('nazev_obce', sa.Unicode(), nullable=True),
    sa.Column('okres_nuts', sa.Unicode(), nullable=True),
    sa.Column('kraj_nuts', sa.Unicode(), nullable=True),
    sa.Column('aken', sa.Unicode(), nullable=True),
    sa.Column('uzis_orp', sa.Unicode(), nullable=True),
    sa.ForeignKeyConstraint(['kraj_nuts'], ['kraje.id'], ),
    sa.ForeignKeyConstraint(['aken'], ['okresy.id'], ),
    sa.PrimaryKeyConstraint('kod_obce_orp')
    )
    
    with open('data/001_Ciselnik-ORP.csv', mode='r', encoding='utf-8') as orp_file:
        reader = csv.reader(orp_file, delimiter=';')
        next(reader, None)
        orp_arr = [{'kod_obce_orp': row[0], 'nazev_obce': row[1], 'okres_nuts': row[2], 'kraj_nuts': row[4], 'aken': row[6], 'uzis_orp': row[7] } for row in reader]

    # print(populace_arr)

    op.bulk_insert(ObceORP.__table__, orp_arr)



    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('obce_orp')
    op.drop_table('ockovani_lide_profese')
    # ### end Alembic commands ###