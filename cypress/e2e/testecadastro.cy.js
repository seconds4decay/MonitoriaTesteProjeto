describe('template spec', () => {
  let name = 'teste';
  let email = 'teste@cypress.com';
  let password = '123456';

  before(() => {
    cy.visit('/')
    cy.get('[href="/login/"]').click()
    cy.get('[type="text"]').type(name)
    cy.get('[type="password"]').type(password)
    cy.get('[type="submit"]').click()
  })

  beforeEach(() => {
    cy.visit('/')
  })

  it('cadastrar loja', () => {
    cy.get('[href="/cadastroloja/"]').click()
    cy.get('[name="nome"]').type('dhsahjdaa')

    cy.get('[name="nome"]').invoke('val').as('nome')
    cy.get('[name="endereco"]').type('Rua do teste')
    cy.get('[name="telefone"]').type('999999999')
    cy.get('[type="submit"]').click()

    cy.visit('/lojas/')

    cy.get('@nome').then((nome) => {
      cy.get(':nth-child(2)').should('have.text', nome);
    });
  })


})