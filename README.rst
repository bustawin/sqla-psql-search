SQLA PSQL Search
################
Methods for building queries with Postgre's Full text search.

Based on `Rachid Belaid's post <http://rachbelaid.com/
postgres-full-text-search-is-good-enough/>`_,
`Code for America's post <https://www.codeforamerica.org/blog/2015/07/02/
multi-table-full-text-search-with-postgres-flask-and-sqlalchemy/>`_,
and `PSQL's search documentation <https://www.postgresql.org/docs/
11/textsearch-controls.html>`_.

This library requires PostgreSQL 11 or newer due to the usage of
``websearch_to_tsquery``.


Although the library is tested, automatic tests are required.
